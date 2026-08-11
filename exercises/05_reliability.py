"""
Exercise 05 — Reliability Patterns

Prerequisites: Mock APIs running, .env configured

Run:  python exercises/05_reliability.py

Goal: Pagination, error handling, idempotency awareness.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")


def fetch_all_incidents_paginated(limit=3):
    """
    Fetch ALL incidents using pagination.

    The mock API supports: page, limit, and returns pagination.has_more
    Use limit=3 to force multiple pages with the sample data.
    """
    # TODO: implement pagination loop
    pass


def safe_get_incident(incident_id):
    """
    GET a single incident with full error handling.
    Return the incident dict on success, None on failure.
    Handle: timeout, 404, 401, other HTTP errors.
    """
    # TODO: implement with try/except
    pass


if __name__ == "__main__":
    all_incidents = fetch_all_incidents_paginated(limit=3)
    assert all_incidents is not None, "Implement fetch_all_incidents_paginated"
    assert len(all_incidents) >= 10, f"Expected 10+ incidents, got {len(all_incidents)}"
    print(f"Paginated fetch: {len(all_incidents)} total incidents")

    found = safe_get_incident("INC-38192")
    assert found is not None, "Should find INC-38192"

    missing = safe_get_incident("INC-99999")
    assert missing is None, "Should return None for missing incident"

    print("Exercise 05 complete!")
