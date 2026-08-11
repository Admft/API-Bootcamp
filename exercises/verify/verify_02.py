"""Verify my-work/02_basics.py — run after Guide 02."""

import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "my-work" / "02_basics.py"

if not SCRIPT.exists():
    print("Create exercises/my-work/02_basics.py first — follow guides/02_python_type_along.md")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("user_02", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

errors = []

if not hasattr(mod, "incident") or mod.incident is None:
    errors.append("Missing 'incident' dictionary")
elif "facility" not in mod.incident:
    errors.append("incident needs 'facility' key")

if not hasattr(mod, "SYNC_SEVERITIES") or len(mod.SYNC_SEVERITIES) < 2:
    errors.append("Define SYNC_SEVERITIES with at least critical and high")

if not hasattr(mod, "severity_to_priority"):
    errors.append("Missing severity_to_priority function")
elif mod.severity_to_priority("critical") != 1:
    errors.append("severity_to_priority('critical') should return 1")

if not hasattr(mod, "transform_incident"):
    errors.append("Missing transform_incident function")
else:
    sample = {"id": "X", "facility": "F", "severity": "high", "message": "m"}
    t = mod.transform_incident(sample)
    for key in ("external_id", "site", "description", "priority"):
        if key not in t:
            errors.append(f"transform_incident missing '{key}'")

if errors:
    print("Not yet — fix these:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Guide 02 verified! Move to guides/03_get_filter_type_along.md")
