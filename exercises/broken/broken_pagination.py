"""BROKEN — never checks has_more; only fetches page 1 logic wrong / infinite risk."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SOURCE_API_KEY")
BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

all_rows = []
page = 1
# BUG: no has_more check — either infinite loop or only one broken fetch
while page < 100:
    response = requests.get(
        f"{BASE}/v1/incidents",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"status": "open", "page": page, "limit": 2},
        timeout=30,
    )
    response.raise_for_status()
    body = response.json()
    all_rows.extend(body["data"])
    page += 1
    # missing: break when not body["pagination"]["has_more"]

print("TOTAL", len(all_rows))
