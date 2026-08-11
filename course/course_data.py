"""Course structure for the API Integration Bootcamp."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "exercises" / "guides"
CHEATSHEETS = ROOT / "cheatsheets"
MY_WORK = ROOT / "exercises" / "my-work"

MODULES = [
    {
        "id": "welcome",
        "title": "Welcome",
        "subtitle": "Get set up in 5 minutes",
        "lessons": [
            {
                "id": "intro",
                "title": "Course Overview",
                "duration": "5 min",
                "type": "content",
                "description": "What you'll build today and how this course works.",
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
        "title": "HTTP & APIs",
        "subtitle": "The foundation everything else sits on",
        "lessons": [
            {
                "id": "http-basics",
                "title": "HTTP Methods & Status Codes",
                "duration": "15 min",
                "type": "cheatsheet",
                "source": "cheatsheets/http-api-basics.md",
                "description": "GET, POST, auth, JSON, and status codes.",
            },
            {
                "id": "http-type-along",
                "title": "Type-Along: First API Request",
                "duration": "30 min",
                "type": "type_along",
                "guide": "exercises/guides/01_http_type_along.md",
                "workspace_file": "01_first_request.py",
                "verify_script": None,
                "description": "Type your first Python script that calls an API.",
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
        "id": "postman",
        "title": "Explore with Postman",
        "subtitle": "Test before you automate",
        "lessons": [
            {
                "id": "postman-lab",
                "title": "Postman Lab",
                "duration": "30 min",
                "type": "lab",
                "description": "Import the collection and call every mock API endpoint.",
            },
        ],
    },
    {
        "id": "python",
        "title": "Python for Integrations",
        "subtitle": "Only the syntax you actually need",
        "lessons": [
            {
                "id": "python-syntax",
                "title": "Python API Syntax",
                "duration": "15 min",
                "type": "cheatsheet",
                "source": "cheatsheets/python-api-syntax.md",
                "description": "requests, env vars, loops, transforms.",
            },
            {
                "id": "python-type-along",
                "title": "Type-Along: Python Basics",
                "duration": "45 min",
                "type": "type_along",
                "guide": "exercises/guides/02_python_type_along.md",
                "workspace_file": "02_basics.py",
                "verify_script": "exercises/verify/verify_02.py",
                "description": "Dictionaries, filters, and schema mapping.",
            },
        ],
    },
    {
        "id": "script1",
        "title": "Script #1 — GET & Filter",
        "subtitle": "Retrieve and filter operational data",
        "lessons": [
            {
                "id": "get-filter",
                "title": "Type-Along: GET Incidents",
                "duration": "45 min",
                "type": "type_along",
                "guide": "exercises/guides/03_get_filter_type_along.md",
                "workspace_file": "03_get_incidents.py",
                "verify_script": "exercises/verify/verify_03.py",
                "description": "Authenticate, fetch JSON, filter critical incidents.",
            },
        ],
    },
    {
        "id": "script2",
        "title": "Script #2 — System A → B",
        "subtitle": "Transfer data between APIs",
        "lessons": [
            {
                "id": "sync-systems",
                "title": "Type-Along: Sync Two Systems",
                "duration": "60 min",
                "type": "type_along",
                "guide": "exercises/guides/04_sync_type_along.md",
                "workspace_file": "04_sync.py",
                "verify_script": "exercises/verify/verify_04.py",
                "description": "Fetch, transform, POST tickets, handle duplicates.",
            },
        ],
    },
    {
        "id": "reliability",
        "title": "Production Patterns",
        "subtitle": "Pagination, errors, idempotency",
        "lessons": [
            {
                "id": "reliability",
                "title": "Type-Along: Reliability",
                "duration": "45 min",
                "type": "type_along",
                "guide": "exercises/guides/05_reliability_type_along.md",
                "workspace_file": "05_reliability.py",
                "verify_script": "exercises/verify/verify_05.py",
                "description": "Paginate through all records and handle failures gracefully.",
            },
        ],
    },
    {
        "id": "capstone",
        "title": "Capstone Project",
        "subtitle": "Build the full integration",
        "lessons": [
            {
                "id": "capstone-build",
                "title": "Type-Along: Full Integration",
                "duration": "90 min",
                "type": "type_along",
                "guide": "exercises/guides/06_capstone_type_along.md",
                "workspace_file": "06_sync_incidents.py",
                "verify_script": "exercises/verify/verify_06.py",
                "description": "Complete incident-to-ticket pipeline with documentation.",
            },
            {
                "id": "reference-capstone",
                "title": "Reference Implementation",
                "duration": "15 min",
                "type": "reference",
                "description": "Compare your work with the production-style reference script.",
            },
        ],
    },
    {
        "id": "exam",
        "title": "Final Exam",
        "subtitle": "Prove it from a blank file",
        "lessons": [
            {
                "id": "self-test",
                "title": "Self-Test Challenge",
                "duration": "45 min",
                "type": "exam",
                "description": "Rebuild the integration without guides or solutions.",
            },
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
