"""BROKEN capstone sketch — missing dotenv, wrong dest key name, no 409 handling."""
import os
import requests

# BUG: forgot load_dotenv()
SOURCE_KEY = os.getenv("SOURCE_API_KEY")
DEST_KEY = os.getenv("DEST_API_KEY")  # BUG: wrong env name
SOURCE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")

PRIORITY = {"critical": 1, "high": 2, "medium": 3, "low": 4}

response = requests.get(
    f"{SOURCE}/v1/incidents",
    headers={"Authorization": f"Bearer {SOURCE_KEY}"},
    params={"status": "open"},
    timeout=30,
)
response.raise_for_status()
incidents = [i for i in response.json()["data"] if i["severity"] in {"critical", "high"}]

for incident in incidents:
    ticket = {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": PRIORITY[incident["severity"]],
    }
    result = requests.post(
        f"{DEST}/v1/tickets",
        headers={"Authorization": f"Bearer {DEST_KEY}"},
        json=ticket,
        timeout=30,
    )
    result.raise_for_status()  # BUG: no 409 handling
    print("OK", result.json()["id"])
