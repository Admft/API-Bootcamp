"""Verify my-work/04_sync.py — run after Guide 04."""

import importlib.util
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SCRIPT = Path(__file__).parent.parent / "my-work" / "04_sync.py"

if not SCRIPT.exists():
    print("Create exercises/my-work/04_sync.py — follow guides/04_sync_type_along.md")
    sys.exit(1)

try:
    requests.get("http://127.0.0.1:5001/health", timeout=2)
except requests.RequestException:
    print("Start mock APIs first: python mock-apis/run_servers.py")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("user_04", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

errors = []

for name in ("transform_incident", "fetch_open_incidents", "create_ticket", "main"):
    if not hasattr(mod, name):
        errors.append(f"Missing function: {name}()")

if errors:
    print("Not yet — fix these:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

# Functional test
sample = {
    "id": "VERIFY-TEST-001",
    "facility": "Test",
    "message": "Verify run",
    "severity": "critical",
}
ticket = mod.transform_incident(sample)
if ticket.get("external_id") != "VERIFY-TEST-001":
    errors.append("transform_incident not mapping external_id correctly")

if errors:
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("Guide 04 verified! Functions look good.")
print("If main() runs and creates/skips tickets, you're solid.")
print("Move to guides/05_reliability_type_along.md")
