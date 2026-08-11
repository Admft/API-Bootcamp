"""
Exercise 04 — System A → System B (API Script #2)

Prerequisites:
  - Mock APIs running
  - .env configured

Run:  python exercises/04_sync_systems.py

Goal: Fetch incidents from source, transform, POST tickets to destination.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")

SYNC_SEVERITIES = {"critical", "high"}


def transform_incident(incident):
    """Map source incident schema → destination ticket schema."""
    priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}
    # TODO: return the transformed dictionary
    pass


def fetch_open_incidents():
    """GET open incidents from source API."""
    # TODO: implement
    pass


def create_ticket(ticket_payload):
    """POST ticket to destination API. Return response JSON."""
    # TODO: implement
    pass


def main():
    incidents = fetch_open_incidents()

    # TODO: loop incidents, filter by SYNC_SEVERITIES, transform, POST
    # Print success/failure for each

    pass


if __name__ == "__main__":
    main()
    print("Exercise 04 complete!")
