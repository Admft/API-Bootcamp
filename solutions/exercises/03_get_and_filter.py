"""Solution for Exercise 03."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

headers = {"Authorization": f"Bearer {SOURCE_API_KEY}"}

response = requests.get(
    f"{SOURCE_API_URL}/v1/incidents",
    headers=headers,
    params={"status": "open"},
    timeout=30,
)
response.raise_for_status()

incidents = response.json()["data"]

SYNC_SEVERITIES = {"critical", "high"}
filtered = [i for i in incidents if i["severity"] in SYNC_SEVERITIES]

for incident in filtered:
    print(f"{incident['id']} | {incident['severity']} | {incident['facility']}")

if __name__ == "__main__":
    print(f"\nFound {len(filtered)} critical/high open incidents.")
