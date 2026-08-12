"""Multiple exercises per lesson — slightly different scenarios, same skill."""

LESSON_EXERCISES = {
    "practice-methods": [
        {
            "id": "drill",
            "label": "A",
            "title": "Type method meanings",
            "scenario": "Write print() lines so you can say what GET/POST/PATCH/PUT/DELETE do without looking.",
            "workspace_file": "drill_methods.py",
            "steps_key": "practice-methods:drill",
        },
    ],
    "practice-status": [
        {
            "id": "drill",
            "label": "A",
            "title": "Type status code meanings",
            "scenario": "Write print() lines for 200, 201, 401, 404, 409, 429, 500 and what you'd do about each.",
            "workspace_file": "drill_status.py",
            "steps_key": "practice-status:drill",
        },
    ],
    "baby-print": [
        {
            "id": "main",
            "label": "A",
            "title": "Your first print()",
            "scenario": "Type one print() line that greets the bootcamp.",
            "workspace_file": "baby_01_print.py",
            "steps_key": "baby-print:main",
        },
    ],
    "baby-import": [
        {
            "id": "main",
            "label": "A",
            "title": "Import requests",
            "scenario": "Import the requests library and confirm it loaded.",
            "workspace_file": "baby_02_import.py",
            "steps_key": "baby-import:main",
        },
    ],
    "baby-health": [
        {
            "id": "main",
            "label": "A",
            "title": "GET /health",
            "scenario": "Call the monitoring health endpoint — no auth required.",
            "workspace_file": "baby_03_health.py",
            "steps_key": "baby-health:main",
        },
    ],
    "baby-json": [
        {
            "id": "main",
            "label": "A",
            "title": "Parse health JSON",
            "scenario": "Parse response.json() and print the service name.",
            "workspace_file": "baby_04_json.py",
            "steps_key": "baby-json:main",
        },
    ],
    "baby-variables": [
        {
            "id": "main",
            "label": "A",
            "title": "Store the base URL",
            "scenario": "Put the base URL in a variable and call /health with an f-string.",
            "workspace_file": "baby_05_url_var.py",
            "steps_key": "baby-variables:main",
        },
    ],
    "baby-auth": [
        {
            "id": "main",
            "label": "A",
            "title": "Bearer auth (hardcoded once)",
            "scenario": "GET /v1/incidents with a hardcoded Bearer key — OK for this lesson only.",
            "workspace_file": "baby_06_auth.py",
            "steps_key": "baby-auth:main",
        },
    ],
    "baby-getenv": [
        {
            "id": "main",
            "label": "A",
            "title": "Load key with os.getenv",
            "scenario": "Replace the hardcoded key with os.getenv('SOURCE_API_KEY').",
            "workspace_file": "baby_07_getenv.py",
            "steps_key": "baby-getenv:main",
        },
    ],
    "baby-dotenv": [
        {
            "id": "main",
            "label": "A",
            "title": "load_dotenv()",
            "scenario": "Call load_dotenv() so getenv finds SOURCE_API_KEY and SOURCE_API_URL.",
            "workspace_file": "baby_08_dotenv.py",
            "steps_key": "baby-dotenv:main",
        },
    ],
    "baby-params": [
        {
            "id": "main",
            "label": "A",
            "title": "Query params",
            "scenario": "Pass params={'status': 'open'} and print how many came back.",
            "workspace_file": "baby_09_params.py",
            "steps_key": "baby-params:main",
        },
    ],
    "baby-raise": [
        {
            "id": "main",
            "label": "A",
            "title": "raise_for_status + count",
            "scenario": "Fail loudly on HTTP errors; print len(data['data']).",
            "workspace_file": "baby_10_raise.py",
            "steps_key": "baby-raise:main",
        },
    ],
    "baby-loop": [
        {
            "id": "main",
            "label": "A",
            "title": "Loop and print fields",
            "scenario": "for incident in data['data']: print id, severity, facility.",
            "workspace_file": "baby_11_loop.py",
            "steps_key": "baby-loop:main",
        },
    ],
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
    # ── New piece-by-piece drills ──
    "py-vars": [
        {
            "id": "main",
            "label": "A",
            "title": "Create name, count, active",
            "scenario": "Type three variables (string, number, boolean) and print each.",
            "workspace_file": "py_01_vars.py",
            "steps_key": "py-vars:main",
        },
    ],
    "py-dict": [
        {
            "id": "main",
            "label": "A",
            "title": "Build an incident dict",
            "scenario": "Create an incident dictionary with id, severity, facility, message — then print fields.",
            "workspace_file": "py_02_dict.py",
            "steps_key": "py-dict:main",
        },
    ],
    "py-list-loop": [
        {
            "id": "main",
            "label": "A",
            "title": "List of 3 + for loop",
            "scenario": "Make a list of three incident dicts and print each id in a for loop.",
            "workspace_file": "py_03_list_loop.py",
            "steps_key": "py-list-loop:main",
        },
    ],
    "py-if": [
        {
            "id": "main",
            "label": "A",
            "title": "Filter critical + high",
            "scenario": "Use SYNC_SEVERITIES and if-in to print only critical and high incidents.",
            "workspace_file": "py_04_if.py",
            "steps_key": "py-if:main",
        },
    ],
    "py-function": [
        {
            "id": "main",
            "label": "A",
            "title": "severity_to_priority",
            "scenario": "Write a function that maps severity strings to priority numbers, then call it.",
            "workspace_file": "py_05_function.py",
            "steps_key": "py-function:main",
        },
    ],
    "py-transform": [
        {
            "id": "main",
            "label": "A",
            "title": "transform_incident",
            "scenario": "Map incident fields into ticket fields: external_id, site, description, priority.",
            "workspace_file": "py_06_transform.py",
            "steps_key": "py-transform:main",
        },
    ],
    "filter-fetch": [
        {
            "id": "main",
            "label": "A",
            "title": "Fetch open incidents",
            "scenario": "Auth + GET open incidents from port 5001 and print the count.",
            "workspace_file": "filter_01_fetch.py",
            "steps_key": "filter-fetch:main",
        },
    ],
    "filter-python": [
        {
            "id": "main",
            "label": "A",
            "title": "Filter in Python",
            "scenario": "After the GET, keep only critical and high in Python.",
            "workspace_file": "filter_02_python.py",
            "steps_key": "filter-python:main",
        },
    ],
    "filter-api": [
        {
            "id": "main",
            "label": "A",
            "title": "Filter with query params",
            "scenario": "Pass severity=critical so the API filters for you.",
            "workspace_file": "filter_03_api.py",
            "steps_key": "filter-api:main",
        },
    ],
    "filter-facility": [
        {
            "id": "main",
            "label": "A",
            "title": "Facility keyword filter",
            "scenario": "Find open incidents whose facility contains Water Treatment.",
            "workspace_file": "filter_04_facility.py",
            "steps_key": "filter-facility:main",
        },
    ],
    "sync-transform": [
        {
            "id": "main",
            "label": "A",
            "title": "Transform only (no HTTP)",
            "scenario": "Build a ticket payload from one incident dict — no network calls.",
            "workspace_file": "sync_01_transform.py",
            "steps_key": "sync-transform:main",
        },
    ],
    "sync-post-one": [
        {
            "id": "main",
            "label": "A",
            "title": "POST one ticket",
            "scenario": "Create one ticket on the destination API (port 5002) with DEST key.",
            "workspace_file": "sync_02_post_one.py",
            "steps_key": "sync-post-one:main",
        },
    ],
    "sync-409": [
        {
            "id": "main",
            "label": "A",
            "title": "Handle 409 duplicate",
            "scenario": "POST twice; catch HTTPError 409 and print SKIP.",
            "workspace_file": "sync_03_409.py",
            "steps_key": "sync-409:main",
        },
    ],
    "sync-loop": [
        {
            "id": "main",
            "label": "A",
            "title": "Sync loop critical+high",
            "scenario": "Fetch, filter, transform, POST each; handle 409 duplicates.",
            "workspace_file": "sync_04_loop.py",
            "steps_key": "sync-loop:main",
        },
    ],
    "page-loop": [
        {
            "id": "main",
            "label": "A",
            "title": "Paginate limit=2",
            "scenario": "while + has_more with limit=2; print total count.",
            "workspace_file": "rel_01_paginate.py",
            "steps_key": "page-loop:main",
        },
    ],
    "err-safe-get": [
        {
            "id": "main",
            "label": "A",
            "title": "safe_get_incident",
            "scenario": "Try INC-38192 and INC-99999 — handle 404 without crashing.",
            "workspace_file": "rel_02_safe_get.py",
            "steps_key": "err-safe-get:main",
        },
    ],
    "doc-readme": [
        {
            "id": "main",
            "label": "A",
            "title": "Integration README notes",
            "scenario": "Practice documenting: print Purpose, Env vars, Field mapping, and Errors sections.",
            "workspace_file": "doc_01_readme_notes.py",
            "steps_key": "doc-readme:main",
        },
    ],
    "demo-discovery": [
        {
            "id": "main",
            "label": "A",
            "title": "Discovery answers",
            "scenario": "Type print() answers to four SE discovery questions.",
            "workspace_file": "demo_01_discovery.py",
            "steps_key": "demo-discovery:main",
        },
    ],
    "demo-talktrack": [
        {
            "id": "main",
            "label": "A",
            "title": "5-minute talk track",
            "scenario": "Type each demo section (problem, success, steps, close) as a print() line.",
            "workspace_file": "demo_02_talktrack.py",
            "steps_key": "demo-talktrack:main",
        },
    ],
    # ── Mastery rails, docs/Postman bridges, SE explain ──
    "review-http-python": [
        {
            "id": "main",
            "label": "A",
            "title": "Review health + open incidents",
            "scenario": "Spaced review — call /health, then list open incidents with Bearer from env.",
            "workspace_file": "review_http_python.py",
            "steps_key": "review-http-python:main",
        },
    ],
    "debug-first-request": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix the health request",
            "scenario": "Wrong port — use the debug ritual.",
            "workspace_file": "debug_first_request.py",
            "starter_file": "broken_first_request.py",
            "steps_key": "debug-first-request:main",
        },
    ],
    "exam-open-incidents": [
        {
            "id": "main",
            "label": "A",
            "title": "Exam: list open incidents",
            "scenario": "Blank-file energy. Examples hidden until you struggle.",
            "workspace_file": "exam_open_incidents.py",
            "hide_examples": True,
            "steps_key": "exam-open-incidents:main",
        },
    ],
    "explain-auth": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain Bearer + env",
            "scenario": "Print SE one-liners about Bearer tokens and loading keys from .env.",
            "workspace_file": "explain_auth.py",
            "steps_key": "explain-auth:main",
        },
    ],
    "docs-read-endpoints": [
        {
            "id": "main",
            "label": "A",
            "title": "Read endpoints from docs",
            "scenario": "From mock-apis README: print method, path, and auth for key endpoints.",
            "workspace_file": "docs_read_endpoints.py",
            "steps_key": "docs-read-endpoints:main",
        },
    ],
    "py-from-postman-health": [
        {
            "id": "main",
            "label": "A",
            "title": "Python recreation: health",
            "scenario": "Recreate the Postman GET /health in Python — expect 200.",
            "workspace_file": "py_from_postman_health.py",
            "steps_key": "py-from-postman-health:main",
        },
    ],
    "py-from-postman-get": [
        {
            "id": "main",
            "label": "A",
            "title": "Python recreation: list incidents",
            "scenario": "Recreate the Postman open-incidents GET with Bearer from env.",
            "workspace_file": "py_from_postman_get.py",
            "steps_key": "py-from-postman-get:main",
        },
    ],
    "py-from-postman-post": [
        {
            "id": "main",
            "label": "A",
            "title": "Python recreation: POST + 409",
            "scenario": "Recreate Postman create-ticket; second POST should SKIP on 409.",
            "workspace_file": "py_from_postman_post.py",
            "steps_key": "py-from-postman-post:main",
        },
    ],
    "review-dicts-if-fn": [
        {
            "id": "main",
            "label": "A",
            "title": "Review dicts / if / functions",
            "scenario": "Filter critical+high then transform to ticket fields — no HTTP.",
            "workspace_file": "review_dicts_if_fn.py",
            "steps_key": "review-dicts-if-fn:main",
        },
    ],
    "debug-transform": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix the transform",
            "scenario": "Wrong JSON key (site vs facility) — use the debug ritual.",
            "workspace_file": "debug_transform.py",
            "starter_file": "broken_transform.py",
            "steps_key": "debug-transform:main",
        },
    ],
    "exam-transform-filter": [
        {
            "id": "main",
            "label": "A",
            "title": "Exam: transform + filter",
            "scenario": "Blank-file energy. Examples hidden until you struggle.",
            "workspace_file": "exam_transform_filter.py",
            "hide_examples": True,
            "steps_key": "exam-transform-filter:main",
        },
    ],
    "explain-transform": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain transform",
            "scenario": "Print SE one-liners about mapping source fields to destination tickets.",
            "workspace_file": "explain_transform.py",
            "steps_key": "explain-transform:main",
        },
    ],
    "review-filter": [
        {
            "id": "main",
            "label": "A",
            "title": "Review GET & filter",
            "scenario": "Fetch open incidents and keep only critical + high.",
            "workspace_file": "review_filter.py",
            "steps_key": "review-filter:main",
        },
    ],
    "debug-filter": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix the filter",
            "scenario": "Wrong severities (medium/low) — fix to critical/high.",
            "workspace_file": "debug_filter.py",
            "starter_file": "broken_filter.py",
            "steps_key": "debug-filter:main",
        },
    ],
    "exam-get-filter": [
        {
            "id": "main",
            "label": "A",
            "title": "Exam: GET & filter",
            "scenario": "Blank-file energy. Examples hidden until you struggle.",
            "workspace_file": "exam_get_filter.py",
            "hide_examples": True,
            "steps_key": "exam-get-filter:main",
        },
    ],
    "explain-filter": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain filter",
            "scenario": "Print SE one-liners: API query params vs filtering in Python.",
            "workspace_file": "explain_filter.py",
            "steps_key": "explain-filter:main",
        },
    ],
    "review-sync": [
        {
            "id": "main",
            "label": "A",
            "title": "Review sync loop",
            "scenario": "Fetch → filter critical/high → transform → POST; SKIP on 409.",
            "workspace_file": "review_sync.py",
            "steps_key": "review-sync:main",
        },
    ],
    "debug-409": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix 409 handling",
            "scenario": "Duplicate POST crashes — catch 409 and print SKIP.",
            "workspace_file": "debug_409.py",
            "starter_file": "broken_409.py",
            "steps_key": "debug-409:main",
        },
    ],
    "exam-sync-two-systems": [
        {
            "id": "main",
            "label": "A",
            "title": "Exam: sync two systems",
            "scenario": "Blank-file energy. Examples hidden until you struggle.",
            "workspace_file": "exam_sync_two_systems.py",
            "hide_examples": True,
            "steps_key": "exam-sync-two-systems:main",
        },
    ],
    "explain-409": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain 409 Conflict",
            "scenario": "Print SE one-liners about duplicates and idempotent sync.",
            "workspace_file": "explain_409.py",
            "steps_key": "explain-409:main",
        },
    ],
    "review-page-errors": [
        {
            "id": "main",
            "label": "A",
            "title": "Review pagination + safe GET",
            "scenario": "Paginate with has_more; safe-get a missing ID without crashing.",
            "workspace_file": "review_page_errors.py",
            "steps_key": "review-page-errors:main",
        },
    ],
    "debug-pagination": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix pagination",
            "scenario": "Missing has_more break — use the debug ritual.",
            "workspace_file": "debug_pagination.py",
            "starter_file": "broken_pagination.py",
            "steps_key": "debug-pagination:main",
        },
    ],
    "exam-paginate-safe-get": [
        {
            "id": "main",
            "label": "A",
            "title": "Exam: paginate + safe GET",
            "scenario": "Blank-file energy. Examples hidden until you struggle.",
            "workspace_file": "exam_paginate_safe_get.py",
            "hide_examples": True,
            "steps_key": "exam-paginate-safe-get:main",
        },
    ],
    "explain-pagination": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain pagination",
            "scenario": "Print SE one-liners about page/limit and has_more.",
            "workspace_file": "explain_pagination.py",
            "steps_key": "explain-pagination:main",
        },
    ],
    "review-full-pipeline": [
        {
            "id": "main",
            "label": "A",
            "title": "Review full pipeline",
            "scenario": "End-to-end: open critical/high → tickets with 409 SKIP.",
            "workspace_file": "review_full_pipeline.py",
            "steps_key": "review-full-pipeline:main",
        },
    ],
    "debug-capstone": [
        {
            "id": "main",
            "label": "A",
            "title": "Fix the capstone sketch",
            "scenario": "Missing dotenv, wrong DEST key name, no 409 — fix all.",
            "workspace_file": "debug_capstone.py",
            "starter_file": "broken_capstone.py",
            "steps_key": "debug-capstone:main",
        },
    ],
    "explain-poc-value": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain POC value",
            "scenario": "Print measurable success criteria and the recommended next step.",
            "workspace_file": "explain_poc_value.py",
            "steps_key": "explain-poc-value:main",
        },
    ],
    "explain-401-vs-409": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain 401 vs 409",
            "scenario": "Print the customer-facing difference between auth failure and duplicate.",
            "workspace_file": "explain_401_vs_409.py",
            "steps_key": "explain-401-vs-409:main",
        },
    ],
    "explain-poll-vs-webhook": [
        {
            "id": "main",
            "label": "A",
            "title": "Explain poll vs webhook",
            "scenario": "Print when scheduled polling wins vs when a webhook is better.",
            "workspace_file": "explain_poll_vs_webhook.py",
            "steps_key": "explain-poll-vs-webhook:main",
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
