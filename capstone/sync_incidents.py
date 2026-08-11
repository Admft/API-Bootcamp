"""
Capstone — Critical Incident → Ticket Integration

Production-style script: fetch, filter, transform, sync with logging,
error handling, pagination, and duplicate prevention.

Prerequisites:
  python mock-apis/run_servers.py   (separate terminal)
  .env configured

Run:
  python capstone/sync_incidents.py
  python capstone/sync_incidents.py --dry-run
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SYNC_SEVERITIES = {"critical", "high"}
PRIORITY_MAP = {"critical": 1, "high": 2, "medium": 3, "low": 4}
STATE_FILE = Path(__file__).parent / "processed_ids.json"


def load_config():
    source_key = os.getenv("SOURCE_API_KEY")
    dest_key = os.getenv("DESTINATION_API_KEY")
    source_url = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
    dest_url = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")

    missing = []
    if not source_key:
        missing.append("SOURCE_API_KEY")
    if not dest_key:
        missing.append("DESTINATION_API_KEY")
    if missing:
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")

    return {
        "source_key": source_key,
        "dest_key": dest_key,
        "source_url": source_url.rstrip("/"),
        "dest_url": dest_url.rstrip("/"),
    }


def load_processed_ids():
    if STATE_FILE.exists():
        return set(json.loads(STATE_FILE.read_text()))
    return set()


def save_processed_ids(ids):
    STATE_FILE.write_text(json.dumps(sorted(ids), indent=2))


def transform_incident(incident):
    return {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": PRIORITY_MAP[incident["severity"]],
    }


def fetch_all_open_incidents(config):
    """Fetch all open incidents with pagination."""
    all_incidents = []
    page = 1
    headers = {"Authorization": f"Bearer {config['source_key']}"}

    while True:
        response = requests.get(
            f"{config['source_url']}/v1/incidents",
            headers=headers,
            params={"status": "open", "page": page, "limit": 100},
            timeout=30,
        )
        response.raise_for_status()
        body = response.json()
        records = body["data"]

        if not records:
            break

        all_incidents.extend(records)

        if not body["pagination"]["has_more"]:
            break
        page += 1

    return all_incidents


def create_ticket(config, payload, dry_run=False):
    if dry_run:
        log.info(f"[DRY RUN] Would create ticket: {payload['external_id']}")
        return {"id": "DRY-RUN", **payload}

    response = requests.post(
        f"{config['dest_url']}/v1/tickets",
        headers={"Authorization": f"Bearer {config['dest_key']}"},
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def sync(dry_run=False):
    config = load_config()
    processed = load_processed_ids()

    log.info("Fetching open incidents from monitoring API...")
    incidents = fetch_all_open_incidents(config)
    log.info(f"Retrieved {len(incidents)} open incidents")

    to_sync = [i for i in incidents if i["severity"] in SYNC_SEVERITIES]
    log.info(f"Filtered to {len(to_sync)} critical/high incidents")

    stats = {"created": 0, "skipped_dup": 0, "skipped_state": 0, "failed": 0}

    for incident in to_sync:
        incident_id = incident["id"]

        if incident_id in processed:
            log.debug(f"Skipping {incident_id} — already processed this session")
            stats["skipped_state"] += 1
            continue

        ticket = transform_incident(incident)

        try:
            result = create_ticket(config, ticket, dry_run=dry_run)
            log.info(f"Created {result['id']} for {incident_id} ({incident['facility']})")
            processed.add(incident_id)
            stats["created"] += 1
        except requests.HTTPError as e:
            if e.response.status_code == 409:
                log.warning(f"Skipped {incident_id} — ticket already exists in destination")
                processed.add(incident_id)
                stats["skipped_dup"] += 1
            else:
                log.error(f"Failed {incident_id}: HTTP {e.response.status_code}")
                stats["failed"] += 1
        except requests.RequestException as e:
            log.error(f"Failed {incident_id}: {e}")
            stats["failed"] += 1

    if not dry_run:
        save_processed_ids(processed)

    log.info(
        f"Sync complete — created: {stats['created']}, "
        f"skipped (state): {stats['skipped_state']}, "
        f"skipped (409): {stats['skipped_dup']}, "
        f"failed: {stats['failed']}"
    )
    return stats


def main():
    parser = argparse.ArgumentParser(description="Sync critical incidents to ticketing system")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating tickets")
    args = parser.parse_args()

    try:
        sync(dry_run=args.dry_run)
    except ValueError as e:
        log.error(str(e))
        sys.exit(1)
    except requests.RequestException as e:
        log.error(f"API connection failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
