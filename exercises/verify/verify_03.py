"""Verify my-work/03_get_incidents.py — run after Guide 03."""

import importlib.util
import sys
from pathlib import Path

import requests

SCRIPT = Path(__file__).parent.parent / "my-work" / "03_get_incidents.py"

if not SCRIPT.exists():
    print("Create exercises/my-work/03_get_incidents.py — follow guides/03_get_filter_type_along.md")
    sys.exit(1)

# Check mock API is up
try:
    requests.get("http://127.0.0.1:5001/health", timeout=2)
except requests.RequestException:
    print("Start mock APIs first: python mock-apis/run_servers.py")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("user_03", SCRIPT)
mod = importlib.util.module_from_spec(spec)

# Capture module-level execution
try:
    spec.loader.exec_module(mod)
except Exception as e:
    print(f"Your script crashed when run:\n  {e}")
    sys.exit(1)

errors = []

for name in ("SOURCE_API_KEY", "SOURCE_API_URL"):
    if not hasattr(mod, name) or getattr(mod, name) is None:
        errors.append(f"Missing {name}")

if not hasattr(mod, "incidents") or not mod.incidents:
    errors.append("Script should define 'incidents' list from API response")
elif len(mod.incidents) < 5:
    errors.append(f"Expected 5+ incidents, got {len(mod.incidents)}")

if not hasattr(mod, "filtered") or not mod.filtered:
    errors.append("Script should define 'filtered' list")
else:
    for inc in mod.filtered:
        if inc["severity"] not in ("critical", "high"):
            errors.append(f"Filtered incident {inc['id']} has wrong severity")

if errors:
    print("Not yet — fix these:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"Guide 03 verified! Filtered {len(mod.filtered)} critical/high incidents.")
print("Move to guides/04_sync_type_along.md")
