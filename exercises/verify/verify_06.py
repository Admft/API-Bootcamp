"""Verify my-work/06_sync_incidents.py — run after Guide 06."""

import importlib.util
import sys
from pathlib import Path

import requests

SCRIPT = Path(__file__).parent.parent / "my-work" / "06_sync_incidents.py"

if not SCRIPT.exists():
    print("Create exercises/my-work/06_sync_incidents.py — follow guides/06_capstone_type_along.md")
    sys.exit(1)

try:
    requests.get("http://127.0.0.1:5001/health", timeout=2)
except requests.RequestException:
    print("Start mock APIs first: python mock-apis/run_servers.py")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("user_06", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

errors = []

required_funcs = (
    "load_config",
    "transform_incident",
    "fetch_all_open_incidents",
    "create_ticket",
    "sync",
)
for name in required_funcs:
    if not hasattr(mod, name):
        errors.append(f"Missing function: {name}()")

if hasattr(mod, "load_config"):
    try:
        cfg = mod.load_config()
        for key in ("source_key", "dest_key", "source_url", "dest_url"):
            if key not in cfg:
                errors.append(f"load_config() missing '{key}'")
    except ValueError as e:
        errors.append(str(e))

readme = Path(__file__).parent.parent / "my-work" / "06_README.md"
if not readme.exists():
    errors.append("Create my-work/06_README.md documenting your script (Guide 06 Step 8)")

if errors:
    print("Not yet — fix these:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Guide 06 verified! Capstone structure complete.")
print("Run your script, then try SELF_TEST.md from a blank file.")
