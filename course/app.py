"""
API Integration Bootcamp — Course Platform

Run:  python course/app.py
Open: http://127.0.0.1:8080
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# Allow running as: python course/app.py
sys.path.insert(0, str(Path(__file__).resolve().parent))

import markdown
import requests
from flask import Flask, jsonify, render_template, request

from course_data import (
    MODULES,
    MY_WORK,
    ROOT,
    get_lesson,
    next_prev,
    total_lessons,
)
from exercises_catalog import (
    default_exercise,
    get_exercise,
    get_exercises,
    lesson_has_exercises,
)
from step_engine import analyze_lesson, get_steps

app = Flask(__name__)
app.config["ROOT"] = ROOT

MD_EXTENSIONS = ["fenced_code", "tables", "nl2br", "sane_lists"]
PROGRESS_FILE = ROOT / ".data" / "progress.json"


def read_progress_file():
    if not PROGRESS_FILE.exists():
        return {}
    try:
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def write_progress_file(data):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def render_md(text):
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def read_file(relative_path):
    path = ROOT / relative_path
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def safe_workspace_path(filename):
    if not filename or ".." in filename or "/" in filename or "\\" in filename:
        return None
    if not re.match(r"^[\w.\-]+$", filename):
        return None
    return MY_WORK / filename


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        modules=MODULES,
        total_lessons=total_lessons(),
    )


@app.route("/lesson/<lesson_id>")
def lesson_page(lesson_id):
    lesson = get_lesson(lesson_id)
    if not lesson:
        return "Lesson not found", 404

    prev_lesson, next_lesson = next_prev(lesson_id)
    content_html = None
    guide_html = None

    if lesson.get("source"):
        raw = read_file(lesson["source"])
        if raw:
            content_html = render_md(raw)

    if lesson.get("guide"):
        raw = read_file(lesson["guide"])
        if raw:
            guide_html = render_md(raw)

    workspace_file = lesson.get("workspace_file")
    workspace_content = ""
    if lesson_has_exercises(lesson_id):
        default_ex = default_exercise(lesson_id)
        if default_ex:
            workspace_file = default_ex["workspace_file"]
    if workspace_file:
        path = safe_workspace_path(workspace_file)
        if path and path.exists():
            workspace_content = path.read_text(encoding="utf-8")

    return render_template(
        "lesson.html",
        modules=MODULES,
        lesson=lesson,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson,
        content_html=content_html,
        guide_html=guide_html,
        workspace_file=workspace_file,
        workspace_content=workspace_content,
        total_lessons=total_lessons(),
        has_interactive_steps=lesson_has_exercises(lesson_id),
        exercises=get_exercises(lesson_id),
    )


@app.route("/api/mock-status")
def mock_status():
    status = {"source": False, "destination": False}
    try:
        r = requests.get("http://127.0.0.1:5001/health", timeout=2)
        status["source"] = r.status_code == 200
    except requests.RequestException:
        pass
    try:
        r = requests.get("http://127.0.0.1:5002/health", timeout=2)
        status["destination"] = r.status_code == 200
    except requests.RequestException:
        pass
    status["online"] = status["source"] and status["destination"]
    return jsonify(status)


@app.route("/api/progress", methods=["GET", "POST", "DELETE"])
def progress_sync():
    """Single shared progress blob — no login. Syncs across any browser hitting this server."""
    if request.method == "GET":
        return jsonify({"progress": read_progress_file()})

    if request.method == "DELETE":
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
        return jsonify({"ok": True, "cleared": True})

    data = request.get_json(silent=True) or {}
    progress = data.get("progress")
    if not isinstance(progress, dict):
        return jsonify({"error": "Expected { progress: { ... } }"}), 400

    # Only keep bootcamp keys
    cleaned = {
        key: value
        for key, value in progress.items()
        if isinstance(key, str) and key.startswith("api-bootcamp-")
    }
    write_progress_file(cleaned)
    return jsonify({"ok": True, "keys": len(cleaned)})


@app.route("/api/workspace/<filename>", methods=["GET", "POST"])
def workspace(filename):
    path = safe_workspace_path(filename)
    if not path:
        return jsonify({"error": "Invalid filename"}), 400

    MY_WORK.mkdir(parents=True, exist_ok=True)

    if request.method == "GET":
        starter = request.args.get("starter")
        if path.exists():
            return jsonify({"content": path.read_text(encoding="utf-8"), "exists": True})
        if starter:
            # Allow only files under exercises/broken/
            starter_name = Path(starter).name
            starter_path = ROOT / "exercises" / "broken" / starter_name
            if starter_path.exists() and starter_path.is_file():
                content = starter_path.read_text(encoding="utf-8")
                path.write_text(content, encoding="utf-8")
                return jsonify({"content": content, "exists": True, "seeded_from": starter_name})
        return jsonify({"content": "", "exists": False})

    data = request.get_json(silent=True) or {}
    content = data.get("content", "")
    path.write_text(content, encoding="utf-8")
    return jsonify({"saved": True, "path": str(path.relative_to(ROOT))})


@app.route("/api/run/<filename>", methods=["POST"])
def run_script(filename):
    path = safe_workspace_path(filename)
    if not path or not path.exists():
        return jsonify({"error": "File not found — save your script first"}), 404
    if not filename.endswith(".py"):
        return jsonify({"error": "Only .py files can be run"}), 400

    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
        timeout=30,
    )
    return jsonify(
        {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "success": result.returncode == 0,
        }
    )


@app.route("/api/exercises/<lesson_id>")
def exercises_api(lesson_id):
    exercises = get_exercises(lesson_id)
    return jsonify(
        {
            "exercises": [
                {
                    "id": ex["id"],
                    "label": ex["label"],
                    "title": ex["title"],
                    "scenario": ex["scenario"],
                    "workspace_file": ex["workspace_file"],
                    "has_verify": bool(ex.get("verify_script")),
                    "starter_file": ex.get("starter_file"),
                    "hide_examples": bool(ex.get("hide_examples") or str(lesson_id).startswith("exam-")),
                }
                for ex in exercises
            ]
        }
    )


@app.route("/api/steps/<lesson_id>")
def lesson_steps_api(lesson_id):
    exercise_id = request.args.get("exercise")
    steps = get_steps(lesson_id, exercise_id)
    if not steps:
        return jsonify({"steps": [], "interactive": False})
    return jsonify(
        {
            "interactive": True,
            "hide_examples": bool(
                (get_exercise(lesson_id, exercise_id) or {}).get("hide_examples")
                or str(lesson_id).startswith("exam-")
            ),
            "steps": [
                {
                    "id": s["id"],
                    "title": s["title"],
                    "instruction": s.get("instruction", ""),
                    "example": s.get("example", ""),
                    "context": s.get("context", ""),
                    "why": s.get("why", ""),
                    "common_mistake": s.get("common_mistake", ""),
                    "reveal_after_fails": s.get("reveal_after_fails", 2),
                    "annotations": s.get("annotations", []),
                }
                for s in steps
            ],
        }
    )


@app.route("/api/analyze/<lesson_id>", methods=["POST"])
def analyze_code(lesson_id):
    data = request.get_json(silent=True) or {}
    code = data.get("code", "")
    exercise_id = data.get("exercise_id")

    if not lesson_has_exercises(lesson_id):
        return jsonify({"error": "No analyze steps for this lesson"}), 404

    steps = get_steps(lesson_id, exercise_id)
    if not code.strip():
        return jsonify(
            {
                "syntax_ok": True,
                "steps": [],
                "summary": "Start typing in the editor — then hit Analyze.",
                "current_step_index": 0,
                "passed_count": 0,
                "total_steps": len(steps),
                "all_passed": False,
            }
        )

    result = analyze_lesson(lesson_id, code, ROOT, exercise_id)
    return jsonify(result)


@app.route("/api/verify/<lesson_id>", methods=["POST"])
def verify_lesson(lesson_id):
    data = request.get_json(silent=True) or {}
    exercise_id = data.get("exercise_id")

    verify_script = None
    if exercise_id:
        ex = get_exercise(lesson_id, exercise_id)
        if ex and ex.get("verify_script"):
            verify_script = ex["verify_script"]

    if not verify_script:
        lesson = get_lesson(lesson_id)
        if lesson and lesson.get("verify_script"):
            verify_script = lesson["verify_script"]

    if not verify_script:
        return jsonify({"error": "No verifier for this exercise — use Analyze instead"}), 404

    script_path = ROOT / verify_script
    if not script_path.exists():
        return jsonify({"error": "Verifier script missing"}), 500

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
        timeout=30,
    )
    output = (result.stdout + result.stderr).strip()
    return jsonify(
        {
            "success": result.returncode == 0,
            "output": output,
        }
    )


@app.route("/api/reference/<path:ref_path>")
def reference_file(ref_path):
    allowed = {
        "capstone/sync_incidents.py": ROOT / "capstone" / "sync_incidents.py",
        "capstone/README.md": ROOT / "capstone" / "README.md",
    }
    if ref_path not in allowed:
        return jsonify({"error": "Not found"}), 404
    path = allowed[ref_path]
    return jsonify({"content": path.read_text(encoding="utf-8")})


if __name__ == "__main__":
    print("\n  API Integration Bootcamp")
    print("  http://127.0.0.1:8080\n")
    print("  Keep mock APIs running: python mock-apis/run_servers.py\n")
    app.run(host="127.0.0.1", port=8080, debug=False)
