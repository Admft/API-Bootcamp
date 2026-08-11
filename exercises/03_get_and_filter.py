"""
Exercise 03 — Retrieve and Filter (API Script #1)

Prerequisites:
  - Mock APIs running: python mock-apis/run_servers.py
  - .env configured (run setup.ps1)

Run:  python exercises/03_get_and_filter.py

Goal: GET open incidents, filter critical/high, print summary.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

# TODO 1: Set up headers with Bearer authentication
headers = None  # replace None

# TODO 2: GET /v1/incidents with params status=open
#         Use timeout=30 and raise_for_status()
response = None  # replace None

# TODO 3: Parse JSON and extract the "data" list
incidents = []  # replace with parsed data

# TODO 4: Filter to only critical and high severity
SYNC_SEVERITIES = {"critical", "high"}
filtered = []  # replace with filtered list

# TODO 5: Print each filtered incident as:  INC-123 | critical | Plant Name
# for incident in filtered:
#     print(...)


if __name__ == "__main__":
    assert headers is not None, "TODO 1: set up auth headers"
    assert response is not None, "TODO 2: make the GET request"
    assert len(incidents) > 0, "TODO 3: parse incidents from response"
    assert len(filtered) > 0, "TODO 4: filter incidents"
    print(f"\nFound {len(filtered)} critical/high open incidents.")
    print("Exercise 03 complete!")
