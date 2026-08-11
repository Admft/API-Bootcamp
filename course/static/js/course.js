(function () {
  const STORAGE_KEY = "api-bootcamp-progress";
  const STEP_STORAGE_PREFIX = "api-bootcamp-step-";
  const EXERCISE_STORAGE_PREFIX = "api-bootcamp-exercise-";
  const EXERCISE_DONE_PREFIX = "api-bootcamp-exdone-";

  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    } catch {
      return [];
    }
  }

  function saveProgress(ids) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(ids));
    updateProgressUI();
  }

  function markComplete(lessonId) {
    const ids = getProgress();
    if (!ids.includes(lessonId)) {
      ids.push(lessonId);
      saveProgress(ids);
    }
  }

  function markExerciseDone(lessonId, exerciseId) {
    const key = EXERCISE_DONE_PREFIX + lessonId;
    let done = [];
    try {
      done = JSON.parse(localStorage.getItem(key) || "[]");
    } catch {
      done = [];
    }
    if (!done.includes(exerciseId)) {
      done.push(exerciseId);
      localStorage.setItem(key, JSON.stringify(done));
    }
    updateExercisePickerUI();
    const exercises = window.LESSON_EXERCISES || [];
    if (exercises.length && done.length >= exercises.length) {
      markComplete(lessonId);
    }
  }

  function getExerciseDone(lessonId) {
    try {
      return JSON.parse(localStorage.getItem(EXERCISE_DONE_PREFIX + lessonId) || "[]");
    } catch {
      return [];
    }
  }

  function updateProgressUI() {
    const ids = getProgress();
    const total = window.COURSE_TOTAL || 0;
    const pct = total ? Math.round((ids.length / total) * 100) : 0;
    const fill = document.getElementById("progress-fill");
    const pctEl = document.getElementById("progress-pct");
    const dashPct = document.getElementById("dash-progress");
    if (fill) fill.style.width = pct + "%";
    if (pctEl) pctEl.textContent = pct + "%";
    if (dashPct) dashPct.textContent = pct + "%";
    document.querySelectorAll("[data-check]").forEach((el) => {
      if (ids.includes(el.dataset.check)) el.classList.add("done");
    });
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

  function updateExercisePickerUI() {
    const picker = document.getElementById("exercise-picker");
    if (!picker || !allExercises.length) return;
    const done = getExerciseDone(window.LESSON_ID);
    picker.innerHTML = allExercises
      .map((ex) => {
        const isDone = done.includes(ex.id);
        const isActive = ex.id === currentExerciseId;
        return `<button type="button" class="exercise-tab ${isActive ? "active" : ""} ${isDone ? "done" : ""}" data-exercise-id="${ex.id}">
          <span class="ex-label">${ex.label}</span>
          <span class="ex-title">${escapeHtml(ex.title)}</span>
          ${isDone ? '<span class="ex-check">✓</span>' : ""}
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

    const res = await fetch("/api/workspace/" + exercise.workspace_file);
    const data = await res.json();
    if (editor) editor.value = data.content || "";
    const saveIndicator = document.getElementById("save-indicator");
    if (saveIndicator) {
      saveIndicator.textContent = "Saved";
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
    const summaryText = document.getElementById("analyze-summary-text");
    const checksEl = document.getElementById("analyze-checks");
    const summaryEl = document.getElementById("analyze-summary");
    if (summaryEl) summaryEl.classList.remove("pass", "fail", "warn");
    if (summaryText) summaryText.textContent = "Type code for this exercise, then hit Analyze.";
    if (checksEl) checksEl.innerHTML = "";
  }

  function renderStepsList() {
    const list = document.getElementById("steps-list");
    if (!list) return;

    list.innerHTML = lessonSteps
      .map((step, i) => {
        const status = getStepStatus(i);
        return `<div class="step-card ${status} ${i === currentStepIndex ? "active" : ""}" data-step="${i}">
          <div class="step-card-head">
            <span class="step-num">${status === "passed" ? "✓" : i + 1}</span>
            <strong>${escapeHtml(step.title)}</strong>
          </div>
          <p class="step-instruction">${escapeHtml(step.instruction)}</p>
        </div>`;
      })
      .join("");

    list.querySelectorAll(".step-card").forEach((card) => {
      card.addEventListener("click", () => {
        currentStepIndex = parseInt(card.dataset.step, 10);
        renderStepsList();
      });
    });
  }

  function getStepStatus(index) {
    if (lastAnalyzeResult && lastAnalyzeResult.steps[index]) {
      return lastAnalyzeResult.steps[index].passed ? "passed" : index === currentStepIndex ? "current" : "pending";
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

    if (counter) counter.textContent = `Step ${currentStepIndex + 1} of ${total}`;
    if (label) label.textContent = passed > 0 ? `${passed}/${total} passed` : "";
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
      checksEl.innerHTML = `<div class="check-item fail"><span class="check-icon">✗</span><span>${escapeHtml(result.syntax_error)}</span></div>`;
      return;
    }

    const step = result.steps[result.current_step_index];
    if (!step) {
      checksEl.innerHTML = "";
      return;
    }

    checksEl.innerHTML = step.checks
      .map(
        (c) => `<div class="check-item ${c.passed ? "pass" : "fail"}">
          <span class="check-icon">${c.passed ? "✓" : "✗"}</span>
          <div><div>${escapeHtml(c.message)}</div>
          ${c.hint && !c.passed ? `<div class="check-hint">${escapeHtml(c.hint)}</div>` : ""}
          </div></div>`
      )
      .join("");

    currentStepIndex = result.current_step_index;
    if (result.all_passed) {
      currentStepIndex = result.total_steps - 1;
      markExerciseDone(window.LESSON_ID, currentExerciseId);
    }

    localStorage.setItem(
      STEP_STORAGE_PREFIX + window.LESSON_ID + "-" + currentExerciseId,
      String(currentStepIndex)
    );

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
        markExerciseDone(window.LESSON_ID, currentExerciseId);
      } else {
        terminal.innerHTML = '<span class="terminal-error">' + escapeHtml(data.output || data.error) + "</span>";
      }
    });

    document.getElementById("btn-clear-terminal")?.addEventListener("click", () => {
      terminal.innerHTML = '<span class="terminal-muted">Use ▶ Run to execute your script.</span>';
    });

    if (window.HAS_INTERACTIVE) loadExercises();
  }

  document.getElementById("btn-complete")?.addEventListener("click", (e) => {
    markComplete(e.target.dataset.lessonId);
    e.target.textContent = "Completed ✓";
  });

  document.getElementById("btn-check-apis")?.addEventListener("click", checkMockApis);

  document.querySelectorAll(".setup-item").forEach((cb) => {
    cb.addEventListener("change", () => {
      const all = [...document.querySelectorAll(".setup-item")];
      if (all.every((c) => c.checked) && window.LESSON_ID === "setup") markComplete("setup");
    });
  });

  updateProgressUI();
  checkMockApis();
  setInterval(checkMockApis, 15000);
  initWorkspace();
})();
