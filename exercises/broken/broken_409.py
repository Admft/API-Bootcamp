"""BROKEN — ignores 409 Conflict on duplicate POST."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
DEST_KEY = os.getenv("DESTINATION_API_KEY")
DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")

payload = {
    "external_id": "INC-DEBUG-409",
    "site": "Debug Yard",
    "description": "Debug 409 drill",
    "priority": 1,
}

# First create should work; second should be handled as SKIP — currently crashes
for attempt in range(2):
    response = requests.post(
        f"{DEST}/v1/tickets",
        headers={"Authorization": f"Bearer {DEST_KEY}"},
        json=payload,
        timeout=30,
    )
    response.raise_for_status()  # BUG: blows up on 409
    print("CREATED", response.json()["id"])
