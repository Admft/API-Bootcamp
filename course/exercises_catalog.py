"""Multiple exercises per lesson — slightly different scenarios, same skill."""

LESSON_EXERCISES = {
    "http-type-along": [
        {
            "id": "open-incidents",
            "label": "A",
            "title": "List open incidents",
            "scenario": "Water utility ops — GET all open incidents and print the count.",
            "workspace_file": "01a_open_incidents.py",
            "steps_key": "http-type-along:open-incidents",
        },
        {
            "id": "health-check",
            "label": "B",
            "title": "Health check (no auth)",
            "scenario": "Before syncing, verify the monitoring API is up — no token required.",
            "workspace_file": "01b_health_check.py",
            "steps_key": "http-type-along:health-check",
        },
        {
            "id": "single-incident",
            "label": "C",
            "title": "Fetch one incident by ID",
            "scenario": "Hospital grid alert — retrieve INC-38201 and print facility + message.",
            "workspace_file": "01c_single_incident.py",
            "steps_key": "http-type-along:single-incident",
        },
    ],
    "python-type-along": [
        {
            "id": "water-plant",
            "label": "A",
            "title": "Water plant incident",
            "scenario": "Map a pump pressure alert into a ticket payload.",
            "workspace_file": "02a_water_plant.py",
            "steps_key": "python-type-along:water-plant",
            "verify_script": "exercises/verify/verify_02.py",
        },
        {
            "id": "gas-pipeline",
            "label": "B",
            "title": "Gas pipeline alert",
            "scenario": "Different field names (eventId, locationName) — same transform pattern.",
            "workspace_file": "02b_gas_pipeline.py",
            "steps_key": "python-type-along:gas-pipeline",
        },
        {
            "id": "hospital-feed",
            "label": "C",
            "title": "Hospital feeder events",
            "scenario": "Filter a feed of events — only sync critical voltage sag alerts.",
            "workspace_file": "02c_hospital_feed.py",
            "steps_key": "python-type-along:hospital-feed",
        },
    ],
    "get-filter": [
        {
            "id": "critical-high",
            "label": "A",
            "title": "Filter critical + high",
            "scenario": "Standard ops report — open incidents, keep critical and high only.",
            "workspace_file": "03a_critical_high.py",
            "steps_key": "get-filter:critical-high",
            "verify_script": "exercises/verify/verify_03.py",
        },
        {
            "id": "api-filter",
            "label": "B",
            "title": "Let the API filter",
            "scenario": "Pass severity=critical in query params — fewer results, less Python filtering.",
            "workspace_file": "03b_api_filter.py",
            "steps_key": "get-filter:api-filter",
        },
        {
            "id": "facility-search",
            "label": "C",
            "title": "Filter by facility keyword",
            "scenario": "Find open incidents at any Water Treatment facility.",
            "workspace_file": "03c_facility_search.py",
            "steps_key": "get-filter:facility-search",
        },
    ],
    "sync-systems": [
        {
            "id": "sync-all-urgent",
            "label": "A",
            "title": "Sync critical + high",
            "scenario": "Default integration — urgent incidents become tickets.",
            "workspace_file": "04a_sync_urgent.py",
            "steps_key": "sync-systems:sync-all-urgent",
            "verify_script": "exercises/verify/verify_04.py",
        },
        {
            "id": "sync-critical-only",
            "label": "B",
            "title": "Critical only",
            "scenario": "Hospital SLA — only critical severity creates tickets.",
            "workspace_file": "04b_sync_critical.py",
            "steps_key": "sync-systems:sync-critical-only",
        },
        {
            "id": "sync-with-stats",
            "label": "C",
            "title": "Sync with counters",
            "scenario": "Same sync, but track created / skipped / failed counts.",
            "workspace_file": "04c_sync_stats.py",
            "steps_key": "sync-systems:sync-with-stats",
        },
    ],
    "reliability": [
        {
            "id": "full-reliability",
            "label": "A",
            "title": "Pagination + safe GET",
            "scenario": "Production pattern — paginate all records, safe single lookups.",
            "workspace_file": "05a_full_reliability.py",
            "steps_key": "reliability:full-reliability",
            "verify_script": "exercises/verify/verify_05.py",
        },
        {
            "id": "paginate-only",
            "label": "B",
            "title": "Pagination drill",
            "scenario": "Large dataset — fetch every incident using limit=2 pages.",
            "workspace_file": "05b_paginate.py",
            "steps_key": "reliability:paginate-only",
        },
        {
            "id": "errors-only",
            "label": "C",
            "title": "Error handling drill",
            "scenario": "Handle missing IDs and timeouts without crashing.",
            "workspace_file": "05c_errors.py",
            "steps_key": "reliability:errors-only",
        },
    ],
    "capstone-build": [
        {
            "id": "full-capstone",
            "label": "A",
            "title": "Full incident → ticket sync",
            "scenario": "Complete pipeline for critical + high open incidents.",
            "workspace_file": "06a_full_sync.py",
            "steps_key": "capstone-build:full-capstone",
            "verify_script": "exercises/verify/verify_06.py",
        },
        {
            "id": "critical-capstone",
            "label": "B",
            "title": "Critical-only capstone",
            "scenario": "Stricter SLA — only critical incidents, with sync statistics.",
            "workspace_file": "06b_critical_sync.py",
            "steps_key": "capstone-build:critical-capstone",
        },
    ],
}


def get_exercises(lesson_id):
    return LESSON_EXERCISES.get(lesson_id, [])


def get_exercise(lesson_id, exercise_id):
    for ex in get_exercises(lesson_id):
        if ex["id"] == exercise_id:
            return ex
    return None


def default_exercise(lesson_id):
    exercises = get_exercises(lesson_id)
    return exercises[0] if exercises else None


def lesson_has_exercises(lesson_id):
    return lesson_id in LESSON_EXERCISES
