"""Verify my-work/05_reliability.py — run after Guide 05."""

import importlib.util
import sys
from pathlib import Path

import requests

SCRIPT = Path(__file__).parent.parent / "my-work" / "05_reliability.py"

if not SCRIPT.exists():
    print("Create exercises/my-work/05_reliability.py — follow guides/05_reliability_type_along.md")
    sys.exit(1)

try:
    requests.get("http://127.0.0.1:5001/health", timeout=2)
except requests.RequestException:
    print("Start mock APIs first: python mock-apis/run_servers.py")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("user_05", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

errors = []

if not hasattr(mod, "fetch_all_incidents"):
    errors.append("Missing fetch_all_incidents()")
else:
    result = mod.fetch_all_incidents(limit=3)
    if not result or len(result) < 10:
        errors.append(f"Pagination should return 10+ incidents, got {len(result) if result else 0}")

if not hasattr(mod, "safe_get_incident"):
    errors.append("Missing safe_get_incident()")
else:
    found = mod.safe_get_incident("INC-38192")
    if not found or found.get("id") != "INC-38192":
        errors.append("safe_get_incident('INC-38192') should return the incident")

    missing = mod.safe_get_incident("INC-99999")
    if missing is not None:
        errors.append("safe_get_incident('INC-99999') should return None")

if errors:
    print("Not yet — fix these:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Guide 05 verified! Pagination and error handling work.")
print("Move to guides/06_capstone_type_along.md")
