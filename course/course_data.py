"""Course structure for the Samsara Sales Engineer API & Python Bootcamp."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "exercises" / "guides"
CHEATSHEETS = ROOT / "cheatsheets"
MY_WORK = ROOT / "exercises" / "my-work"

MODULES = [
    {
        "id": "welcome",
        "title": "Role Mission",
        "subtitle": "Build technical credibility and customer value",
        "lessons": [
            {
                "id": "intro",
                "title": "Samsara SE Course Overview",
                "duration": "5 min",
                "type": "content",
                "source": "ROLE_PLAYBOOK.md",
                "description": "How the API work maps to discovery, POCs, demos, and connected operations.",
            },
            {
                "id": "setup",
                "title": "Environment Setup",
                "duration": "10 min",
                "type": "setup",
                "description": "Virtual env, dependencies, mock APIs, and .env file.",
            },
        ],
    },
    {
        "id": "fundamentals",
        "title": "HTTP & APIs — Bit by Bit",
        "subtitle": "Read a tiny chunk, then type it so it sticks",
        "lessons": [
            {
                "id": "http-methods",
                "title": "Read: HTTP Methods",
                "duration": "5 min",
                "type": "cheatsheet",
                "source": "cheatsheets/01_http_methods.md",
                "description": "GET, POST, PUT, PATCH, DELETE — what each means.",
            },
            {
                "id": "practice-methods",
                "title": "Type: Method Meanings",
                "duration": "10 min",
                "type": "type_along",
                "workspace_file": "drill_methods.py",
                "verify_script": None,
                "description": "Type print() lines for each HTTP method meaning.",
            },
            {
                "id": "http-status",
                "title": "Read: Status Codes",
                "duration": "8 min",
                "type": "cheatsheet",
                "source": "cheatsheets/02_status_codes.md",
                "description": "200, 201, 401, 404, 409, 429, 500 — and what to do.",
            },
            {
                "id": "practice-status",
                "title": "Type: Status Code Drill",
                "duration": "10 min",
                "type": "type_along",
                "workspace_file": "drill_status.py",
                "verify_script": None,
                "description": "Type each status code and what you'd do about it.",
            },
            {
                "id": "http-anatomy",
                "title": "Read: Request Anatomy",
                "duration": "8 min",
                "type": "cheatsheet",
                "source": "cheatsheets/03_request_anatomy.md",
                "description": "URL, headers, query params, JSON navigation.",
            },
            {
                "id": "http-basics",
                "title": "Reference: Full HTTP Cheat Sheet",
                "duration": "5 min",
                "type": "cheatsheet",
                "source": "cheatsheets/http-api-basics.md",
                "description": "Keep this open anytime — full reference.",
            },
        ],
    },
    {
        "id": "first-python",
        "title": "First Python — One Skill at a Time",
        "subtitle": "See an example, type it yourself, Analyze, then next line",
        "lessons": [
            {
                "id": "baby-print",
                "title": "1. print()",
                "duration": "5 min",
                "type": "type_along",
                "workspace_file": "baby_01_print.py",
                "description": "Your first line: print a string.",
            },
            {
                "id": "baby-import",
                "title": "2. import requests",
                "duration": "8 min",
                "type": "type_along",
                "workspace_file": "baby_02_import.py",
                "description": "Import the requests library and print that it loaded.",
            },
            {
                "id": "baby-health",
                "title": "3. GET /health (no auth)",
                "duration": "12 min",
                "type": "type_along",
                "workspace_file": "baby_03_health.py",
                "description": "Call the monitoring health endpoint with requests.get.",
            },
            {
                "id": "baby-json",
                "title": "4. Read JSON",
                "duration": "10 min",
                "type": "type_along",
                "workspace_file": "baby_04_json.py",
                "description": "Parse response.json() and print the service name.",
            },
            {
                "id": "baby-variables",
                "title": "5. Store the URL",
                "duration": "8 min",
                "type": "type_along",
                "workspace_file": "baby_05_url_var.py",
                "description": "Put the base URL in a variable — no hardcoding mid-call.",
            },
            {
                "id": "baby-auth",
                "title": "6. Bearer header (hardcoded once)",
                "duration": "12 min",
                "type": "type_along",
                "workspace_file": "baby_06_auth.py",
                "description": "GET /v1/incidents with Authorization Bearer (hardcoded key OK here).",
            },
            {
                "id": "baby-getenv",
                "title": "7. os.getenv — load the key",
                "duration": "12 min",
                "type": "type_along",
                "workspace_file": "baby_07_getenv.py",
                "description": "Replace hardcoded key with os.getenv('SOURCE_API_KEY').",
            },
            {
                "id": "baby-dotenv",
                "title": "8. load_dotenv()",
                "duration": "10 min",
                "type": "type_along",
                "workspace_file": "baby_08_dotenv.py",
                "description": "Load .env so getenv finds your keys.",
            },
            {
                "id": "baby-params",
                "title": "9. Query params",
                "duration": "12 min",
                "type": "type_along",
                "workspace_file": "baby_09_params.py",
                "description": "Pass params={'status': 'open'} to filter at the API.",
            },
            {
                "id": "baby-raise",
                "title": "10. raise_for_status + count",
                "duration": "12 min",
                "type": "type_along",
                "workspace_file": "baby_10_raise.py",
                "description": "Fail loudly on errors; print how many incidents came back.",
            },
            {
                "id": "baby-loop",
                "title": "11. Loop and print fields",
                "duration": "15 min",
                "type": "type_along",
                "workspace_file": "baby_11_loop.py",
                "description": "for incident in data: print id, severity, facility.",
            },
            {
                "id": "http-type-along",
                "title": "12. Put it together",
                "duration": "25 min",
                "type": "type_along",
                "guide": "exercises/guides/01_http_type_along.md",
                "workspace_file": "01_first_request.py",
                "verify_script": None,
                "description": "Combine everything into a real open-incidents script (3 scenarios).",
            },
            {
                "id": "vocabulary",
                "title": "Integration Vocabulary",
                "duration": "10 min",
                "type": "cheatsheet",
                "source": "cheatsheets/vocabulary.md",
                "description": "Terms every Sales Engineer should explain in one sentence.",
            },
        ],
    },
    {
        "id": "gate-first-python",
        "title": "Mastery Gate — First Python",
        "subtitle": "Review, debug, exam, then explain auth like an SE",
        "mastery_lessons": ["review-http-python", "debug-first-request", "exam-open-incidents"],
        "lessons": [
            {
                "id": "debug-ritual-read",
                "title": "Read: Debug Ritual",
                "duration": "5 min",
                "type": "cheatsheet",
                "source": "cheatsheets/debug_ritual.md",
                "description": "Memorize the fix checklist before you debug.",
            },
            {
                "id": "review-http-python",
                "title": "Review: HTTP + Python",
                "duration": "15 min",
                "type": "type_along",
                "workspace_file": "review_http_python.py",
                "description": "Spaced review — health + open incidents from memory.",
            },
            {
                "id": "debug-first-request",
                "title": "Debug: First request",
                "duration": "15 min",
                "type": "type_along",
                "workspace_file": "debug_first_request.py",
                "description": "Wrong port — use the debug ritual to fix it.",
            },
            {
                "id": "exam-open-incidents",
                "title": "Exam: List open incidents",
                "duration": "20 min",
                "type": "type_along",
                "workspace_file": "exam_open_incidents.py",
                "description": "Blank-file energy. Examples hidden until you struggle.",
            },
            {
                "id": "explain-auth",
                "title": "Explain: Bearer + env",
                "duration": "10 min",
                "type": "type_along",
                "workspace_file": "explain_auth.py",
                "description": "Print SE one-liners about Bearer tokens and .env.",
            },
        ],
    },
    {
        "id": "postman",
        "title": "Postman — Click Before You Code",
        "subtitle": "Prove the API works with buttons, then automate",
        "lessons": [
            {"id": "postman-intro", "title": "Read: What is Postman?", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/postman_intro.md", "description": "Why SEs open Postman before writing Python.", "required_prior": ["exam-open-incidents"]},
            {"id": "docs-reading", "title": "Read: How to read API docs", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/docs_reading.md", "description": "Method, path, auth, gotchas — extract before you code."},
            {"id": "docs-read-endpoints", "title": "Type: Read endpoints from docs", "duration": "12 min", "type": "type_along", "workspace_file": "docs_read_endpoints.py", "description": "Print method/path/auth from mock-apis README."},
            {"id": "postman-health-lab", "title": "Lab: Health check in Postman", "duration": "8 min", "type": "lab", "description": "Send GET /health — expect 200, no auth."},
            {"id": "py-from-postman-health", "title": "Python: Recreate health check", "duration": "10 min", "type": "type_along", "workspace_file": "py_from_postman_health.py", "description": "Same GET /health you just clicked — now in Python."},
            {"id": "postman-get-lab", "title": "Lab: List incidents in Postman", "duration": "10 min", "type": "lab", "description": "Bearer auth + GET open incidents."},
            {"id": "py-from-postman-get", "title": "Python: Recreate list incidents", "duration": "12 min", "type": "type_along", "workspace_file": "py_from_postman_get.py", "description": "Same open-incidents GET from Postman — in Python."},
            {"id": "postman-post-lab", "title": "Lab: Create ticket + 409", "duration": "12 min", "type": "lab", "description": "POST a ticket, then duplicate for 409."},
            {"id": "py-from-postman-post", "title": "Python: Recreate POST + 409", "duration": "15 min", "type": "type_along", "workspace_file": "py_from_postman_post.py", "description": "Same create-ticket flow from Postman — handle 409."},
            {"id": "postman-lab", "title": "Lab: Full Postman checklist", "duration": "15 min", "type": "lab", "description": "Final checklist across all collection requests."},
        ],
    },
    {
        "id": "python",
        "title": "Python Building Blocks",
        "subtitle": "One language idea per lesson — then combine",
        "lessons": [
            {"id": "py-read-vars", "title": "Read: Variables", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_01_vars.md", "description": "Strings, numbers, booleans.", "required_prior": ["exam-open-incidents"]},
            {"id": "py-vars", "title": "Type: Variables", "duration": "8 min", "type": "type_along", "workspace_file": "py_01_vars.py", "description": "Create name, count, active and print them."},
            {"id": "py-read-dicts", "title": "Read: Dictionaries", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_02_dicts.md", "description": "JSON objects in Python."},
            {"id": "py-dict", "title": "Type: Make a dict", "duration": "10 min", "type": "type_along", "workspace_file": "py_02_dict.py", "description": "Build an incident dictionary and print fields."},
            {"id": "py-read-lists", "title": "Read: Lists & for", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_03_lists.md", "description": "Lists of dicts like API data arrays."},
            {"id": "py-list-loop", "title": "Type: List + loop", "duration": "12 min", "type": "type_along", "workspace_file": "py_03_list_loop.py", "description": "Loop a list of incidents and print ids."},
            {"id": "py-read-if", "title": "Read: if / else", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_04_if.md", "description": "Decisions and severity filters."},
            {"id": "py-if", "title": "Type: if filter", "duration": "12 min", "type": "type_along", "workspace_file": "py_04_if.py", "description": "Only print critical and high from a list."},
            {"id": "py-read-functions", "title": "Read: Functions", "duration": "6 min", "type": "cheatsheet", "source": "cheatsheets/py_05_functions.md", "description": "Reusable transform recipes."},
            {"id": "py-function", "title": "Type: severity_to_priority", "duration": "12 min", "type": "type_along", "workspace_file": "py_05_function.py", "description": "Write a function that maps severity → number."},
            {"id": "py-transform", "title": "Type: transform_incident", "duration": "15 min", "type": "type_along", "workspace_file": "py_06_transform.py", "description": "Map incident fields into ticket fields."},
            {"id": "python-syntax", "title": "Reference: Python API Syntax", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/python-api-syntax.md", "description": "Full syntax cheat sheet."},
            {"id": "python-type-along", "title": "Put it together: Python basics", "duration": "25 min", "type": "type_along", "guide": "exercises/guides/02_python_type_along.md", "workspace_file": "02_basics.py", "verify_script": "exercises/verify/verify_02.py", "description": "Combine dicts, filters, and transforms (3 scenarios)."},
        ],
    },
    {
        "id": "gate-python",
        "title": "Mastery Gate — Python Blocks",
        "subtitle": "Review dicts/if/functions, then debug and exam",
        "mastery_lessons": ["review-dicts-if-fn", "debug-transform", "exam-transform-filter"],
        "lessons": [
            {"id": "review-dicts-if-fn", "title": "Review: Dicts, if, functions", "duration": "15 min", "type": "type_along", "workspace_file": "review_dicts_if_fn.py", "description": "Spaced review of transform building blocks."},
            {"id": "debug-transform", "title": "Debug: Transform", "duration": "15 min", "type": "type_along", "workspace_file": "debug_transform.py", "description": "Wrong JSON key — fix until site prints."},
            {"id": "exam-transform-filter", "title": "Exam: Transform + filter", "duration": "20 min", "type": "type_along", "workspace_file": "exam_transform_filter.py", "description": "Blank-file: filter then transform."},
            {"id": "explain-transform", "title": "Explain: Transform", "duration": "8 min", "type": "type_along", "workspace_file": "explain_transform.py", "description": "SE one-liner: why we map fields."},
        ],
    },
    {
        "id": "script1",
        "title": "GET & Filter — Piece by Piece",
        "subtitle": "Fetch, then decide what matters",
        "lessons": [
            {"id": "filter-fetch", "title": "Type: Fetch open incidents", "duration": "15 min", "type": "type_along", "workspace_file": "filter_01_fetch.py", "description": "Auth + GET open incidents + print count.", "required_prior": ["exam-transform-filter"]},
            {"id": "filter-python", "title": "Type: Filter in Python", "duration": "15 min", "type": "type_along", "workspace_file": "filter_02_python.py", "description": "Keep only critical and high after the GET."},
            {"id": "filter-api", "title": "Type: Filter with query params", "duration": "12 min", "type": "type_along", "workspace_file": "filter_03_api.py", "description": "Pass severity=critical to the API."},
            {"id": "filter-facility", "title": "Type: Facility keyword filter", "duration": "12 min", "type": "type_along", "workspace_file": "filter_04_facility.py", "description": "Find Water Treatment facilities."},
            {"id": "get-filter", "title": "Put it together: GET & Filter", "duration": "25 min", "type": "type_along", "guide": "exercises/guides/03_get_filter_type_along.md", "workspace_file": "03_get_incidents.py", "verify_script": "exercises/verify/verify_03.py", "description": "Three filter scenarios back-to-back."},
        ],
    },
    {
        "id": "gate-filter",
        "title": "Mastery Gate — GET & Filter",
        "subtitle": "Review, debug the wrong severities, then exam",
        "mastery_lessons": ["review-filter", "debug-filter", "exam-get-filter"],
        "lessons": [
            {"id": "review-filter", "title": "Review: GET & filter", "duration": "15 min", "type": "type_along", "workspace_file": "review_filter.py", "description": "Fetch open, keep critical+high."},
            {"id": "debug-filter", "title": "Debug: Filter", "duration": "15 min", "type": "type_along", "workspace_file": "debug_filter.py", "description": "Filters medium/low by mistake — fix it."},
            {"id": "exam-get-filter", "title": "Exam: GET & filter", "duration": "20 min", "type": "type_along", "workspace_file": "exam_get_filter.py", "description": "Blank-file filter exam."},
            {"id": "explain-filter", "title": "Explain: Filter", "duration": "8 min", "type": "type_along", "workspace_file": "explain_filter.py", "description": "SE one-liner: API vs Python filter."},
        ],
    },
    {
        "id": "script2",
        "title": "System A → B — Piece by Piece",
        "subtitle": "Transform, POST, handle duplicates, then sync",
        "lessons": [
            {"id": "post-read", "title": "Read: POST creates", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_06_post.md", "description": "json= body, 201 vs 409.", "required_prior": ["exam-get-filter"]},
            {"id": "sync-transform", "title": "Type: Transform only", "duration": "12 min", "type": "type_along", "workspace_file": "sync_01_transform.py", "description": "Build ticket payload from one incident dict (no HTTP)."},
            {"id": "sync-post-one", "title": "Type: POST one ticket", "duration": "15 min", "type": "type_along", "workspace_file": "sync_02_post_one.py", "description": "Create one ticket on destination API."},
            {"id": "sync-409", "title": "Type: Handle 409 duplicate", "duration": "15 min", "type": "type_along", "workspace_file": "sync_03_409.py", "description": "POST twice; catch 409 and print SKIP."},
            {"id": "sync-loop", "title": "Type: Sync loop critical+high", "duration": "20 min", "type": "type_along", "workspace_file": "sync_04_loop.py", "description": "Fetch, filter, transform, POST each; handle 409."},
            {"id": "sync-systems", "title": "Put it together: Full sync", "duration": "30 min", "type": "type_along", "guide": "exercises/guides/04_sync_type_along.md", "workspace_file": "04_sync.py", "verify_script": "exercises/verify/verify_04.py", "description": "Three sync variants with stats."},
        ],
    },
    {
        "id": "gate-sync",
        "title": "Mastery Gate — Sync",
        "subtitle": "Review sync, fix 409 handling, then exam",
        "mastery_lessons": ["review-sync", "debug-409", "exam-sync-two-systems"],
        "lessons": [
            {"id": "review-sync", "title": "Review: Sync loop", "duration": "18 min", "type": "type_along", "workspace_file": "review_sync.py", "description": "Fetch → filter → transform → POST with 409."},
            {"id": "debug-409", "title": "Debug: 409 handling", "duration": "15 min", "type": "type_along", "workspace_file": "debug_409.py", "description": "Duplicate POST crashes — catch and SKIP."},
            {"id": "exam-sync-two-systems", "title": "Exam: Sync two systems", "duration": "25 min", "type": "type_along", "workspace_file": "exam_sync_two_systems.py", "description": "Blank-file sync exam."},
            {"id": "explain-409", "title": "Explain: 409 Conflict", "duration": "8 min", "type": "type_along", "workspace_file": "explain_409.py", "description": "SE one-liner: duplicates are OK when skipped."},
        ],
    },
    {
        "id": "reliability",
        "title": "Production Patterns — Piece by Piece",
        "subtitle": "Pagination and errors before the combo",
        "lessons": [
            {"id": "page-read", "title": "Read: Pagination", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_07_pagination.md", "description": "has_more and page loops.", "required_prior": ["exam-sync-two-systems"]},
            {"id": "page-loop", "title": "Type: Paginate limit=2", "duration": "18 min", "type": "type_along", "workspace_file": "rel_01_paginate.py", "description": "while + has_more; print total count."},
            {"id": "err-read", "title": "Read: try/except", "duration": "5 min", "type": "cheatsheet", "source": "cheatsheets/py_08_errors.md", "description": "Timeout and HTTPError without crashing."},
            {"id": "err-safe-get", "title": "Type: safe_get_incident", "duration": "18 min", "type": "type_along", "workspace_file": "rel_02_safe_get.py", "description": "Handle 404 and missing IDs gracefully."},
            {"id": "reliability", "title": "Put it together: Reliability", "duration": "30 min", "type": "type_along", "guide": "exercises/guides/05_reliability_type_along.md", "workspace_file": "05_reliability.py", "verify_script": "exercises/verify/verify_05.py", "description": "Pagination + safe GET scenarios."},
        ],
    },
    {
        "id": "gate-reliability",
        "title": "Mastery Gate — Reliability",
        "subtitle": "Review pagination/errors, debug, then exam",
        "mastery_lessons": ["review-page-errors", "debug-pagination", "exam-paginate-safe-get"],
        "lessons": [
            {"id": "review-page-errors", "title": "Review: Page + errors", "duration": "18 min", "type": "type_along", "workspace_file": "review_page_errors.py", "description": "Paginate with has_more; safe-get pattern."},
            {"id": "debug-pagination", "title": "Debug: Pagination", "duration": "15 min", "type": "type_along", "workspace_file": "debug_pagination.py", "description": "Missing has_more break — fix the loop."},
            {"id": "exam-paginate-safe-get", "title": "Exam: Paginate + safe GET", "duration": "25 min", "type": "type_along", "workspace_file": "exam_paginate_safe_get.py", "description": "Blank-file reliability exam."},
            {"id": "explain-pagination", "title": "Explain: Pagination", "duration": "8 min", "type": "type_along", "workspace_file": "explain_pagination.py", "description": "SE one-liner: why page loops matter."},
        ],
    },
    {
        "id": "capstone",
        "title": "Customer POC",
        "subtitle": "Build, document, and compare",
        "lessons": [
            {"id": "capstone-build", "title": "Type-Along: Connected Operations POC", "duration": "60 min", "type": "type_along", "guide": "exercises/guides/06_capstone_type_along.md", "workspace_file": "06_sync_incidents.py", "verify_script": "exercises/verify/verify_06.py", "description": "Full event→work-order pipeline.", "required_prior": ["exam-paginate-safe-get"]},
            {"id": "doc-readme", "title": "Type: Integration README", "duration": "20 min", "type": "type_along", "workspace_file": "doc_01_readme_notes.py", "description": "Type the purpose, mapping, and run steps as print() sections (practice documenting)."},
            {"id": "reference-capstone", "title": "Reference Implementation", "duration": "15 min", "type": "reference", "description": "Compare with production-style reference."},
        ],
    },
    {
        "id": "demo",
        "title": "Discovery & Demo",
        "subtitle": "Say it out loud like an SE",
        "lessons": [
            {"id": "demo-discovery", "title": "Type: Discovery answers", "duration": "15 min", "type": "type_along", "workspace_file": "demo_01_discovery.py", "description": "Type print() answers to discovery questions."},
            {"id": "demo-talktrack", "title": "Type: 5-minute talk track", "duration": "15 min", "type": "type_along", "workspace_file": "demo_02_talktrack.py", "description": "Type each demo section as a print() line."},
            {"id": "explain-401-vs-409", "title": "Explain: 401 vs 409", "duration": "8 min", "type": "type_along", "workspace_file": "explain_401_vs_409.py", "description": "Print the difference customers care about."},
            {"id": "explain-poll-vs-webhook", "title": "Explain: Poll vs webhook", "duration": "8 min", "type": "type_along", "workspace_file": "explain_poll_vs_webhook.py", "description": "When to poll vs when a webhook wins."},
            {"id": "se-demo", "title": "Read: Full Role Playbook", "duration": "20 min", "type": "content", "source": "ROLE_PLAYBOOK.md", "description": "Discovery, demo, IoT path, interview story."},
        ],
    },
    {
        "id": "gate-capstone",
        "title": "Mastery Gate — Capstone",
        "subtitle": "Full pipeline review, debug, then POC value",
        "mastery_lessons": ["review-full-pipeline", "debug-capstone"],
        "lessons": [
            {"id": "review-full-pipeline", "title": "Review: Full pipeline", "duration": "25 min", "type": "type_along", "workspace_file": "review_full_pipeline.py", "description": "End-to-end sync from memory."},
            {"id": "debug-capstone", "title": "Debug: Capstone", "duration": "20 min", "type": "type_along", "workspace_file": "debug_capstone.py", "description": "Missing dotenv, wrong key name, no 409 — fix all."},
            {"id": "explain-poc-value", "title": "Explain: POC value", "duration": "10 min", "type": "type_along", "workspace_file": "explain_poc_value.py", "description": "Print measurable success criteria and next step."},
        ],
    },
    {
        "id": "exam",
        "title": "Final Exam",
        "subtitle": "Blank file. No guides. You've earned this.",
        "lessons": [
            {"id": "self-test", "title": "Self-Test Challenge", "duration": "45 min", "type": "exam", "description": "Rebuild the integration and explain the value.", "required_prior": ["debug-capstone", "explain-poc-value"]},
        ],
    },
]


def all_lessons():
    lessons = []
    for module in MODULES:
        for lesson in module["lessons"]:
            lessons.append({**lesson, "module_id": module["id"], "module_title": module["title"]})
    return lessons


def get_lesson(lesson_id):
    for lesson in all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None


def lesson_index(lesson_id):
    lessons = all_lessons()
    for i, lesson in enumerate(lessons):
        if lesson["id"] == lesson_id:
            return i
    return -1


def next_prev(lesson_id):
    lessons = all_lessons()
    idx = lesson_index(lesson_id)
    prev_lesson = lessons[idx - 1] if idx > 0 else None
    next_lesson = lessons[idx + 1] if idx < len(lessons) - 1 else None
    return prev_lesson, next_lesson


def total_lessons():
    return len(all_lessons())
