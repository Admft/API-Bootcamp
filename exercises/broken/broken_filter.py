"""BROKEN — filters medium instead of critical/high."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SOURCE_API_KEY")
BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

response = requests.get(
    f"{BASE}/v1/incidents",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"status": "open"},
    timeout=30,
)
response.raise_for_status()
incidents = response.json()["data"]

# BUG: wrong severities
filtered = [i for i in incidents if i["severity"] in {"medium", "low"}]
for i in filtered:
    print(i["id"], i["severity"])
print("COUNT", len(filtered))
