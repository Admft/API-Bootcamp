"""Solution for Exercise 05."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

HEADERS = {"Authorization": f"Bearer {SOURCE_API_KEY}"}


def fetch_all_incidents_paginated(limit=3):
    all_records = []
    page = 1

    while True:
        response = requests.get(
            f"{SOURCE_API_URL}/v1/incidents",
            headers=HEADERS,
            params={"page": page, "limit": limit},
            timeout=30,
        )
        response.raise_for_status()
        body = response.json()
        records = body["data"]

        if not records:
            break

        all_records.extend(records)

        if not body["pagination"]["has_more"]:
            break

        page += 1

    return all_records


def safe_get_incident(incident_id):
    try:
        response = requests.get(
            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",
            headers=HEADERS,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print(f"Timeout fetching {incident_id}")
        return None
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Incident {incident_id} not found")
        elif e.response.status_code == 401:
            print("Authentication failed — check SOURCE_API_KEY")
        else:
            print(f"HTTP error {e.response.status_code}: {e}")
        return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


if __name__ == "__main__":
    all_incidents = fetch_all_incidents_paginated(limit=3)
    print(f"Paginated fetch: {len(all_incidents)} total incidents")

    found = safe_get_incident("INC-38192")
    print(f"Found: {found['id'] if found else None}")

    missing = safe_get_incident("INC-99999")
    print(f"Missing: {missing}")
