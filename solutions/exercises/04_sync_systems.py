"""Solution for Exercise 04."""

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
    priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}
    return {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": priority_map[incident["severity"]],
    }


def fetch_open_incidents():
    response = requests.get(
        f"{SOURCE_API_URL}/v1/incidents",
        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},
        params={"status": "open"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["data"]


def create_ticket(ticket_payload):
    response = requests.post(
        f"{DESTINATION_API_URL}/v1/tickets",
        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},
        json=ticket_payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def main():
    incidents = fetch_open_incidents()
    created = 0

    for incident in incidents:
        if incident["severity"] not in SYNC_SEVERITIES:
            continue

        ticket = transform_incident(incident)
        try:
            result = create_ticket(ticket)
            print(f"Created {result['id']} for {incident['id']}")
            created += 1
        except requests.HTTPError as e:
            if e.response.status_code == 409:
                print(f"Skipped {incident['id']} — already exists")
            else:
                print(f"Failed {incident['id']}: {e}")

    print(f"\nSynced {created} tickets.")


if __name__ == "__main__":
    main()
