(function () {
  const STORAGE_KEY = "api-bootcamp-progress";
  const STARTED_KEY = "api-bootcamp-started";
  const STEP_STORAGE_PREFIX = "api-bootcamp-step-";
  const EXERCISE_STORAGE_PREFIX = "api-bootcamp-exercise-";
  const EXERCISE_DONE_PREFIX = "api-bootcamp-exdone-";
  const CHECKLIST_PREFIX = "api-bootcamp-checklist-";
  const SYNC_PREFIX = "api-bootcamp-";
  const SIDEBAR_KEY = "api-bootcamp-sidebar-collapsed";

  function initSidebarToggle() {
    const shell = document.getElementById("app-shell");
    const hideBtn = document.getElementById("btn-hide-sidebar");
    const showBtn = document.getElementById("btn-show-sidebar");
    if (!shell) return;

    function apply(collapsed) {
      shell.classList.toggle("sidebar-collapsed", collapsed);
      localStorage.setItem(SIDEBAR_KEY, collapsed ? "1" : "0");
    }

    apply(localStorage.getItem(SIDEBAR_KEY) === "1");
    hideBtn?.addEventListener("click", () => apply(true));
    showBtn?.addEventListener("click", () => apply(false));
  }

  let syncTimer = null;
  let syncReady = false;

  function readJson(key, fallback) {
    try {
      return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback));
    } catch {
      return fallback;
    }
  }

  function writeJson(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
    scheduleProgressSync();
  }

  function collectProgressSnapshot() {
    const data = {};
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (!key || !key.startsWith(SYNC_PREFIX)) continue;
      try {
        data[key] = JSON.parse(localStorage.getItem(key));
      } catch {
        data[key] = localStorage.getItem(key);
      }
    }
    return data;
  }

  function applyProgressSnapshot(data) {
    Object.entries(data || {}).forEach(([key, value]) => {
      if (!key.startsWith(SYNC_PREFIX)) return;
      localStorage.setItem(
        key,
        typeof value === "string" ? value : JSON.stringify(value)
      );
    });
  }

  function mergeSnapshots(local, remote) {
    const keys = new Set([
      ...Object.keys(local || {}),
      ...Object.keys(remote || {}),
    ]);
    const merged = {};
    keys.forEach((key) => {
      const a = local ? local[key] : undefined;
      const b = remote ? remote[key] : undefined;
      if (Array.isArray(a) || Array.isArray(b)) {
        merged[key] = [
          ...new Set([
            ...(Array.isArray(b) ? b : []),
            ...(Array.isArray(a) ? a : []),
          ]),
        ];
      } else if (
        a &&
        b &&
        typeof a === "object" &&
        typeof b === "object" &&
        !Array.isArray(a) &&
        !Array.isArray(b)
      ) {
        merged[key] = { ...b, ...a };
      } else {
        merged[key] = a !== undefined ? a : b;
      }
    });
    return merged;
  }

  function scheduleProgressSync() {
    if (!syncReady) return;
    clearTimeout(syncTimer);
    syncTimer = setTimeout(pushProgressToServer, 400);
  }

  async function pushProgressToServer() {
    try {
      await fetch("/api/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ progress: collectProgressSnapshot() }),
      });
    } catch {
      // Offline / server restart — local progress still works
    }
  }

  async function pullProgressFromServer() {
    try {
      const res = await fetch("/api/progress");
      if (!res.ok) return;
      const data = await res.json();
      const remote = data.progress || {};
      const local = collectProgressSnapshot();
      const merged = mergeSnapshots(local, remote);
      applyProgressSnapshot(merged);
      // Push merged result so both sides stay in sync
      await fetch("/api/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ progress: merged }),
      });
    } catch {
      // Keep local-only if sync fails
    }
  }

  function getProgress() {
    return readJson(STORAGE_KEY, []);
  }

  function getStarted() {
    return readJson(STARTED_KEY, []);
  }

  function markStarted(lessonId) {
    if (!lessonId) return;
    const ids = getStarted();
    if (!ids.includes(lessonId)) {
      ids.push(lessonId);
      writeJson(STARTED_KEY, ids);
    }
  }

  function isComplete(lessonId) {
    return getProgress().includes(lessonId);
  }

  function saveProgress(ids) {
    writeJson(STORAGE_KEY, ids);
    updateProgressUI();
  }

  function markComplete(lessonId) {
    if (!lessonId) return;
    markStarted(lessonId);
    const ids = getProgress();
    if (!ids.includes(lessonId)) {
      ids.push(lessonId);
      saveProgress(ids);
    } else {
      updateProgressUI();
    }
    refreshCompleteButton();
  }

  function unmarkComplete(lessonId) {
    saveProgress(getProgress().filter((id) => id !== lessonId));
    refreshCompleteButton();
  }

  function markExerciseDone(lessonId, exerciseId) {
    if (!lessonId || !exerciseId) return;
    const key = EXERCISE_DONE_PREFIX + lessonId;
    const done = readJson(key, []);
    if (!done.includes(exerciseId)) {
      done.push(exerciseId);
      writeJson(key, done);
    }
    updateExercisePickerUI();
    const exercises = window.LESSON_EXERCISES || [];
    if (exercises.length && done.length >= exercises.length) {
      markComplete(lessonId);
    }
  }

  function getExerciseDone(lessonId) {
    return readJson(EXERCISE_DONE_PREFIX + lessonId, []);
  }

  function refreshCompleteButton() {
    const btn = document.getElementById("btn-complete");
    if (!btn) return;
    const lessonId = btn.dataset.lessonId || window.LESSON_ID;
    if (isComplete(lessonId)) {
      btn.textContent = "Completed ✓";
      btn.classList.add("is-complete");
      btn.setAttribute("aria-pressed", "true");
    } else {
      btn.textContent = "Mark complete";
      btn.classList.remove("is-complete");
      btn.setAttribute("aria-pressed", "false");
    }
  }

  function updateModuleProgress() {
    document.querySelectorAll("[data-module-lessons]").forEach((el) => {
      const ids = (el.dataset.moduleLessons || "").split(",").filter(Boolean);
      if (!ids.length) return;
      const done = ids.filter((id) => isComplete(id)).length;
      const pct = Math.round((done / ids.length) * 100);
      const fill = el.querySelector(".module-progress-fill");
      const label = el.querySelector(".module-progress-label");
      if (fill) fill.style.width = pct + "%";
      if (label) label.textContent = `${done}/${ids.length} complete`;
      el.classList.toggle("module-done", done === ids.length);

      const mastery = (el.dataset.masteryLessons || "").split(",").filter(Boolean);
      const masteryDone =
        mastery.length > 0 && mastery.every((id) => isComplete(id));
      el.classList.toggle("mastery-complete", masteryDone);
    });
  }

  function updateProgressUI() {
    const ids = getProgress();
    const started = getStarted();
    const total = window.COURSE_TOTAL || 0;
    const pct = total ? Math.round((ids.length / total) * 100) : 0;

    const fill = document.getElementById("progress-fill");
    const pctEl = document.getElementById("progress-pct");
    const countEl = document.getElementById("progress-count");
    const dashPct = document.getElementById("dash-progress");
    const dashCount = document.getElementById("dash-progress-count");

    if (fill) fill.style.width = pct + "%";
    if (pctEl) pctEl.textContent = pct + "%";
    if (countEl) countEl.textContent = `${ids.length}/${total} lessons`;
    if (dashPct) dashPct.textContent = pct + "%";
    if (dashCount) dashCount.textContent = `${ids.length} of ${total} lessons complete`;

    document.querySelectorAll("[data-check]").forEach((el) => {
      const done = ids.includes(el.dataset.check);
      el.classList.toggle("done", done);
      el.setAttribute("aria-label", done ? "Completed" : "Not completed");
    });

    document.querySelectorAll(".nav-lesson[data-lesson-id]").forEach((el) => {
      const id = el.dataset.lessonId;
      el.classList.toggle("completed", ids.includes(id));
      el.classList.toggle("started", started.includes(id) && !ids.includes(id));
    });

    document.querySelectorAll(".module-lessons a[data-lesson-id]").forEach((el) => {
      el.classList.toggle("completed", ids.includes(el.dataset.lessonId));
    });

    updateModuleProgress();
    refreshCompleteButton();
  }

  async function checkMockApis() {
    const el = document.getElementById("api-status");
    if (!el) return;
    try {
      const res = await fetch("/api/mock-status");
      const data = await res.json();
      el.classList.remove("online", "offline", "partial");
      if (data.online) {
        el.classList.add("online");
        el.querySelector(".status-text").textContent = "Mock APIs online";
      } else if (data.source || data.destination) {
        el.classList.add("partial");
        el.querySelector(".status-text").textContent = "Partial — start both APIs";
      } else {
        el.classList.add("offline");
        el.querySelector(".status-text").textContent = "Mock APIs offline";
      }
    } catch {
      el.classList.add("offline");
      el.querySelector(".status-text").textContent = "Cannot reach course server";
    }
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  let lessonSteps = [];
  let currentStepIndex = 0;
  let lastAnalyzeResult = null;
  let currentExerciseId = null;
  let currentExercise = null;
  let allExercises = [];
  let analyzeFailCounts = {};
  let hideExamplesDefault = false;
  let revealedSteps = {};

  function updateExercisePickerUI() {
    const picker = document.getElementById("exercise-picker");
    if (!picker || !allExercises.length) return;
    const done = getExerciseDone(window.LESSON_ID);
    picker.innerHTML = allExercises
      .map((ex) => {
        const isDone = done.includes(ex.id);
        const isActive = ex.id === currentExerciseId;
        return `<button type="button" class="exercise-tab ${isActive ? "active" : ""} ${isDone ? "done" : ""}" data-exercise-id="${ex.id}">
          <span class="ex-label">${isDone ? "✓" : ex.label}</span>
          <span class="ex-title">${escapeHtml(ex.title)}</span>
          ${isDone ? '<span class="ex-check">done</span>' : ""}
        </button>`;
      })
      .join("");

    picker.querySelectorAll(".exercise-tab").forEach((btn) => {
      btn.addEventListener("click", () => switchExercise(btn.dataset.exerciseId));
    });
  }

  async function loadExercises() {
    if (!window.HAS_INTERACTIVE || !window.LESSON_ID) return;
    const res = await fetch("/api/exercises/" + window.LESSON_ID);
    const data = await res.json();
    allExercises = data.exercises || [];
    window.LESSON_EXERCISES = allExercises;

    const saved = localStorage.getItem(EXERCISE_STORAGE_PREFIX + window.LESSON_ID);
    currentExerciseId = saved || (allExercises[0] && allExercises[0].id);
    currentExercise = allExercises.find((e) => e.id === currentExerciseId) || allExercises[0];
    hideExamplesDefault = !!(currentExercise && currentExercise.hide_examples);

    updateExercisePickerUI();
    if (currentExercise) {
      document.getElementById("exercise-scenario").innerHTML =
        `<strong>Scenario:</strong> ${escapeHtml(currentExercise.scenario)}`;
      await loadWorkspaceForExercise(currentExercise);
      await loadStepsForExercise(currentExerciseId);
    }
  }

  async function switchExercise(exerciseId) {
    if (exerciseId === currentExerciseId) return;
    const editor = document.getElementById("code-editor");
    if (editor) await saveWorkspace(editor);

    currentExerciseId = exerciseId;
    currentExercise = allExercises.find((e) => e.id === exerciseId);
    localStorage.setItem(EXERCISE_STORAGE_PREFIX + window.LESSON_ID, exerciseId);
    scheduleProgressSync();

    updateExercisePickerUI();
    if (currentExercise) {
      document.getElementById("exercise-scenario").innerHTML =
        `<strong>Scenario:</strong> ${escapeHtml(currentExercise.scenario)}`;
      await loadWorkspaceForExercise(currentExercise);
      await loadStepsForExercise(exerciseId);
      resetAnalyzePanel();
    }
  }

  async function loadWorkspaceForExercise(exercise) {
    const editor = document.getElementById("code-editor");
    const filenameEl = document.getElementById("workspace-filename");
    const verifyBtn = document.getElementById("btn-verify");
    window.WORKSPACE_FILE = exercise.workspace_file;

    if (filenameEl) filenameEl.textContent = exercise.workspace_file;
    if (verifyBtn) {
      verifyBtn.style.display = exercise.has_verify ? "inline-flex" : "none";
    }

    let url = "/api/workspace/" + exercise.workspace_file;
    if (exercise.starter_file) {
      url += "?starter=" + encodeURIComponent(exercise.starter_file);
    }
    const res = await fetch(url);
    const data = await res.json();
    if (editor) editor.value = data.content || "";
    const saveIndicator = document.getElementById("save-indicator");
    if (saveIndicator) {
      saveIndicator.textContent = data.seeded_from ? "Seeded from broken starter" : "Saved";
      saveIndicator.classList.remove("unsaved");
    }
  }

  async function saveWorkspace(editor) {
    if (!window.WORKSPACE_FILE || !editor) return;
    await fetch("/api/workspace/" + window.WORKSPACE_FILE, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: editor.value }),
    });
  }

  async function loadStepsForExercise(exerciseId) {
    const list = document.getElementById("steps-list");
    if (!list) return;

    const res = await fetch(`/api/steps/${window.LESSON_ID}?exercise=${exerciseId}`);
    const data = await res.json();
    lessonSteps = data.steps || [];
    hideExamplesDefault = !!data.hide_examples;
    analyzeFailCounts = {};
    revealedSteps = {};

    const saved = parseInt(
      localStorage.getItem(STEP_STORAGE_PREFIX + window.LESSON_ID + "-" + exerciseId) || "0",
      10
    );
    currentStepIndex = Math.min(saved, Math.max(lessonSteps.length - 1, 0));
    lastAnalyzeResult = null;

    renderStepsList();
    renderStepDots(0, lessonSteps.length);
  }

  function resetAnalyzePanel() {
    lastAnalyzeResult = null;
    analyzeFailCounts = {};
    const summaryText = document.getElementById("analyze-summary-text");
    const checksEl = document.getElementById("analyze-checks");
    const summaryEl = document.getElementById("analyze-summary");
    if (summaryEl) summaryEl.classList.remove("pass", "fail", "warn");
    if (summaryText) summaryText.textContent = "Type code for this exercise, then hit Analyze.";
    if (checksEl) checksEl.innerHTML = "";
  }

  function formatTeaching(text) {
    return String(text || "")
      .split(/\n\n+/)
      .filter(Boolean)
      .map((p) => `<p>${escapeHtml(p)}</p>`)
      .join("");
  }

  function stripExampleFromInstruction(instruction) {
    const text = String(instruction || "");
    const cut = text.search(/\nEXAMPLE:\n/i);
    if (cut === -1) return text.trim();
    const before = text.slice(0, cut).trim();
    const after = text.slice(cut).replace(/^[\s\S]*?\n\n/, "").trim();
    // Keep the human guidance after the example block if present
    const parts = [before];
    if (after && !/^EXAMPLE:/i.test(after)) parts.push(after);
    return parts.filter(Boolean).join("\n\n");
  }

  function renderStepsList() {
    const list = document.getElementById("steps-list");
    if (!list) return;

    list.innerHTML = lessonSteps
      .map((step, i) => {
        const status = getStepStatus(i);
        const isActive = i === currentStepIndex;
        const isPassed = status === "passed";
        const fails = analyzeFailCounts[i] || 0;
        const revealAfter = step.reveal_after_fails != null ? step.reveal_after_fails : 2;
        const showExample =
          isActive &&
          step.example &&
          (!hideExamplesDefault || revealedSteps[i] || fails >= revealAfter);
        const showRevealBtn =
          isActive &&
          hideExamplesDefault &&
          step.example &&
          !revealedSteps[i] &&
          fails >= revealAfter;

        if (!isActive && !isPassed) {
          return `<div class="step-card pending-collapsed" data-step="${i}">
            <div class="step-card-head">
              <span class="step-num">${i + 1}</span>
              <strong>${escapeHtml(step.title)}</strong>
              <span class="step-locked">locked until you finish step ${currentStepIndex + 1}</span>
            </div>
          </div>`;
        }

        if (isPassed && !isActive) {
          return `<div class="step-card passed collapsed" data-step="${i}">
            <div class="step-card-head">
              <span class="step-num">✓</span>
              <strong>${escapeHtml(step.title)}</strong>
            </div>
          </div>`;
        }

        const exampleHtml = showExample
          ? `<div class="step-example-wrap"><div class="step-label">Type this</div><pre class="step-example">${escapeHtml(step.example)}</pre></div>`
          : "";
        const contextHtml = step.context
          ? `<div class="step-context"><div class="step-label">What's going on</div>${formatTeaching(step.context)}</div>`
          : "";
        const whyHtml = step.why && step.why !== (step.context || "").split("\n\n")[0]
          ? `<p class="step-why"><strong>Why this matters:</strong> ${escapeHtml(step.why)}</p>`
          : "";
        const mistakeHtml = step.common_mistake
          ? `<p class="step-mistake"><strong>Common mistake:</strong> ${escapeHtml(step.common_mistake)}</p>`
          : "";
        const revealHtml = showRevealBtn
          ? `<button type="button" class="btn btn-sm btn-secondary btn-reveal-example" data-reveal-step="${i}">Reveal example</button>`
          : hideExamplesDefault && isActive && step.example && !revealedSteps[i]
            ? `<p class="step-exam-hint">Exam mode: examples stay hidden until you try Analyze a couple times.</p>`
            : "";

        return `<div class="step-card ${status} active" data-step="${i}">
          <div class="step-card-head">
            <span class="step-num">${isPassed ? "✓" : i + 1}</span>
            <strong>${escapeHtml(step.title)}</strong>
          </div>
          ${contextHtml}
          <div class="step-do">
            <div class="step-label">What to do</div>
            <p class="step-instruction">${escapeHtml(stripExampleFromInstruction(step.instruction))}</p>
          </div>
          ${whyHtml}
          ${mistakeHtml}
          ${revealHtml}
          ${exampleHtml}
        </div>`;
      })
      .join("");

    list.querySelectorAll(".step-card.passed.collapsed, .step-card.active").forEach((card) => {
      card.addEventListener("click", (e) => {
        if (e.target.closest(".btn-reveal-example")) return;
        const idx = parseInt(card.dataset.step, 10);
        if (getStepStatus(idx) === "passed" || idx === currentStepIndex) {
          currentStepIndex = idx;
          renderStepsList();
        }
      });
    });

    list.querySelectorAll(".btn-reveal-example").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        const idx = parseInt(btn.dataset.revealStep, 10);
        revealedSteps[idx] = true;
        renderStepsList();
      });
    });
  }

  function getStepStatus(index) {
    if (lastAnalyzeResult && lastAnalyzeResult.steps[index]) {
      return lastAnalyzeResult.steps[index].passed
        ? "passed"
        : index === currentStepIndex
          ? "current"
          : "pending";
    }
    return index === currentStepIndex ? "current" : "pending";
  }

  function renderStepDots(passed, total) {
    const dots = document.getElementById("steps-dots");
    const counter = document.getElementById("steps-counter");
    const label = document.getElementById("steps-passed-label");
    if (!dots) return;

    dots.innerHTML = Array.from({ length: total }, (_, i) => {
      let cls = "step-dot";
      if (lastAnalyzeResult && lastAnalyzeResult.steps[i]?.passed) cls += " done";
      else if (i === currentStepIndex) cls += " current";
      return `<span class="${cls}"></span>`;
    }).join("");

    if (counter) counter.textContent = `Step ${Math.min(currentStepIndex + 1, total)} of ${total}`;
    if (label) label.textContent = passed > 0 ? `${passed}/${total} checks passed` : "";
  }

  function renderAnalyzeFeedback(result) {
    lastAnalyzeResult = result;
    const summaryEl = document.getElementById("analyze-summary");
    const summaryText = document.getElementById("analyze-summary-text");
    const checksEl = document.getElementById("analyze-checks");

    if (!summaryEl || !checksEl) return;

    summaryEl.classList.remove("pass", "fail", "warn");
    if (result.all_passed) summaryEl.classList.add("pass");
    else if (!result.syntax_ok) summaryEl.classList.add("fail");
    else summaryEl.classList.add("warn");

    if (summaryText) summaryText.textContent = result.summary || "";

    if (!result.syntax_ok && result.syntax_error) {
      const idx = result.current_step_index || currentStepIndex;
      analyzeFailCounts[idx] = (analyzeFailCounts[idx] || 0) + 1;
      checksEl.innerHTML = `<div class="check-item fail"><span class="check-icon">✗</span><span>${escapeHtml(result.syntax_error)}</span></div>`;
      renderStepsList();
      return;
    }

    const step = result.steps[result.current_step_index];
    if (!step) {
      checksEl.innerHTML = "";
      return;
    }

    if (!result.all_passed && !step.passed) {
      analyzeFailCounts[result.current_step_index] =
        (analyzeFailCounts[result.current_step_index] || 0) + 1;
    }

    const stepMeta = lessonSteps[result.current_step_index] || {};
    const extraHints = [];
    if (!step.passed && stepMeta.common_mistake) {
      extraHints.push(
        `<div class="check-item warn"><span class="check-icon">!</span><span>${escapeHtml(stepMeta.common_mistake)}</span></div>`
      );
    }

    checksEl.innerHTML =
      step.checks
        .map(
          (c) => `<div class="check-item ${c.passed ? "pass" : "fail"}">
          <span class="check-icon">${c.passed ? "✓" : "✗"}</span>
          <div><div>${escapeHtml(c.message)}</div>
          ${c.hint && !c.passed ? `<div class="check-hint">${escapeHtml(c.hint)}</div>` : ""}
          </div></div>`
        )
        .join("") + extraHints.join("");

    currentStepIndex = result.current_step_index;
    if (result.all_passed) {
      currentStepIndex = result.total_steps - 1;
      markExerciseDone(window.LESSON_ID, currentExerciseId);
    }

    localStorage.setItem(
      STEP_STORAGE_PREFIX + window.LESSON_ID + "-" + currentExerciseId,
      String(currentStepIndex)
    );
    scheduleProgressSync();

    renderStepsList();
    renderStepDots(result.passed_count, result.total_steps);
    updateExercisePickerUI();
  }

  async function analyzeCode(editor) {
    const summaryText = document.getElementById("analyze-summary-text");
    if (summaryText) summaryText.textContent = "Analyzing your code…";

    const res = await fetch("/api/analyze/" + window.LESSON_ID, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: editor.value, exercise_id: currentExerciseId }),
    });
    const data = await res.json();
    renderAnalyzeFeedback(data);
    return data;
  }

  function initWorkspace() {
    const editor = document.getElementById("code-editor");
    if (!editor || !window.WORKSPACE_FILE) return;

    const terminal = document.getElementById("terminal-body");
    const saveIndicator = document.getElementById("save-indicator");
    let saveTimeout;

    function setUnsaved() {
      if (saveIndicator) {
        saveIndicator.textContent = "Unsaved";
        saveIndicator.classList.add("unsaved");
      }
    }

    function setSaved() {
      if (saveIndicator) {
        saveIndicator.textContent = "Saved";
        saveIndicator.classList.remove("unsaved");
      }
    }

    async function saveFile() {
      const res = await fetch("/api/workspace/" + window.WORKSPACE_FILE, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: editor.value }),
      });
      if (res.ok) setSaved();
    }

    editor.addEventListener("input", () => {
      setUnsaved();
      clearTimeout(saveTimeout);
      saveTimeout = setTimeout(saveFile, 1500);
    });

    editor.addEventListener("keydown", (e) => {
      if (e.key === "Tab") {
        e.preventDefault();
        const start = editor.selectionStart;
        editor.value = editor.value.slice(0, start) + "    " + editor.value.slice(editor.selectionEnd);
        editor.selectionStart = editor.selectionEnd = start + 4;
        setUnsaved();
      }
      if (e.key === "Enter" && e.ctrlKey && window.HAS_INTERACTIVE) {
        e.preventDefault();
        document.getElementById("btn-analyze")?.click();
      }
    });

    document.getElementById("btn-save")?.addEventListener("click", saveFile);

    document.getElementById("btn-analyze")?.addEventListener("click", async () => {
      await saveFile();
      if (window.HAS_INTERACTIVE) await analyzeCode(editor);
    });

    document.getElementById("btn-run")?.addEventListener("click", async () => {
      await saveFile();
      terminal.innerHTML = '<span class="terminal-muted">Running…</span>';
      const res = await fetch("/api/run/" + window.WORKSPACE_FILE, { method: "POST" });
      const data = await res.json();
      if (data.error) {
        terminal.innerHTML = '<span class="terminal-error">' + escapeHtml(data.error) + "</span>";
        return;
      }
      let out = (data.stdout || "") + (data.stderr ? (data.stdout ? "\n" : "") + data.stderr : "");
      terminal.innerHTML = data.success
        ? '<span class="terminal-success">' + escapeHtml(out || "(no output)") + "</span>"
        : '<span class="terminal-error">' + escapeHtml(out || "Script failed") + "</span>";
    });

    document.getElementById("btn-verify")?.addEventListener("click", async () => {
      await saveFile();
      terminal.innerHTML = '<span class="terminal-muted">Verifying…</span>';
      const res = await fetch("/api/verify/" + window.LESSON_ID, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ exercise_id: currentExerciseId }),
      });
      const data = await res.json();
      if (data.success) {
        terminal.innerHTML = '<span class="terminal-success">' + escapeHtml(data.output) + "</span>";
        if (currentExerciseId) {
          markExerciseDone(window.LESSON_ID, currentExerciseId);
        } else {
          markComplete(window.LESSON_ID);
        }
      } else {
        terminal.innerHTML = '<span class="terminal-error">' + escapeHtml(data.output || data.error) + "</span>";
      }
    });

    document.getElementById("btn-clear-terminal")?.addEventListener("click", () => {
      terminal.innerHTML = '<span class="terminal-muted">Use ▶ Run to execute your script.</span>';
    });

    if (window.HAS_INTERACTIVE) loadExercises();
  }

  function initChecklists() {
    const lessonId = window.LESSON_ID;
    if (!lessonId) return;

    const boxes = [...document.querySelectorAll(".progress-checklist .setup-item, .setup-checklist .setup-item")];
    if (!boxes.length) return;

    const key = CHECKLIST_PREFIX + lessonId;
    const saved = readJson(key, {});

    boxes.forEach((cb) => {
      const id = cb.dataset.checkId || cb.value || cb.parentElement?.textContent?.trim() || "";
      cb.dataset.checkId = id;
      if (saved[id]) cb.checked = true;

      cb.addEventListener("change", () => {
        const state = {};
        boxes.forEach((box) => {
          state[box.dataset.checkId] = box.checked;
        });
        writeJson(key, state);

        if (boxes.every((box) => box.checked)) {
          markComplete(lessonId);
        }
      });
    });

    if (boxes.every((box) => box.checked)) {
      markComplete(lessonId);
    }
  }

  function initAutoCompleteOnContinue() {
    const readingTypes = new Set(["content", "cheatsheet", "lab", "setup", "reference"]);
    const shouldAuto =
      readingTypes.has(window.LESSON_TYPE) && !window.HAS_INTERACTIVE;
    const hasChecklist = !!document.querySelector(".progress-checklist");

    document.querySelectorAll("a.btn-primary, a.lesson-continue, #btn-next").forEach((link) => {
      link.addEventListener("click", (e) => {
        const required = (window.REQUIRED_PRIOR || []).filter(Boolean);
        if (required.length) {
          const missing = required.filter((id) => !isComplete(id));
          if (missing.length) {
            e.preventDefault();
            alert(
              "Mastery gate: finish these lessons first:\n- " +
                missing.join("\n- ")
            );
            return;
          }
        }
        if (shouldAuto && window.LESSON_ID) {
          markComplete(window.LESSON_ID);
        }
      });
    });

    // Reading lessons without a checklist: complete after dwell time
    if (
      shouldAuto &&
      !hasChecklist &&
      window.LESSON_ID &&
      !isComplete(window.LESSON_ID)
    ) {
      setTimeout(() => {
        if (document.visibilityState === "visible") {
          markComplete(window.LESSON_ID);
        }
      }, 15000);
    }
  }

  document.getElementById("btn-complete")?.addEventListener("click", (e) => {
    const lessonId = e.currentTarget.dataset.lessonId || window.LESSON_ID;
    if (isComplete(lessonId)) {
      unmarkComplete(lessonId);
    } else {
      markComplete(lessonId);
    }
  });

  document.getElementById("btn-check-apis")?.addEventListener("click", checkMockApis);

  document.getElementById("btn-reset-progress")?.addEventListener("click", async () => {
    if (!confirm("Reset all course progress on this server and browser?")) return;
    Object.keys(localStorage)
      .filter((k) => k.startsWith(SYNC_PREFIX))
      .forEach((k) => localStorage.removeItem(k));
    try {
      await fetch("/api/progress", { method: "DELETE" });
    } catch {
      // ignore
    }
    updateProgressUI();
    location.reload();
  });

  async function boot() {
    initSidebarToggle();
    await pullProgressFromServer();
    syncReady = true;

    if (window.LESSON_ID) {
      markStarted(window.LESSON_ID);
    }

    initChecklists();
    initAutoCompleteOnContinue();
    updateProgressUI();
    checkMockApis();
    setInterval(checkMockApis, 15000);
    initWorkspace();
  }

  boot();
})();
