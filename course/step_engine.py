"""Step-by-step validation engine for hands-on lessons."""

import ast
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from exercises_catalog import default_exercise, get_exercise
from lesson_steps import LESSON_STEPS


def get_steps(lesson_id, exercise_id=None):
    return get_steps_for_exercise(lesson_id, exercise_id)


def get_steps_for_exercise(lesson_id, exercise_id=None):
    from step_teaching import enrich_steps

    raw = []
    steps_key = lesson_id
    if exercise_id:
        ex = get_exercise(lesson_id, exercise_id)
        if ex:
            steps_key = ex["steps_key"]
            raw = LESSON_STEPS.get(steps_key, [])
    if not raw:
        default = default_exercise(lesson_id)
        if default:
            steps_key = default["steps_key"]
            raw = LESSON_STEPS.get(steps_key, [])
        else:
            steps_key = lesson_id
            raw = LESSON_STEPS.get(lesson_id, [])
    return enrich_steps(raw, steps_key)


def _contains(code, value, case_insensitive=False):
    if case_insensitive:
        return value.lower() in code.lower()
    return value in code


def _regex(code, pattern):
    return bool(re.search(pattern, code, re.MULTILINE | re.DOTALL))


def _has_import(code, module):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == module or alias.name.startswith(module + "."):
                    return True
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == module or node.module.startswith(module + "."):
                return True
    return False


def _has_function(code, name):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return True
    return False


def _no_hardcoded_secrets(code):
    bad = re.search(
        r'(API_KEY|SOURCE_API_KEY|DESTINATION_API_KEY|TOKEN)\s*=\s*["\'][a-zA-Z0-9\-_]{8,}',
        code,
    )
    if bad and "getenv" not in code:
        return False
    return True


def _syntax_ok(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax error line {e.lineno}: {e.msg}"


def _run_script(code, root_path):
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write(code)
        tmp = f.name

    try:
        result = subprocess.run(
            [sys.executable, tmp],
            capture_output=True,
            text=True,
            cwd=str(root_path),
            timeout=15,
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output
    except subprocess.TimeoutExpired:
        return False, "Script timed out (15s)"
    finally:
        Path(tmp).unlink(missing_ok=True)


def run_check(code, check, root_path):
    ctype = check["type"]
    msg = check.get("message", "Check failed")
    hint = check.get("hint", "")

    if ctype == "contains":
        ok = _contains(code, check["value"], check.get("case_insensitive", False))
    elif ctype == "regex":
        ok = _regex(code, check["pattern"])
    elif ctype == "not_contains":
        ok = not _contains(code, check["value"], check.get("case_insensitive", False))
    elif ctype == "has_import":
        ok = _has_import(code, check["module"])
    elif ctype == "has_function":
        ok = _has_function(code, check["name"])
    elif ctype == "no_hardcoded_secrets":
        ok = _no_hardcoded_secrets(code)
    elif ctype == "runs":
        ok, output = _run_script(code, root_path)
        if not ok:
            hint = hint or output[:200]
    elif ctype == "output_contains":
        ok, output = _run_script(code, root_path)
        if ok:
            ok = check["value"].lower() in output.lower()
        else:
            hint = hint or output[:200]
    else:
        ok = False
        hint = f"Unknown check type: {ctype}"

    return {"message": msg, "passed": ok, "hint": hint if not ok else ""}


def analyze_lesson(lesson_id, code, root_path, exercise_id=None):
    steps = get_steps_for_exercise(lesson_id, exercise_id)
    if not steps:
        return {"error": "No interactive steps for this exercise", "steps": []}

    syntax_ok, syntax_err = _syntax_ok(code)
    step_results = []
    first_incomplete = len(steps)

    for i, step in enumerate(steps):
        checks_out = []
        step_passed = True

        for check in step.get("checks", []):
            if not syntax_ok and check["type"] in ("runs", "output_contains"):
                checks_out.append(
                    {
                        "message": check.get("message", ""),
                        "passed": False,
                        "hint": syntax_err or "Fix syntax errors first",
                    }
                )
                step_passed = False
                continue

            result = run_check(code, check, root_path)
            checks_out.append(result)
            if not result["passed"]:
                step_passed = False

        step_results.append(
            {
                "id": step["id"],
                "title": step["title"],
                "instruction": step.get("instruction", ""),
                "passed": step_passed,
                "checks": checks_out,
            }
        )

        if not step_passed and first_incomplete == len(steps):
            first_incomplete = i

    current = step_results[min(first_incomplete, len(steps) - 1)] if step_results else None
    passed_count = sum(1 for s in step_results if s["passed"])

    if all(s["passed"] for s in step_results):
        summary = "All steps passed for this exercise! Try the next variant or Verify."
    elif current:
        failed = [c for c in current["checks"] if not c["passed"]]
        if failed:
            summary = f"Step {first_incomplete + 1}: {failed[0]['message']}"
            if failed[0].get("hint"):
                summary += f" — Hint: {failed[0]['hint']}"
        else:
            summary = f"Keep going — you're on step {first_incomplete + 1}."
    else:
        summary = "Start typing in the editor."

    return {
        "syntax_ok": syntax_ok,
        "syntax_error": syntax_err,
        "steps": step_results,
        "current_step_index": min(first_incomplete, max(len(steps) - 1, 0)),
        "passed_count": passed_count,
        "total_steps": len(steps),
        "all_passed": passed_count == len(steps),
        "summary": summary,
    }
