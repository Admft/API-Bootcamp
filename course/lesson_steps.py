"""Step checks keyed by lesson:exercise — used by Analyze."""

# Shared check snippets
_SETUP_IMPORTS = [
    {"type": "has_import", "module": "requests", "message": "Import requests"},
    {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
    {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
    {"type": "no_hardcoded_secrets", "message": "No hardcoded API keys"},
]

LESSON_STEPS = {
    # ── http-type-along:open-incidents ──
    "http-type-along:open-incidents": [
        {
            "id": 'h01',
            "title": 'Import os',
            "instruction": (
                'Start a fresh file. First import os so you can read environment variables.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'os lets you read secrets from the environment instead of hardcoding them.',
            "common_mistake": 'Typing `from os import getenv` is fine later — for now use `import os`.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'h02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": "requests is the library you'll use to call HTTP APIs.",
            "common_mistake": "Don't write `import request` (singular) — the package name is requests.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'h03',
            "title": 'Import load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'from dotenv import load_dotenv',
            "why": 'load_dotenv reads your .env file into the process environment.',
            "common_mistake": "It's `from dotenv import load_dotenv`, not `import dotenv.load_dotenv`.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Import load_dotenv'},
            ],
        },
        {
            "id": 'h04',
            "title": 'Call load_dotenv',
            "instruction": (
                'Add this under what you already typed — call the function so .env is loaded.\n'
                '\n'
                'EXAMPLE:\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'load_dotenv()',
            "why": 'Importing alone does nothing; you must call load_dotenv().',
            "common_mistake": 'Forgetting the parentheses means the .env file never loads.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"load_dotenv\s*\(", "message": 'Call load_dotenv()'},
            ],
        },
        {
            "id": 'h05',
            "title": 'Load SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'The monitoring API expects a Bearer token from SOURCE_API_KEY.',
            "common_mistake": "Don't paste the key as a string literal — always use os.getenv.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'contains', "value": 'os.getenv', "message": 'Use os.getenv()'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded API keys'},
            ],
        },
        {
            "id": 'h06',
            "title": 'Load SOURCE_API_URL',
            "instruction": (
                'Add this under what you already typed. Default to the mock monitoring API on port 5001.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")',
            "why": 'A base URL variable keeps every request pointed at the right host.',
            "common_mistake": 'Port 5001 is the source/monitoring mock — not 5002 (ticketing).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Load SOURCE_API_URL'},
                {"type": 'contains', "value": '5001', "message": 'Default to port 5001'},
            ],
        },
        {
            "id": 'h07',
            "title": 'Start the GET call',
            "instruction": (
                "Add this under what you already typed. We'll fill headers and params next.\n"
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                ')'
            ),
            "why": 'GET /v1/incidents is the list endpoint on the monitoring API.',
            "common_mistake": "Use an f-string with SOURCE_API_URL — don't hardcode the full URL only.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.get', "message": 'Use requests.get()'},
                {"type": 'contains', "value": '/v1/incidents', "message": 'Hit /v1/incidents'},
            ],
        },
        {
            "id": 'h08',
            "title": 'Add Bearer auth header',
            "instruction": (
                'Update your GET to include the Authorization header. Add this under / replace your previous GET.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                ')'
            ),
            "why": 'The mock APIs reject requests without a valid Bearer token.',
            "common_mistake": 'Write Bearer with a capital B and a space before the key.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"Bearer", "message": 'Bearer authentication'},
                {"type": 'contains', "value": 'Authorization', "message": 'Set Authorization header'},
            ],
        },
        {
            "id": 'h09',
            "title": 'Filter status=open',
            "instruction": (
                'Add params so the API returns only open incidents.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                ')'
            ),
            "why": 'Query params let the API filter before sending data back.',
            "common_mistake": 'Use params={"status": "open"} — not a path like /open.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'params', "message": 'Pass params'},
                {"type": 'contains', "value": 'status', "message": 'Filter status=open'},
                {"type": 'contains', "value": 'open', "message": 'status value open'},
            ],
        },
        {
            "id": 'h10',
            "title": 'Add timeout',
            "instruction": (
                "Add timeout=30 so a hung API can't freeze your script forever.\n"
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')'
            ),
            "why": 'Timeouts are a reliability habit — always set one on network calls.',
            "common_mistake": 'timeout is in seconds (30), not milliseconds.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'timeout', "message": 'Pass timeout'},
                {"type": 'contains', "value": 'requests.get', "message": 'Keep requests.get'},
            ],
        },
        {
            "id": 'h11',
            "title": 'Raise on HTTP errors',
            "instruction": (
                'Add this under your GET. It raises if the status is 4xx/5xx.\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response.raise_for_status()',
            "why": 'raise_for_status turns failed HTTP responses into Python exceptions.',
            "common_mistake": 'Calling .json() without checking status can hide 401/404 errors.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'Check HTTP status'},
            ],
        },
        {
            "id": 'h12',
            "title": 'Parse JSON body',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'data = response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'data = response.json()',
            "why": 'response.json() turns the HTTP body into a Python dict/list.',
            "common_mistake": "Don't use json.loads(response.text) unless you have a reason — .json() is enough.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'json()', "message": 'Parse JSON'},
            ],
        },
        {
            "id": 'h13',
            "title": 'Print the open count',
            "instruction": (
                'Add this under what you already typed. The list lives under the data key.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Count:", len(data["data"]))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Count:", len(data["data"]))',
            "why": 'Printing the count proves your filter and auth worked.',
            "common_mistake": 'The envelope is {"data": [...]} — count data["data"], not data itself.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print incident count'},
                {"type": 'contains', "value": 'len(', "message": 'Use len()'},
                {"type": 'contains', "value": '["data"]', "message": 'Read data key'},
            ],
        },
        {
            "id": 'h14',
            "title": 'Run against the mock API',
            "instruction": (
                'Keep your full script. Mock APIs and .env must be ready. Click Analyze to run it.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Count:", len(data["data"]))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Count:", len(data["data"]))',
            "why": 'Running end-to-end confirms auth, URL, and params against the live mock.',
            "common_mistake": 'If it fails, check mock APIs are running and SOURCE_API_KEY is in .env.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
                {"type": 'runs', "message": 'Script runs without error'},
                {"type": 'output_contains', "value": 'Count:', "message": 'Output shows Count:'},
            ],
        },
    ],

    # ── http-type-along:health-check ──
    "http-type-along:health-check": [
        {
            "id": 'hb01',
            "title": 'Import requests',
            "instruction": (
                'Start fresh. Health checks need no .env — just requests.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": 'Even a health probe uses the same HTTP client as real API work.',
            "common_mistake": "Don't skip the import — requests isn't built into Python.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'hb02',
            "title": 'Set BASE_URL',
            "instruction": (
                'Add this under what you already typed. Point at the monitoring mock.\n'
                '\n'
                'EXAMPLE:\n'
                'BASE_URL = "http://127.0.0.1:5001"\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'BASE_URL = "http://127.0.0.1:5001"',
            "why": 'A base URL keeps paths short and easy to change later.',
            "common_mistake": 'Use 5001 (monitoring), not 5002 (ticketing).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'BASE_URL', "message": 'Define BASE_URL'},
                {"type": 'contains', "value": '5001', "message": 'Point at port 5001'},
            ],
        },
        {
            "id": 'hb03',
            "title": 'Build the health URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'url = f"{BASE_URL}/health"\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'url = f"{BASE_URL}/health"',
            "why": '/health is the liveness endpoint — no auth required.',
            "common_mistake": 'Path is /health, not /v1/health.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '/health', "message": 'Include /health path'},
            ],
        },
        {
            "id": 'hb04',
            "title": 'GET the health endpoint',
            "instruction": (
                'Add this under what you already typed. No Authorization header.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(url, timeout=30)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response = requests.get(url, timeout=30)',
            "why": 'A health check should be the simplest GET you write.',
            "common_mistake": 'Do not add Authorization — health is intentionally public on the mock.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.get', "message": 'Use requests.get()'},
                {"type": 'contains', "value": 'timeout', "message": 'Pass timeout'},
                {"type": 'not_contains', "value": 'Authorization', "message": 'Health check needs no auth'},
            ],
        },
        {
            "id": 'hb05',
            "title": 'Print status_code',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(response.status_code)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(response.status_code)',
            "why": 'status_code tells you immediately if the service answered OK.',
            "common_mistake": "It's response.status_code, not response.status.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'status_code', "message": 'Read status_code'},
                {"type": 'contains', "value": 'print', "message": 'Print status_code'},
            ],
        },
        {
            "id": 'hb06',
            "title": 'Raise on bad status',
            "instruction": (
                'Add this under what you already typed (before or after the status print is fine).\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response.raise_for_status()',
            "why": 'Even health checks should fail loudly on 5xx.',
            "common_mistake": "raise_for_status() has parentheses — it's a method call.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'Check response status'},
            ],
        },
        {
            "id": 'hb07',
            "title": 'Parse JSON',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'body = response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'body = response.json()',
            "why": 'The health payload is JSON with service metadata.',
            "common_mistake": 'Call .json() on the response object, not on status_code.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'json()', "message": 'Parse JSON body'},
            ],
        },
        {
            "id": 'hb08',
            "title": 'Read the service field',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Service:", body["service"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Service:", body["service"])',
            "why": 'Printing service proves you parsed the right JSON shape.',
            "common_mistake": 'Key is "service", not "name" or "app".',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'service', "message": 'Read the service field'},
                {"type": 'contains', "value": 'print', "message": 'Print the result'},
            ],
        },
        {
            "id": 'hb09',
            "title": 'Also print status from body',
            "instruction": (
                'Add this under what you already typed for extra confidence.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Status:", body.get("status"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Status:", body.get("status"))',
            "why": '.get avoids a KeyError if a field is missing while you explore.',
            "common_mistake": "body.get('status') is the JSON field — different from HTTP status_code.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'status', "message": 'Read status from body'},
                {"type": 'contains', "value": 'print', "message": 'Keep prints'},
            ],
        },
        {
            "id": 'hb10',
            "title": 'Confirm no auth headers',
            "instruction": (
                'Double-check your GET has no Authorization header. Keep the rest of the script.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(url, timeout=30)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response = requests.get(url, timeout=30)',
            "why": "Health endpoints are for 'is it up?' — keep them unauthenticated.",
            "common_mistake": 'If you copied an incidents GET, remove headers=...',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '/health', "message": 'Hit /health'},
                {"type": 'not_contains', "value": 'Authorization', "message": 'No Authorization header'},
                {"type": 'not_contains', "value": 'SOURCE_API_KEY', "message": 'No API key needed'},
            ],
        },
        {
            "id": 'hb11',
            "title": 'Keep the service print',
            "instruction": (
                'Make sure you still print the service name before running.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Service:", body["service"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Service:", body["service"])',
            "why": 'The final check will look for monitoring-api in the output.',
            "common_mistake": "Don't rename the print so much that the word Service disappears.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'service', "message": 'Keep service field access'},
                {"type": 'contains', "value": 'print', "message": 'Keep print'},
            ],
        },
        {
            "id": 'hb12',
            "title": 'Run the health check',
            "instruction": (
                'Mock monitoring API must be running on 5001. Click Analyze to execute.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Service:", body["service"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Service:", body["service"])',
            "why": 'A green run means your laptop can reach the mock API.',
            "common_mistake": "Connection refused usually means the mock API isn't started.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": '/health', "message": 'Hit /health'},
                {"type": 'runs', "message": 'Script runs without error'},
                {"type": 'output_contains', "value": 'monitoring-api', "message": 'Output shows monitoring-api'},
            ],
        },
    ],

    # ── http-type-along:single-incident ──
    "http-type-along:single-incident": [
        {
            "id": 'hs01',
            "title": 'Import os',
            "instruction": (
                'Start fresh for a single-incident GET.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": "You'll load SOURCE_API_KEY from the environment.",
            "common_mistake": 'Keep import os at the top of the file.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'hs02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": 'requests performs the HTTP GET for one incident id.',
            "common_mistake": 'Spelling is requests (plural).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'hs03',
            "title": 'Import load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'from dotenv import load_dotenv',
            "why": '.env holds your mock API keys for class.',
            "common_mistake": 'Import load_dotenv before calling it.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Import load_dotenv'},
            ],
        },
        {
            "id": 'hs04',
            "title": 'Call load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'load_dotenv()',
            "why": 'Without this call, os.getenv may return None.',
            "common_mistake": 'Remember the parentheses.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"load_dotenv\s*\(", "message": 'Call load_dotenv()'},
            ],
        },
        {
            "id": 'hs05',
            "title": 'Load SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Single-resource GETs still require Bearer auth on this API.',
            "common_mistake": 'Never hardcode the key string.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded keys'},
            ],
        },
        {
            "id": 'hs06',
            "title": 'Load SOURCE_API_URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")',
            "why": 'Default to the local monitoring mock.',
            "common_mistake": '5001 is source; 5002 is destination.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Load SOURCE_API_URL'},
                {"type": 'contains', "value": '5001', "message": 'Default port 5001'},
            ],
        },
        {
            "id": 'hs07',
            "title": 'Pick the incident id',
            "instruction": (
                'Add this under what you already typed. Hospital grid alert id.\n'
                '\n'
                'EXAMPLE:\n'
                'incident_id = "INC-38201"\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'incident_id = "INC-38201"',
            "why": 'Storing the id in a variable makes the URL easier to read.',
            "common_mistake": 'Use INC-38201 exactly (hospital scenario).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-38201', "message": 'Use incident INC-38201'},
            ],
        },
        {
            "id": 'hs08',
            "title": 'GET by id with auth',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    timeout=30,\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    timeout=30,\n'
                ')'
            ),
            "why": 'Detail routes put the id in the path: /v1/incidents/{id}.',
            "common_mistake": "Don't put the id only in params for this exercise.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.get', "message": 'Use GET request'},
                {"type": 'regex', "pattern": r"Bearer", "message": 'Use Bearer token'},
                {"type": 'contains', "value": 'INC-38201', "message": 'Request incident INC-38201'},
            ],
        },
        {
            "id": 'hs09',
            "title": 'Raise for status',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response.raise_for_status()',
            "why": '404/401 should fail clearly before you print fields.',
            "common_mistake": 'Call raise_for_status before .json().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'Handle HTTP errors'},
            ],
        },
        {
            "id": 'hs10',
            "title": 'Parse the incident',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'incident = response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'incident = response.json()',
            "why": 'A single-incident response is one object, not a data list.',
            "common_mistake": "Don't do response.json()['data'] for this detail endpoint.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'json()', "message": 'Parse JSON'},
            ],
        },
        {
            "id": 'hs11',
            "title": 'Print facility',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(incident["facility"])',
            "why": 'Facility tells ops where the alert happened.',
            "common_mistake": 'Key is "facility", not "site" (site comes after transform).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'facility', "message": 'Access facility field'},
                {"type": 'contains', "value": 'print', "message": 'Print facility'},
            ],
        },
        {
            "id": 'hs12',
            "title": 'Print message',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["message"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(incident["message"])',
            "why": 'Message is the human-readable alert text.',
            "common_mistake": 'Key is "message", not "description" yet.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'message', "message": 'Access message field'},
                {"type": 'contains', "value": 'print', "message": 'Print message'},
            ],
        },
        {
            "id": 'hs13',
            "title": 'Run and verify facility',
            "instruction": (
                'Keep both prints. Click Analyze — mock API + .env required.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["facility"])\n'
                'print(incident["message"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'print(incident["facility"])\n'
                'print(incident["message"])'
            ),
            "why": 'Running proves INC-38201 resolves on the mock API.',
            "common_mistake": 'If facility is missing, you may have hit the list endpoint by mistake.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-38201', "message": 'Keep INC-38201'},
                {"type": 'runs', "message": 'Script runs without error'},
                {"type": 'output_contains', "value": 'Hospital', "message": 'Output mentions Hospital'},
            ],
        },
        {
            "id": 'hs14',
            "title": 'Confirm voltage sag message',
            "instruction": (
                'Final run should show the voltage sag text. Click Analyze again if needed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["message"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(incident["message"])',
            "why": 'Matching the known message confirms you fetched the right record.',
            "common_mistake": 'Wrong id → wrong message; stick with INC-38201.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'message', "message": 'Print message'},
                {"type": 'output_contains', "value": 'Voltage', "message": 'Output mentions Voltage sag'},
            ],
        },
    ],

    # ── python-type-along:water-plant ──
    "python-type-along:water-plant": [
        {
            "id": 'p01',
            "title": 'Start the incident dict',
            "instruction": (
                'Start offline Python practice. Create an empty incident dict.\n'
                '\n'
                'EXAMPLE:\n'
                'incident = {\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'incident = {\n'
                '}'
            ),
            "why": 'Dictionaries are how JSON objects look in Python.',
            "common_mistake": 'Use curly braces {}, not square brackets [].',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"incident\s*=\s*\{", "message": 'Create incident dictionary'},
            ],
        },
        {
            "id": 'p02',
            "title": 'Add id field',
            "instruction": (
                'Add the id field inside the dict.\n'
                '\n'
                'EXAMPLE:\n'
                'incident = {\n'
                '    "id": "INC-38192",\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'incident = {\n'
                '    "id": "INC-38192",\n'
                '}'
            ),
            "why": 'Every incident needs a stable id for later ticket external_id mapping.',
            "common_mistake": 'Quotes around keys and string values are required.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-38192', "message": 'Include INC-38192'},
                {"type": 'contains', "value": '"id"', "message": 'Include id key'},
            ],
        },
        {
            "id": 'p03',
            "title": 'Add facility + severity + message',
            "instruction": (
                'Fill in the remaining fields under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'incident = {\n'
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'incident = {\n'
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                '}'
            ),
            "why": 'These four fields mirror what the monitoring API returns.',
            "common_mistake": 'Trailing commas after the last field are fine in Python.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'facility', "message": 'Include facility'},
                {"type": 'contains', "value": 'severity', "message": 'Include severity'},
                {"type": 'contains', "value": 'message', "message": 'Include message'},
            ],
        },
        {
            "id": 'p04',
            "title": 'Print facility',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(incident["facility"])',
            "why": 'Square-bracket access is how you read JSON fields in Python.',
            "common_mistake": 'Use double quotes consistently inside the brackets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print something'},
                {"type": 'contains', "value": 'facility', "message": 'Read facility'},
            ],
        },
        {
            "id": 'p05',
            "title": 'Print severity too',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(incident["severity"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(incident["severity"])',
            "why": "You'll filter on severity constantly in later lessons.",
            "common_mistake": "Don't print the whole dict yet — practice field access.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'severity', "message": 'Print severity'},
            ],
        },
        {
            "id": 'p06',
            "title": 'Create incidents list',
            "instruction": (
                'Add this under what you already typed — a small list to practice filtering.\n'
                '\n'
                'EXAMPLE:\n'
                'incidents = [\n'
                '    {"id": "INC-001", "severity": "critical", "facility": "Plant A"},\n'
                '    {"id": "INC-002", "severity": "low", "facility": "Plant B"},\n'
                '    {"id": "INC-003", "severity": "high", "facility": "Plant C"},\n'
                ']\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'incidents = [\n'
                '    {"id": "INC-001", "severity": "critical", "facility": "Plant A"},\n'
                '    {"id": "INC-002", "severity": "low", "facility": "Plant B"},\n'
                '    {"id": "INC-003", "severity": "high", "facility": "Plant C"},\n'
                ']'
            ),
            "why": 'APIs return lists of objects; practice the same shape offline.',
            "common_mistake": 'Square brackets for the list, curly braces for each item.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'incidents', "message": 'Create incidents list'},
            ],
        },
        {
            "id": 'p07',
            "title": 'Define SYNC_SEVERITIES',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SYNC_SEVERITIES = ["critical", "high"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = ["critical", "high"]',
            "why": 'A named allow-list makes the sync rule obvious and changeable.',
            "common_mistake": 'Include both critical and high for this water-plant exercise.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SYNC_SEVERITIES', "message": 'Define SYNC_SEVERITIES'},
                {"type": 'contains', "value": 'critical', "message": 'Include critical'},
                {"type": 'contains', "value": 'high', "message": 'Include high'},
            ],
        },
        {
            "id": 'p08',
            "title": 'Filter loop with SKIP',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for item in incidents:\n'
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(f"WILL SYNC: {item[\'id\']}")\n'
                '    else:\n'
                '        print(f"SKIP: {item[\'id\']}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for item in incidents:\n'
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(f"WILL SYNC: {item[\'id\']}")\n'
                '    else:\n'
                '        print(f"SKIP: {item[\'id\']}")'
            ),
            "why": 'Printing SKIP makes filter decisions visible during testing.',
            "common_mistake": 'Use `in SYNC_SEVERITIES`, not == "critical" only.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'for ', "message": 'Loop with for'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP for non-matches'},
                {"type": 'contains', "value": 'WILL SYNC', "message": 'Print WILL SYNC for matches'},
            ],
        },
        {
            "id": 'p09',
            "title": 'severity_to_priority function',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def severity_to_priority(severity):\n'
                '    if severity == "critical":\n'
                '        return 1\n'
                '    if severity == "high":\n'
                '        return 2\n'
                '    if severity == "medium":\n'
                '        return 3\n'
                '    return 4\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def severity_to_priority(severity):\n'
                '    if severity == "critical":\n'
                '        return 1\n'
                '    if severity == "high":\n'
                '        return 2\n'
                '    if severity == "medium":\n'
                '        return 3\n'
                '    return 4'
            ),
            "why": 'Ticketing systems often want numeric priority, not severity words.',
            "common_mistake": "critical → 1 (highest). Don't reverse the scale.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'severity_to_priority', "message": 'Define severity_to_priority()'},
            ],
        },
        {
            "id": 'p10',
            "title": 'transform_incident function',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(inc):\n'
                '    return {\n'
                '        "external_id": inc["id"],\n'
                '        "site": inc["facility"],\n'
                '        "description": inc.get("message", "No description"),\n'
                '        "priority": severity_to_priority(inc["severity"]),\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(inc):\n'
                '    return {\n'
                '        "external_id": inc["id"],\n'
                '        "site": inc["facility"],\n'
                '        "description": inc.get("message", "No description"),\n'
                '        "priority": severity_to_priority(inc["severity"]),\n'
                '    }'
            ),
            "why": 'Transform maps source field names to destination ticket fields.',
            "common_mistake": "external_id comes from id — don't leave it as id in the ticket.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_incident', "message": 'Define transform_incident()'},
                {"type": 'contains', "value": 'external_id', "message": 'Map external_id'},
            ],
        },
        {
            "id": 'p11',
            "title": 'Transform the water incident',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'ticket = transform_incident(incident)\n'
                'print(ticket)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'ticket = transform_incident(incident)\n'
                'print(ticket)'
            ),
            "why": 'Calling transform on your dict proves the mapping works.',
            "common_mistake": 'Pass incident (the dict), not the string id.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'transform_incident', "message": 'Call transform_incident'},
                {"type": 'contains', "value": 'print', "message": 'Print ticket'},
            ],
        },
        {
            "id": 'p12',
            "title": 'Run — see SKIP output',
            "instruction": (
                'Keep the filter loop in the file. Click Analyze to run.\n'
                '\n'
                'EXAMPLE:\n'
                'for item in incidents:\n'
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(f"WILL SYNC: {item[\'id\']}")\n'
                '    else:\n'
                '        print(f"SKIP: {item[\'id\']}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for item in incidents:\n'
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(f"WILL SYNC: {item[\'id\']}")\n'
                '    else:\n'
                '        print(f"SKIP: {item[\'id\']}")'
            ),
            "why": 'INC-002 is low severity and should print SKIP.',
            "common_mistake": 'If nothing prints SKIP, your else branch is missing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SKIP', "message": 'Keep SKIP print'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output shows SKIP'},
            ],
        },
        {
            "id": 'p13',
            "title": 'Confirm WILL SYNC lines',
            "instruction": (
                'Also print external_id and priority from the transformed ticket. Click Analyze.\n'
                '\n'
                'EXAMPLE:\n'
                'print(ticket["external_id"], ticket["priority"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(ticket["external_id"], ticket["priority"])',
            "why": 'critical should become priority 1 with external_id INC-38192.',
            "common_mistake": 'If priority is wrong, check severity_to_priority.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'external_id', "message": 'Use external_id'},
                {"type": 'output_contains', "value": 'WILL SYNC', "message": 'Output shows WILL SYNC'},
                {"type": 'output_contains', "value": 'INC-38192', "message": 'Output mentions INC-38192'},
            ],
        },
    ],

    # ── python-type-along:gas-pipeline ──
    "python-type-along:gas-pipeline": [
        {
            "id": 'gp01',
            "title": 'Create empty event dict',
            "instruction": (
                'Gas pipeline feed uses different field names. Start an event dict.\n'
                '\n'
                'EXAMPLE:\n'
                'event = {\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'event = {\n'
                '}'
            ),
            "why": 'Source systems rarely match your ticket schema 1:1.',
            "common_mistake": "Name it event — this source doesn't say incident.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"event\s*=\s*\{", "message": 'Create event dictionary'},
            ],
        },
        {
            "id": 'gp02',
            "title": 'Add eventId',
            "instruction": (
                'Add eventId (camelCase) — not id.\n'
                '\n'
                'EXAMPLE:\n'
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '}'
            ),
            "why": "eventId is the source system's primary key.",
            "common_mistake": "Don't rename it to id in the source dict — transform later.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'eventId', "message": 'Use eventId key (source schema)'},
            ],
        },
        {
            "id": 'gp03',
            "title": 'Add locationName',
            "instruction": (
                'Add locationName under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '    "locationName": "Gas Pipeline Station 7",\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '    "locationName": "Gas Pipeline Station 7",\n'
                '}'
            ),
            "why": "locationName is this API's word for facility/site.",
            "common_mistake": 'Spelling is locationName (camelCase), not location_name.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'locationName', "message": 'Use locationName key'},
            ],
        },
        {
            "id": 'gp04',
            "title": 'Add severity + message',
            "instruction": (
                'Finish the source event. Note severity is UPPERCASE here.\n'
                '\n'
                'EXAMPLE:\n'
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '    "locationName": "Gas Pipeline Station 7",\n'
                '    "severity": "CRITICAL",\n'
                '    "message": "Pressure anomaly detected",\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'event = {\n'
                '    "eventId": "EVT-9001",\n'
                '    "locationName": "Gas Pipeline Station 7",\n'
                '    "severity": "CRITICAL",\n'
                '    "message": "Pressure anomaly detected",\n'
                '}'
            ),
            "why": 'Some feeds shout severities in ALL CAPS — your map must match.',
            "common_mistake": 'Use "CRITICAL", not "critical", for this source.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'CRITICAL', "message": 'Include CRITICAL severity'},
                {"type": 'contains', "value": 'message', "message": 'Include message'},
            ],
        },
        {
            "id": 'gp05',
            "title": 'Print source fields',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print(event["eventId"], event["locationName"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print(event["eventId"], event["locationName"])',
            "why": 'Printing source keys first prevents transform typos.',
            "common_mistake": 'KeyError usually means you typed facility instead of locationName.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print source fields'},
            ],
        },
        {
            "id": 'gp06',
            "title": 'Stub transform_event',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_event(event):\n'
                '    return {\n'
                '        "external_id": event["eventId"],\n'
                '        "site": event["locationName"],\n'
                '        "description": event["message"],\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_event(event):\n'
                '    return {\n'
                '        "external_id": event["eventId"],\n'
                '        "site": event["locationName"],\n'
                '        "description": event["message"],\n'
                '    }'
            ),
            "why": 'Map foreign names onto the ticket schema your destination expects.',
            "common_mistake": "Read eventId / locationName — don't invent facility.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_event', "message": 'Define transform_event()'},
                {"type": 'contains', "value": 'external_id', "message": 'Map to external_id'},
                {"type": 'contains', "value": 'locationName', "message": 'Read locationName from source'},
            ],
        },
        {
            "id": 'gp07',
            "title": 'Add PRIORITY_MAP',
            "instruction": (
                'Add this under what you already typed (above or near transform).\n'
                '\n'
                'EXAMPLE:\n'
                'PRIORITY_MAP = {\n'
                '    "CRITICAL": 1,\n'
                '    "HIGH": 2,\n'
                '    "MEDIUM": 3,\n'
                '}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'PRIORITY_MAP = {\n'
                '    "CRITICAL": 1,\n'
                '    "HIGH": 2,\n'
                '    "MEDIUM": 3,\n'
                '}'
            ),
            "why": 'A dict lookup is cleaner than a long if/elif for uppercase enums.',
            "common_mistake": 'Keys must match source casing exactly.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'PRIORITY_MAP', "message": 'Define PRIORITY_MAP'},
                {"type": 'contains', "value": 'CRITICAL', "message": 'Handle CRITICAL severity'},
            ],
        },
        {
            "id": 'gp08',
            "title": 'Include priority in transform',
            "instruction": (
                'Update transform_event to include priority from PRIORITY_MAP.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_event(event):\n'
                '    return {\n'
                '        "external_id": event["eventId"],\n'
                '        "site": event["locationName"],\n'
                '        "description": event["message"],\n'
                '        "priority": PRIORITY_MAP[event["severity"]],\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_event(event):\n'
                '    return {\n'
                '        "external_id": event["eventId"],\n'
                '        "site": event["locationName"],\n'
                '        "description": event["message"],\n'
                '        "priority": PRIORITY_MAP[event["severity"]],\n'
                '    }'
            ),
            "why": 'Destination tickets need priority as a number.',
            "common_mistake": "Use PRIORITY_MAP[event['severity']] — not a hardcoded 1 only (unless critical-only).",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'priority', "message": 'Include priority in output'},
                {"type": 'contains', "value": 'PRIORITY_MAP', "message": 'Use PRIORITY_MAP'},
                {"type": 'contains', "value": 'return', "message": 'Return transformed dict'},
            ],
        },
        {
            "id": 'gp09',
            "title": 'Call transform_event',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'ticket = transform_event(event)\n'
                'print(ticket)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'ticket = transform_event(event)\n'
                'print(ticket)'
            ),
            "why": 'Always print the ticket once while learning field maps.',
            "common_mistake": "Pass the event dict, not event['eventId'].",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'transform_event(', "message": 'Call transform_event'},
                {"type": 'contains', "value": 'print', "message": 'Print ticket'},
            ],
        },
        {
            "id": 'gp10',
            "title": 'Print external_id',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("external_id:", ticket["external_id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("external_id:", ticket["external_id"])',
            "why": 'external_id should be EVT-9001 from eventId.',
            "common_mistake": 'If you see eventId in the ticket, you forgot to rename.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'external_id', "message": 'Print external_id'},
            ],
        },
        {
            "id": 'gp11',
            "title": 'Print priority',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("priority:", ticket["priority"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("priority:", ticket["priority"])',
            "why": 'CRITICAL must map to priority 1.',
            "common_mistake": 'KeyError on PRIORITY_MAP usually means casing mismatch.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'priority', "message": 'Print priority'},
            ],
        },
        {
            "id": 'gp12',
            "title": 'Run — expect EVT-9001',
            "instruction": (
                'Click Analyze to run the offline transform.\n'
                '\n'
                'EXAMPLE:\n'
                'print("external_id:", ticket["external_id"])\n'
                'print("priority:", ticket["priority"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'print("external_id:", ticket["external_id"])\n'
                'print("priority:", ticket["priority"])'
            ),
            "why": 'Offline transforms should run with no network.',
            "common_mistake": 'If Priority fails, confirm CRITICAL is uppercase in the event.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_event', "message": 'Keep transform_event'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'EVT-9001', "message": 'Output shows EVT-9001'},
            ],
        },
        {
            "id": 'gp13',
            "title": 'Confirm priority 1',
            "instruction": (
                'Final check — priority should print as 1.\n'
                '\n'
                'EXAMPLE:\n'
                'print("priority:", ticket["priority"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("priority:", ticket["priority"])',
            "why": 'Seeing 1 confirms PRIORITY_MAP wiring.',
            "common_mistake": 'Printing the whole ticket is fine as long as priority 1 appears.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'EVT-9001', "message": 'Output still includes EVT-9001'},
                {"type": 'output_contains', "value": 'priority', "message": 'Output mentions priority'},
            ],
        },
    ],

    # ── python-type-along:hospital-feed ──
    "python-type-along:hospital-feed": [
        {
            "id": 'hf01',
            "title": 'Create the feed list',
            "instruction": (
                'Hospital feeder: start with a small in-memory feed list.\n'
                '\n'
                'EXAMPLE:\n'
                'feed = [\n'
                '    {"id": "H-1", "severity": "critical", "facility": "ER Wing", "message": "Power flicker"},\n'
                '    {"id": "H-2", "severity": "low", "facility": "Pharmacy", "message": "Printer offline"},\n'
                '    {"id": "H-3", "severity": "critical", "facility": "ICU", "message": "Monitor alarm"},\n'
                ']\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'feed = [\n'
                '    {"id": "H-1", "severity": "critical", "facility": "ER Wing", "message": "Power flicker"},\n'
                '    {"id": "H-2", "severity": "low", "facility": "Pharmacy", "message": "Printer offline"},\n'
                '    {"id": "H-3", "severity": "critical", "facility": "ICU", "message": "Monitor alarm"},\n'
                ']'
            ),
            "why": "A feed is just a list of event dicts you'll filter.",
            "common_mistake": 'Keep all three rows so you can see KEEP vs skip behavior.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'feed', "message": 'Create feed list'},
            ],
        },
        {
            "id": 'hf02',
            "title": 'Loop the feed',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for event in feed:\n'
                '    print(event["id"], event["severity"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for event in feed:\n'
                '    print(event["id"], event["severity"])'
            ),
            "why": 'Always print the raw feed once before filtering.',
            "common_mistake": 'Loop variable name can be event or item — stay consistent.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"for\s+\w+\s+in\s+feed", "message": 'Loop over feed'},
            ],
        },
        {
            "id": 'hf03',
            "title": 'Filter critical only',
            "instruction": (
                'Replace or add a filter loop — hospital SLA is critical only.\n'
                '\n'
                'EXAMPLE:\n'
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        print("KEEP", event["id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        print("KEEP", event["id"])'
            ),
            "why": 'Critical-only filters ignore low noise like printer offline.',
            "common_mistake": 'Compare to "critical" exactly (lowercase here).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical', "message": 'Filter critical severity'},
                {"type": 'contains', "value": 'if ', "message": 'Use if condition'},
                {"type": 'contains', "value": 'KEEP', "message": 'Print KEEP'},
            ],
        },
        {
            "id": 'hf04',
            "title": 'Print SKIP for others',
            "instruction": (
                'Update the loop so non-critical rows print SKIP.\n'
                '\n'
                'EXAMPLE:\n'
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        print("KEEP", event["id"])\n'
                '    else:\n'
                '        print("SKIP", event["id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        print("KEEP", event["id"])\n'
                '    else:\n'
                '        print("SKIP", event["id"])'
            ),
            "why": 'Explicit SKIP lines make audits easy during training.',
            "common_mistake": 'H-2 should SKIP; H-1 and H-3 should KEEP.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
                {"type": 'contains', "value": 'else', "message": 'Use else branch'},
            ],
        },
        {
            "id": 'hf05',
            "title": 'Define build_ticket',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def build_ticket(event):\n'
                '    return {\n'
                '        "external_id": event["id"],\n'
                '        "site": event["facility"],\n'
                '        "description": event["message"],\n'
                '        "priority": 1,\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def build_ticket(event):\n'
                '    return {\n'
                '        "external_id": event["id"],\n'
                '        "site": event["facility"],\n'
                '        "description": event["message"],\n'
                '        "priority": 1,\n'
                '    }'
            ),
            "why": 'Critical hospital events always map to priority 1.',
            "common_mistake": 'priority is the integer 1, not the string "1".',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'build_ticket', "message": 'Define build_ticket()'},
                {"type": 'contains', "value": 'description', "message": 'Include description'},
                {"type": 'contains', "value": 'priority', "message": 'Set priority'},
            ],
        },
        {
            "id": 'hf06',
            "title": 'Collect critical tickets',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'tickets = []\n'
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        tickets.append(build_ticket(event))\n'
                '    else:\n'
                '        print("SKIP", event["id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'tickets = []\n'
                'for event in feed:\n'
                '    if event["severity"] == "critical":\n'
                '        tickets.append(build_ticket(event))\n'
                '    else:\n'
                '        print("SKIP", event["id"])'
            ),
            "why": 'Appending transformed tickets prepares a batch to POST later.',
            "common_mistake": "Call build_ticket(event), not build_ticket(event['id']).",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'tickets', "message": 'Collect tickets list'},
                {"type": 'contains', "value": 'append', "message": 'Append built tickets'},
                {"type": 'contains', "value": 'build_ticket', "message": 'Use build_ticket'},
            ],
        },
        {
            "id": 'hf07',
            "title": 'Print ticket count',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("ticket count:", len(tickets))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("ticket count:", len(tickets))',
            "why": 'Expect 2 critical tickets from this feed.',
            "common_mistake": 'If count is 3, you forgot the critical filter.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'len(', "message": 'Use len()'},
                {"type": 'contains', "value": 'print', "message": 'Print count'},
            ],
        },
        {
            "id": 'hf08',
            "title": 'Print each external_id',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for t in tickets:\n'
                '    print("TICKET", t["external_id"], t["site"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for t in tickets:\n'
                '    print("TICKET", t["external_id"], t["site"])'
            ),
            "why": 'Listing ticket ids confirms transform + filter together.',
            "common_mistake": 'external_id should be H-1 and H-3 only.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'external_id', "message": 'Print external_id'},
                {"type": 'contains', "value": 'TICKET', "message": 'Label TICKET lines'},
            ],
        },
        {
            "id": 'hf09',
            "title": 'Sanity-check priority',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for t in tickets:\n'
                '    print(t["external_id"], "priority=", t["priority"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for t in tickets:\n'
                '    print(t["external_id"], "priority=", t["priority"])'
            ),
            "why": 'Every critical hospital ticket should show priority 1.',
            "common_mistake": 'If priority is missing, rebuild the dict in build_ticket.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'priority', "message": 'Print priority'},
            ],
        },
        {
            "id": 'hf10',
            "title": 'Keep SKIP for H-2',
            "instruction": (
                'Ensure SKIP still appears for non-critical (your loop else is best).\n'
                '\n'
                'EXAMPLE:\n'
                'print("SKIP", "H-2")  # low severity pharmacy noise\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("SKIP", "H-2")  # low severity pharmacy noise',
            "why": 'Ops trainers look for SKIP lines to trust the filter.',
            "common_mistake": "Don't delete the else: SKIP branch when adding tickets.append.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SKIP', "message": 'Keep SKIP output'},
            ],
        },
        {
            "id": 'hf11',
            "title": 'Run — expect SKIP',
            "instruction": (
                'Keep your filter loop, SKIP prints, and ticket list. Click Analyze to run.\n'
                '\n'
                'EXAMPLE:\n'
                'print("ticket count:", len(tickets))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("ticket count:", len(tickets))',
            "why": 'Running proves KEEP/SKIP logic without any HTTP yet.',
            "common_mistake": 'NameError usually means tickets = [] is missing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'build_ticket', "message": 'Keep build_ticket'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output shows SKIP'},
            ],
        },
        {
            "id": 'hf12',
            "title": 'Confirm H-1 and H-3',
            "instruction": (
                'Final run should list TICKET H-1 and H-3. Click Analyze.\n'
                '\n'
                'EXAMPLE:\n'
                'for t in tickets:\n'
                '    print("TICKET", t["external_id"], t["site"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for t in tickets:\n'
                '    print("TICKET", t["external_id"], t["site"])'
            ),
            "why": 'Two critical events → two tickets after filtering.',
            "common_mistake": 'H-2 must not appear as a TICKET line.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'H-1', "message": 'Output includes H-1'},
                {"type": 'output_contains', "value": 'H-3', "message": 'Output includes H-3'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output still shows SKIP'},
            ],
        },
    ],

    # ── get-filter:critical-high ──
    "get-filter:critical-high": [
        {
            "id": 'g01',
            "title": 'Import os',
            "instruction": (
                'Start with env + requests setup for the monitoring API.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'os.getenv reads SOURCE_API_KEY from .env.',
            "common_mistake": 'Put imports at the top.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'g02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": "You'll GET /v1/incidents next.",
            "common_mistake": 'Spelling is requests.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'g03',
            "title": 'Import + call load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'load_dotenv must be called before getenv.',
            "common_mistake": "Don't forget the call parentheses.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv()'},
            ],
        },
        {
            "id": 'g04',
            "title": 'Load SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Bearer auth uses SOURCE_API_KEY for the monitoring API.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded API keys'},
            ],
        },
        {
            "id": 'g05',
            "title": 'Load SOURCE_API_URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")',
            "why": 'Default the mock monitoring base URL to port 5001.',
            "common_mistake": '5002 is destination — wrong for GET incidents.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Load SOURCE_API_URL'},
                {"type": 'contains', "value": '5001', "message": 'Port 5001 default'},
            ],
        },
        {
            "id": 'g06',
            "title": 'GET open incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')'
            ),
            "why": "Pull open incidents first; you'll filter severity in Python next.",
            "common_mistake": 'Include Bearer auth and status=open.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.get', "message": 'GET request'},
                {"type": 'regex', "pattern": r"Bearer", "message": 'Bearer auth'},
                {"type": 'contains', "value": 'status', "message": 'Filter open status'},
            ],
        },
        {
            "id": 'g07',
            "title": 'raise_for_status',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response.raise_for_status()',
            "why": 'Fail fast on 401/500 before filtering.',
            "common_mistake": 'Call it on response, not on json().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'Check status'},
            ],
        },
        {
            "id": 'g08',
            "title": 'Read incidents list',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'incidents = response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'incidents = response.json()["data"]',
            "why": 'The list endpoint wraps rows under data.',
            "common_mistake": "Don't iterate the envelope dict by mistake.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'json()', "message": 'Parse JSON'},
                {"type": 'contains', "value": '["data"]', "message": 'Read data list'},
            ],
        },
        {
            "id": 'g09',
            "title": 'Define SYNC_SEVERITIES set',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SYNC_SEVERITIES = {"critical", "high"}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = {"critical", "high"}',
            "why": 'A set makes `in` checks fast and intention clear.',
            "common_mistake": 'Include both critical and high.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SYNC_SEVERITIES', "message": 'Define SYNC_SEVERITIES'},
                {"type": 'contains', "value": 'critical', "message": 'Include critical'},
                {"type": 'contains', "value": 'high', "message": 'Include high'},
            ],
        },
        {
            "id": 'g10',
            "title": 'Build filtered list',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'filtered = []\n'
                'for inc in incidents:\n'
                '    if inc["severity"] in SYNC_SEVERITIES:\n'
                '        filtered.append(inc)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'filtered = []\n'
                'for inc in incidents:\n'
                '    if inc["severity"] in SYNC_SEVERITIES:\n'
                '        filtered.append(inc)'
            ),
            "why": "Client-side filtering is fine when the API can't combine filters.",
            "common_mistake": 'Append the whole incident dict, not just the id.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'filtered', "message": 'Create filtered list'},
                {"type": 'contains', "value": 'append', "message": 'Append matches'},
            ],
        },
        {
            "id": 'g11',
            "title": 'Print filtered rows',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in filtered:\n'
                '    print(inc["id"], inc["severity"], inc["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in filtered:\n'
                '    print(inc["id"], inc["severity"], inc["facility"])'
            ),
            "why": 'Printing severity proves the filter kept the right rows.',
            "common_mistake": 'Loop filtered, not the original incidents list.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'regex', "pattern": r"for\s+\w+\s+in\s+filtered", "message": 'Loop filtered'},
                {"type": 'contains', "value": 'print', "message": 'Print results'},
            ],
        },
        {
            "id": 'g12',
            "title": 'Print filtered count',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Filtered count:", len(filtered))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Filtered count:", len(filtered))',
            "why": 'A count is the fastest sanity check for filter logic.',
            "common_mistake": 'Use len(filtered), not len(incidents).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'len(', "message": 'Print count with len()'},
                {"type": 'contains', "value": 'Filtered count', "message": 'Label Filtered count'},
            ],
        },
        {
            "id": 'g13',
            "title": 'Run against mock API',
            "instruction": (
                'Mock APIs + .env required. Click Analyze to run.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Filtered count:", len(filtered))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Filtered count:", len(filtered))',
            "why": 'Live data should include INC-38192 as critical water-plant.',
            "common_mistake": 'Empty filtered usually means wrong severity spelling.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical', "message": 'Keep critical'},
                {"type": 'contains', "value": 'high', "message": 'Keep high'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'INC-38192', "message": 'Output includes INC-38192'},
            ],
        },
        {
            "id": 'g14',
            "title": 'Confirm critical appears',
            "instruction": (
                'Final check — critical/high rows should print.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in filtered:\n'
                '    print(inc["id"], inc["severity"], inc["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in filtered:\n'
                '    print(inc["id"], inc["severity"], inc["facility"])'
            ),
            "why": 'Seeing critical in output confirms the allow-list works.',
            "common_mistake": 'If only medium prints, your SYNC_SEVERITIES is wrong.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'critical', "message": 'Output includes critical'},
                {"type": 'output_contains', "value": 'Filtered count', "message": 'Output includes Filtered count'},
            ],
        },
    ],

    # ── get-filter:api-filter ──
    "get-filter:api-filter": [
        {
            "id": 'gf01',
            "title": 'Import os',
            "instruction": (
                'Start with env + requests setup for the monitoring API.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'os.getenv reads SOURCE_API_KEY from .env.',
            "common_mistake": 'Put imports at the top.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'gf02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": "You'll GET /v1/incidents next.",
            "common_mistake": 'Spelling is requests.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'gf03',
            "title": 'Import + call load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'load_dotenv must be called before getenv.',
            "common_mistake": "Don't forget the call parentheses.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv()'},
            ],
        },
        {
            "id": 'gf04',
            "title": 'Load SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Bearer auth uses SOURCE_API_KEY for the monitoring API.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded API keys'},
            ],
        },
        {
            "id": 'gf05',
            "title": 'Load SOURCE_API_URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")',
            "why": 'Default the mock monitoring base URL to port 5001.',
            "common_mistake": '5002 is destination — wrong for GET incidents.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Load SOURCE_API_URL'},
                {"type": 'contains', "value": '5001', "message": 'Port 5001 default'},
            ],
        },
        {
            "id": 'gf06',
            "title": 'GET with severity param',
            "instruction": (
                'Add this under what you already typed. Let the API filter severity.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open", "severity": "critical"},\n'
                '    timeout=30,\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open", "severity": "critical"},\n'
                '    timeout=30,\n'
                ')'
            ),
            "why": 'Server-side filters cut payload size before Python runs.',
            "common_mistake": 'Put both status and severity inside params.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'params', "message": 'Use params dict'},
                {"type": 'contains', "value": 'severity', "message": 'Pass severity param'},
                {"type": 'contains', "value": 'critical', "message": 'Filter critical at API'},
            ],
        },
        {
            "id": 'gf07',
            "title": 'raise_for_status',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'response.raise_for_status()',
            "why": 'Still check HTTP errors even when params look right.',
            "common_mistake": '401 means key/header issues, not filter issues.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'Check status'},
            ],
        },
        {
            "id": 'gf08',
            "title": 'Parse data list',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'incidents = response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'incidents = response.json()["data"]',
            "why": 'Even with API filters, the envelope still uses data.',
            "common_mistake": "Don't assume a bare list at the top level.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'json()', "message": 'Parse JSON'},
            ],
        },
        {
            "id": 'gf09',
            "title": 'Print count',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Count:", len(incidents))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Count:", len(incidents))',
            "why": 'Count should be smaller than all-open incidents.',
            "common_mistake": 'Use len(incidents).',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print incidents'},
                {"type": 'contains', "value": 'len(', "message": 'Print count with len()'},
            ],
        },
        {
            "id": 'gf10',
            "title": 'Print each id',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in incidents:\n'
                '    print(inc["id"], inc["severity"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in incidents:\n'
                '    print(inc["id"], inc["severity"])'
            ),
            "why": 'Every printed severity should be critical if the API filter worked.',
            "common_mistake": "If you see high/medium, severity param didn't apply.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'for ', "message": 'Loop incidents'},
                {"type": 'contains', "value": 'print', "message": 'Print each row'},
            ],
        },
        {
            "id": 'gf11',
            "title": 'Assert-style note in print',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("API filtered to critical only")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("API filtered to critical only")',
            "why": 'A label in stdout helps when you compare exercises A vs B.',
            "common_mistake": 'Keep the exact phrase for the output check.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical only', "message": 'Label critical only'},
            ],
        },
        {
            "id": 'gf12',
            "title": 'Run mock GET',
            "instruction": (
                'Click Analyze — mock API must be up.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Count:", len(incidents))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Count:", len(incidents))',
            "why": 'Critical open incidents include INC-38192.',
            "common_mistake": 'Connection errors mean start the mock APIs.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'severity', "message": 'Keep severity param'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'Count:', "message": 'Output shows Count:'},
            ],
        },
        {
            "id": 'gf13',
            "title": 'Confirm INC-38192',
            "instruction": (
                'Final run should list INC-38192 among critical results.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in incidents:\n'
                '    print(inc["id"], inc["severity"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in incidents:\n'
                '    print(inc["id"], inc["severity"])'
            ),
            "why": 'INC-38192 is a known critical open incident in the mock data.',
            "common_mistake": 'Missing id → wrong auth or filters.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-38192', "message": 'Output includes INC-38192'},
                {"type": 'output_contains', "value": 'critical', "message": 'Output includes critical'},
            ],
        },
    ],

    # ── get-filter:facility-search ──
    "get-filter:facility-search": [
        {
            "id": 'gs01',
            "title": 'Import os',
            "instruction": (
                'Start with env + requests setup for the monitoring API.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'os.getenv reads SOURCE_API_KEY from .env.',
            "common_mistake": 'Put imports at the top.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'gs02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": "You'll GET /v1/incidents next.",
            "common_mistake": 'Spelling is requests.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'gs03',
            "title": 'Import + call load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'load_dotenv must be called before getenv.',
            "common_mistake": "Don't forget the call parentheses.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv()'},
            ],
        },
        {
            "id": 'gs04',
            "title": 'Load SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Bearer auth uses SOURCE_API_KEY for the monitoring API.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load SOURCE_API_KEY'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded API keys'},
            ],
        },
        {
            "id": 'gs05',
            "title": 'Load SOURCE_API_URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")',
            "why": 'Default the mock monitoring base URL to port 5001.',
            "common_mistake": '5002 is destination — wrong for GET incidents.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Load SOURCE_API_URL'},
                {"type": 'contains', "value": '5001', "message": 'Port 5001 default'},
            ],
        },
        {
            "id": 'gs06',
            "title": 'GET open incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    f"{SOURCE_API_URL}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '    params={"status": "open"},\n'
                '    timeout=30,\n'
                ')'
            ),
            "why": 'Facility keyword search is easiest client-side on open incidents.',
            "common_mistake": 'Auth + status=open first.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.get', "message": 'GET incidents'},
            ],
        },
        {
            "id": 'gs07',
            "title": 'raise + parse',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'response.raise_for_status()\n'
                'incidents = response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'response.raise_for_status()\n'
                'incidents = response.json()["data"]'
            ),
            "why": 'Parse only after confirming HTTP success.',
            "common_mistake": 'Remember the data key.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'raise_for_status', "message": 'raise_for_status'},
                {"type": 'contains', "value": '["data"]', "message": 'Read data'},
            ],
        },
        {
            "id": 'gs08',
            "title": 'Start matches list',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'matches = []\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'matches = []',
            "why": 'Collect facility keyword hits in a new list.',
            "common_mistake": "Don't reuse the name incidents for the filtered list.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'matches', "message": 'Create matches list'},
            ],
        },
        {
            "id": 'gs09',
            "title": 'Filter Water facilities',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in incidents:\n'
                '    if "Water" in inc["facility"]:\n'
                '        matches.append(inc)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in incidents:\n'
                '    if "Water" in inc["facility"]:\n'
                '        matches.append(inc)'
            ),
            "why": 'Substring checks find Water Treatment Plant rows.',
            "common_mistake": 'Use "Water" in facility — case matters.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'facility', "message": 'Check facility field'},
                {"type": 'contains', "value": 'Water', "message": 'Filter for Water Treatment facilities'},
                {"type": 'contains', "value": 'if ', "message": 'Use if to filter'},
            ],
        },
        {
            "id": 'gs10',
            "title": 'Print match count',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Matches:", len(matches))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Matches:", len(matches))',
            "why": 'Mock data has multiple Water Treatment Plant 4 incidents.',
            "common_mistake": 'Zero matches → typo in Water or facility key.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print matches'},
                {"type": 'contains', "value": 'Matches:', "message": 'Label Matches:'},
            ],
        },
        {
            "id": 'gs11',
            "title": 'Print each facility',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in matches:\n'
                '    print(inc["id"], inc["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in matches:\n'
                '    print(inc["id"], inc["facility"])'
            ),
            "why": 'Reading facility names confirms the keyword filter.',
            "common_mistake": 'Loop matches, not incidents.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'facility', "message": 'Print facility names'},
            ],
        },
        {
            "id": 'gs12',
            "title": 'Run facility search',
            "instruction": (
                'Click Analyze with mock APIs running.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Matches:", len(matches))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Matches:", len(matches))',
            "why": 'You should see Water Treatment Plant 4 in the output.',
            "common_mistake": "Auth failures won't reach the filter loop.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'Water', "message": 'Keep Water filter'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'Matches:', "message": 'Output shows Matches:'},
            ],
        },
        {
            "id": 'gs13',
            "title": 'Confirm Water Treatment text',
            "instruction": (
                'Final output should include Water Treatment Plant 4.\n'
                '\n'
                'EXAMPLE:\n'
                'for inc in matches:\n'
                '    print(inc["id"], inc["facility"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'for inc in matches:\n'
                '    print(inc["id"], inc["facility"])'
            ),
            "why": 'Known mock facility string proves the keyword search.',
            "common_mistake": 'If you filtered Wastewater only, broaden to Water.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'Water Treatment', "message": 'Output includes Water Treatment'},
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes incident ids'},
            ],
        },
    ],

    # ── sync-systems:sync-all-urgent ──
    "sync-systems:sync-all-urgent": [
        {
            "id": 's01',
            "title": 'Import os',
            "instruction": (
                'Sync needs source + destination keys from .env.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'Both APIs authenticate with env-based keys.',
            "common_mistake": 'Start with import os.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 's02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": 'GET incidents and POST tickets with requests.',
            "common_mistake": 'Keep the plural spelling.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 's03',
            "title": 'load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Load .env before reading either API key.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv'},
            ],
        },
        {
            "id": 's04',
            "title": 'SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Monitoring/source API uses SOURCE_API_KEY.',
            "common_mistake": "Don't hardcode.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Source key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 's05',
            "title": 'DESTINATION_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")',
            "why": 'Ticketing/destination API uses DESTINATION_API_KEY.',
            "common_mistake": 'Using SOURCE_API_KEY on POST will 401.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'DESTINATION_API_KEY', "message": 'Dest key'},
            ],
        },
        {
            "id": 's06',
            "title": 'URLs',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")'
            ),
            "why": '5001 source, 5002 destination — keep them straight.',
            "common_mistake": 'Swapping ports is a classic sync bug.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Source URL'},
                {"type": 'contains', "value": 'DESTINATION_API_URL', "message": 'Dest URL'},
                {"type": 'contains', "value": '5002', "message": 'Destination port 5002'},
            ],
        },
        {
            "id": 's07',
            "title": 'SYNC_SEVERITIES',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SYNC_SEVERITIES = {"critical", "high"}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = {"critical", "high"}',
            "why": 'Urgent sync includes critical and high.',
            "common_mistake": 'Use a set/list you can test with `in`.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SYNC_SEVERITIES', "message": 'Define SYNC_SEVERITIES'},
                {"type": 'contains', "value": 'critical', "message": 'Include critical'},
                {"type": 'contains', "value": 'high', "message": 'Include high'},
            ],
        },
        {
            "id": 's08',
            "title": 'transform_incident',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(incident):\n'
                '    priority_map = {\n'
                '        "critical": 1,\n'
                '        "high": 2,\n'
                '        "medium": 3,\n'
                '        "low": 4,\n'
                '    }\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(incident):\n'
                '    priority_map = {\n'
                '        "critical": 1,\n'
                '        "high": 2,\n'
                '        "medium": 3,\n'
                '        "low": 4,\n'
                '    }\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                '    }'
            ),
            "why": 'Destination tickets need external_id/site/description/priority.',
            "common_mistake": 'Map id → external_id before POSTing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_incident', "message": 'Define transform_incident()'},
                {"type": 'contains', "value": 'external_id', "message": 'Map external_id'},
            ],
        },
        {
            "id": 's09',
            "title": 'fetch_open_incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]'
            ),
            "why": 'Wrap the GET so main() stays readable.',
            "common_mistake": 'Return the data list, not the full response.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_open_incidents', "message": 'Define fetch function'},
            ],
        },
        {
            "id": 's10',
            "title": 'create_ticket',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()'
            ),
            "why": 'POST uses DESTINATION_API_KEY and json=payload.',
            "common_mistake": "Don't send the source Bearer key to the ticket API.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'create_ticket', "message": 'Define create_ticket()'},
                {"type": 'contains', "value": 'requests.post', "message": 'POST tickets'},
                {"type": 'contains', "value": 'DESTINATION_API_KEY', "message": 'Use destination key'},
            ],
        },
        {
            "id": 's11',
            "title": 'main loop with 409 handling',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in SYNC_SEVERITIES:\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(ticket)\n'
                '            print(f"CREATED {incident[\'id"]} -> {created.get(\'id\', created)}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id"]} — already exists")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in SYNC_SEVERITIES:\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(ticket)\n'
                '            print(f"CREATED {incident[\'id"]} -> {created.get(\'id\', created)}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']} — already exists")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": '409 conflict means the ticket already exists — treat as SKIP, not crash.',
            "common_mistake": 'Print SKIP for filtered severities and duplicates.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'main', "message": 'Define main()'},
                {"type": 'contains', "value": '409', "message": 'Handle 409 conflict'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
            ],
        },
        {
            "id": 's12',
            "title": 'Run the sync',
            "instruction": (
                'Both mock APIs + .env required. Click Analyze to execute main().\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'A real sync run should print SKIP and/or CREATED lines with incident ids.',
            "common_mistake": 'If nothing runs, check the __main__ guard.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '__main__', "message": 'Main guard'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output includes SKIP'},
            ],
        },
        {
            "id": 's13',
            "title": 'Confirm an incident id in output',
            "instruction": (
                'Re-run is fine — look for INC- ids in SKIP/CREATED lines.\n'
                '\n'
                'EXAMPLE:\n'
                'main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'Incident ids in stdout prove you looped real mock data.',
            "common_mistake": "Empty output means main() wasn't called.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes an INC- id'},
            ],
        },
    ],

    # ── sync-systems:sync-critical-only ──
    "sync-systems:sync-critical-only": [
        {
            "id": 'sc01',
            "title": 'Import os',
            "instruction": (
                'Sync needs source + destination keys from .env.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'Both APIs authenticate with env-based keys.',
            "common_mistake": 'Start with import os.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'sc02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": 'GET incidents and POST tickets with requests.',
            "common_mistake": 'Keep the plural spelling.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'sc03',
            "title": 'load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Load .env before reading either API key.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv'},
            ],
        },
        {
            "id": 'sc04',
            "title": 'SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Monitoring/source API uses SOURCE_API_KEY.',
            "common_mistake": "Don't hardcode.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Source key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'sc05',
            "title": 'DESTINATION_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")',
            "why": 'Ticketing/destination API uses DESTINATION_API_KEY.',
            "common_mistake": 'Using SOURCE_API_KEY on POST will 401.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'DESTINATION_API_KEY', "message": 'Dest key'},
            ],
        },
        {
            "id": 'sc06',
            "title": 'URLs',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")'
            ),
            "why": '5001 source, 5002 destination — keep them straight.',
            "common_mistake": 'Swapping ports is a classic sync bug.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Source URL'},
                {"type": 'contains', "value": 'DESTINATION_API_URL', "message": 'Dest URL'},
                {"type": 'contains', "value": '5002', "message": 'Destination port 5002'},
            ],
        },
        {
            "id": 'sc07',
            "title": 'fetch_open_incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]'
            ),
            "why": 'Fetch open incidents; filter critical in Python next.',
            "common_mistake": 'Use SOURCE_API_KEY for GET.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_open_incidents', "message": 'Define fetch_open_incidents'},
            ],
        },
        {
            "id": 'sc08',
            "title": 'transform critical → priority 1',
            "instruction": (
                'Add this under what you already typed. Critical-only → always priority 1.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1,\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1,\n'
                '    }'
            ),
            "why": 'Hospital SLA tickets from critical alerts are priority 1.',
            "common_mistake": "Don't include a high branch in this exercise.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_incident', "message": 'transform_incident'},
                {"type": 'contains', "value": 'priority', "message": 'Set priority'},
            ],
        },
        {
            "id": 'sc09',
            "title": 'create_ticket POST',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()'
            ),
            "why": 'POST tickets with the destination Bearer key.',
            "common_mistake": 'json=payload sends the transformed dict.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'requests.post', "message": 'POST to destination'},
                {"type": 'contains', "value": 'transform', "message": 'Transform before POST'},
            ],
        },
        {
            "id": 'sc10',
            "title": 'Critical-only main loop',
            "instruction": (
                'Add this under what you already typed. Critical only — not high.\n'
                '\n'
                'EXAMPLE:\n'
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] != "critical":\n'
                '            print(f"SKIP {incident[\'id"]} ({incident[\'severity\']})")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(transform_incident(incident))\n'
                '            print(f"CREATED {incident[\'id\']} ticket={created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']} — duplicate")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] != "critical":\n'
                '            print(f"SKIP {incident[\'id\']} ({incident[\'severity\']})")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(transform_incident(incident))\n'
                '            print(f"CREATED {incident[\'id\']} ticket={created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']} — duplicate")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'Hospital SLA: only severity == critical creates tickets.',
            "common_mistake": 'Do not add high to the allow path in this exercise.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical', "message": 'Filter critical only'},
                {"type": 'contains', "value": '409', "message": 'Handle duplicates'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
                {"type": 'not_contains', "value": 'SYNC_SEVERITIES', "message": 'No SYNC_SEVERITIES allow-list — critical equality only'},
            ],
        },
        {
            "id": 'sc11',
            "title": 'Run critical sync',
            "instruction": (
                'Click Analyze with both mocks running.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'You should see SKIP for non-critical rows.',
            "common_mistake": 'Missing DESTINATION_API_KEY causes POST failures.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output includes SKIP'},
            ],
        },
        {
            "id": 'sc12',
            "title": 'Confirm INC ids',
            "instruction": (
                'Output should mention INC- ids for skipped or created rows.\n'
                '\n'
                'EXAMPLE:\n'
                'main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'Ids prove the loop hit mock incidents.',
            "common_mistake": 'No INC- text usually means print statements missing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes INC- id'},
            ],
        },
    ],

    # ── sync-systems:sync-with-stats ──
    "sync-systems:sync-with-stats": [
        {
            "id": 'ss01',
            "title": 'Import os',
            "instruction": (
                'Sync needs source + destination keys from .env.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'Both APIs authenticate with env-based keys.',
            "common_mistake": 'Start with import os.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'ss02',
            "title": 'Import requests',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import requests',
            "why": 'GET incidents and POST tickets with requests.',
            "common_mistake": 'Keep the plural spelling.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 'ss03',
            "title": 'load_dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Load .env before reading either API key.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'load_dotenv', "message": 'Call load_dotenv'},
            ],
        },
        {
            "id": 'ss04',
            "title": 'SOURCE_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")',
            "why": 'Monitoring/source API uses SOURCE_API_KEY.',
            "common_mistake": "Don't hardcode.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Source key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'ss05',
            "title": 'DESTINATION_API_KEY',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")',
            "why": 'Ticketing/destination API uses DESTINATION_API_KEY.',
            "common_mistake": 'Using SOURCE_API_KEY on POST will 401.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'DESTINATION_API_KEY', "message": 'Dest key'},
            ],
        },
        {
            "id": 'ss06',
            "title": 'URLs',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")'
            ),
            "why": '5001 source, 5002 destination — keep them straight.',
            "common_mistake": 'Swapping ports is a classic sync bug.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_URL', "message": 'Source URL'},
                {"type": 'contains', "value": 'DESTINATION_API_URL', "message": 'Dest URL'},
                {"type": 'contains', "value": '5002', "message": 'Destination port 5002'},
            ],
        },
        {
            "id": 'ss07',
            "title": 'SYNC_SEVERITIES',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SYNC_SEVERITIES = {"critical", "high"}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = {"critical", "high"}',
            "why": 'Urgent sync includes critical and high.',
            "common_mistake": 'Use a set/list you can test with `in`.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SYNC_SEVERITIES', "message": 'Define SYNC_SEVERITIES'},
                {"type": 'contains', "value": 'critical', "message": 'Include critical'},
                {"type": 'contains', "value": 'high', "message": 'Include high'},
            ],
        },
        {
            "id": 'ss08',
            "title": 'Stats dict',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'stats = {"created": 0, "skipped": 0, "failed": 0}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'stats = {"created": 0, "skipped": 0, "failed": 0}',
            "why": 'Counters make sync runs measurable for ops handoff.',
            "common_mistake": 'Include created, skipped, and failed keys.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'created', "message": 'Track created count'},
                {"type": 'contains', "value": 'skipped', "message": 'Track skipped count'},
                {"type": 'contains', "value": 'failed', "message": 'Track failed count'},
            ],
        },
        {
            "id": 'ss09',
            "title": 'fetch_open_incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_open_incidents():\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]'
            ),
            "why": 'Fetch once, then update stats while syncing.',
            "common_mistake": 'Return data list.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_open_incidents', "message": 'Fetch function'},
            ],
        },
        {
            "id": 'ss10',
            "title": 'transform + create_ticket',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1 if incident["severity"] == "critical" else 2,\n'
                '    }\n'
                '\n'
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1 if incident["severity"] == "critical" else 2,\n'
                '    }\n'
                '\n'
                'def create_ticket(payload):\n'
                '    response = requests.post(\n'
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                '        json=payload,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()'
            ),
            "why": 'Transform then POST — stats wrap the try/except around create.',
            "common_mistake": 'Use DESTINATION_API_KEY on POST.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'create_ticket', "message": 'Create ticket function'},
            ],
        },
        {
            "id": 'ss11',
            "title": 'Main with stats increments',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in SYNC_SEVERITIES:\n'
                '            stats["skipped"] += 1\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(transform_incident(incident))\n'
                '            stats["created"] += 1\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                stats["skipped"] += 1\n'
                '                print(f"SKIP {incident[\'id\']} duplicate")\n'
                '            else:\n'
                '                stats["failed"] += 1\n'
                '                print(f"FAIL {incident[\'id\']}")\n'
                '    print(f"created={stats[\'created\']} skipped={stats[\'skipped\']} failed={stats[\'failed\']}")\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def main():\n'
                '    incidents = fetch_open_incidents()\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in SYNC_SEVERITIES:\n'
                '            stats["skipped"] += 1\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(transform_incident(incident))\n'
                '            stats["created"] += 1\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                stats["skipped"] += 1\n'
                '                print(f"SKIP {incident[\'id\']} duplicate")\n'
                '            else:\n'
                '                stats["failed"] += 1\n'
                '                print(f"FAIL {incident[\'id\']}")\n'
                '    print(f"created={stats[\'created\']} skipped={stats[\'skipped\']} failed={stats[\'failed\']}")\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'Print a one-line summary after the loop for operators.',
            "common_mistake": 'Increment skipped on filter misses and on 409.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print summary'},
                {"type": 'contains', "value": '409', "message": 'Increment skipped on 409'},
                {"type": 'contains', "value": 'created=', "message": 'Print created= summary'},
            ],
        },
        {
            "id": 'ss12',
            "title": 'Run with stats',
            "instruction": (
                'Click Analyze — expect created=/skipped= summary.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'Summary line proves counters updated.',
            "common_mistake": 'failed should stay 0 on a healthy mock run.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'created=', "message": 'Output includes created='},
                {"type": 'output_contains', "value": 'skipped=', "message": 'Output includes skipped='},
            ],
        },
        {
            "id": 'ss13',
            "title": 'Confirm SKIP lines',
            "instruction": (
                'Non-urgent severities should print SKIP with an id.\n'
                '\n'
                'EXAMPLE:\n'
                'main()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    main()'
            ),
            "why": 'SKIP lines show the filter is working alongside counters.',
            "common_mistake": "If skipped=0 always, medium/low rows aren't being counted.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output includes SKIP'},
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes INC- id'},
            ],
        },
    ],

    # ── reliability:full-reliability ──
    "reliability:full-reliability": [
        {
            "id": 'r01',
            "title": 'Import os',
            "instruction": (
                'Reliability lesson: pagination + safe error handling.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'Load SOURCE_API_KEY from the environment.',
            "common_mistake": 'Start with import os.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'r02',
            "title": 'Import requests + dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Same setup as other API lessons.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": 'load_dotenv', "message": 'load_dotenv'},
            ],
        },
        {
            "id": 'r03',
            "title": 'Load key + URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "why": 'Pagination still needs auth against the monitoring API.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load API key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'r04',
            "title": 'HEADERS constant',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'HEADERS = {"Authorization": f"Bearer {SOURCE_API_KEY}"}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'HEADERS = {"Authorization": f"Bearer {SOURCE_API_KEY}"}',
            "why": 'Reuse one headers dict across paginated calls.',
            "common_mistake": 'Bearer + SOURCE_API_KEY.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'HEADERS', "message": 'Define HEADERS'},
                {"type": 'regex', "pattern": r"Bearer", "message": 'Bearer auth'},
            ],
        },
        {
            "id": 'r05',
            "title": 'fetch_all_incidents stub',
            "instruction": (
                'Add a function stub under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_all_incidents(limit=3):\n'
                '    all_records = []\n'
                '    page = 1\n'
                '    return all_records\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_all_incidents(limit=3):\n'
                '    all_records = []\n'
                '    page = 1\n'
                '    return all_records'
            ),
            "why": 'Small limit forces multiple pages on the mock API.',
            "common_mistake": 'Initialize all_records and page before the loop.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_all_incidents', "message": 'Define fetch_all_incidents()'},
                {"type": 'contains', "value": 'page', "message": 'Track page'},
            ],
        },
        {
            "id": 'r06',
            "title": 'Pagination while loop',
            "instruction": (
                'Replace the stub with a full pagination loop.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_all_incidents(limit=3):\n'
                '    all_records = []\n'
                '    page = 1\n'
                '    while True:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents",\n'
                '            headers=HEADERS,\n'
                '            params={"page": page, "limit": limit},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        body = response.json()\n'
                '        all_records.extend(body["data"])\n'
                '        if not body["pagination"]["has_more"]:\n'
                '            break\n'
                '        page += 1\n'
                '    return all_records\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_all_incidents(limit=3):\n'
                '    all_records = []\n'
                '    page = 1\n'
                '    while True:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents",\n'
                '            headers=HEADERS,\n'
                '            params={"page": page, "limit": limit},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        body = response.json()\n'
                '        all_records.extend(body["data"])\n'
                '        if not body["pagination"]["has_more"]:\n'
                '            break\n'
                '        page += 1\n'
                '    return all_records'
            ),
            "why": 'Stop when pagination.has_more is false.',
            "common_mistake": 'Use extend, not append of the whole list object incorrectly.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'has_more', "message": 'Check has_more'},
                {"type": 'contains', "value": 'while', "message": 'Use while loop'},
                {"type": 'contains', "value": 'extend', "message": 'Accumulate with extend'},
            ],
        },
        {
            "id": 'r07',
            "title": 'safe_get_incident',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers=HEADERS,\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        print(f"Timeout fetching {incident_id}")\n'
                '        return None\n'
                '    except requests.HTTPError as e:\n'
                '        print(f"HTTP error: {e}")\n'
                '        return None\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers=HEADERS,\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        print(f"Timeout fetching {incident_id}")\n'
                '        return None\n'
                '    except requests.HTTPError as e:\n'
                '        print(f"HTTP error: {e}")\n'
                '        return None'
            ),
            "why": 'Safe helpers return None instead of crashing the whole job.',
            "common_mistake": 'Catch Timeout and HTTPError at minimum.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'safe_get_incident', "message": 'Define safe_get_incident()'},
                {"type": 'contains', "value": 'HTTPError', "message": 'Catch HTTPError'},
                {"type": 'contains', "value": 'Timeout', "message": 'Catch Timeout'},
            ],
        },
        {
            "id": 'r08',
            "title": 'Main: paginate',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    all_incidents = fetch_all_incidents(limit=3)\n'
                '    print(f"Paginated fetch: {len(all_incidents)} total incidents")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    all_incidents = fetch_all_incidents(limit=3)\n'
                '    print(f"Paginated fetch: {len(all_incidents)} total incidents")'
            ),
            "why": 'Print totals so you know pagination gathered every page.',
            "common_mistake": 'limit=3 is intentional for demos.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '__main__', "message": 'Main block'},
                {"type": 'contains', "value": 'Paginated fetch', "message": 'Print Paginated fetch'},
            ],
        },
        {
            "id": 'r09',
            "title": 'Main: safe get existing',
            "instruction": (
                'Add these lines inside the __main__ block.\n'
                '\n'
                'EXAMPLE:\n'
                'found = safe_get_incident("INC-38192")\n'
                '    print(f"Found: {found[\'id\'] if found else None}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '    found = safe_get_incident("INC-38192")\n'
                '    print(f"Found: {found[\'id\'] if found else None}")'
            ),
            "why": 'INC-38192 exists in mock data and should return a dict.',
            "common_mistake": 'Indent under __main__.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-38192', "message": 'Test existing ID'},
                {"type": 'contains', "value": 'safe_get_incident', "message": 'Call safe_get_incident'},
            ],
        },
        {
            "id": 'r10',
            "title": 'Main: safe get missing',
            "instruction": (
                'Add these lines inside the __main__ block.\n'
                '\n'
                'EXAMPLE:\n'
                'missing = safe_get_incident("INC-99999")\n'
                '    print(f"Missing: {missing}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '    missing = safe_get_incident("INC-99999")\n'
                '    print(f"Missing: {missing}")'
            ),
            "why": 'Missing ids should print None (and maybe an HTTP error line).',
            "common_mistake": 'INC-99999 is intentionally absent.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-99999', "message": 'Test missing ID'},
                {"type": 'contains', "value": 'Missing', "message": 'Print Missing'},
            ],
        },
        {
            "id": 'r11',
            "title": 'Run reliability script',
            "instruction": (
                'Click Analyze with the monitoring mock running.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    all_incidents = fetch_all_incidents(limit=3)\n'
                '    print(f"Paginated fetch: {len(all_incidents)} total incidents")\n'
                '    found = safe_get_incident("INC-38192")\n'
                '    print(f"Found: {found[\'id\'] if found else None}")\n'
                '    missing = safe_get_incident("INC-99999")\n'
                '    print(f"Missing: {missing}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    all_incidents = fetch_all_incidents(limit=3)\n'
                '    print(f"Paginated fetch: {len(all_incidents)} total incidents")\n'
                '    found = safe_get_incident("INC-38192")\n'
                '    print(f"Found: {found[\'id\'] if found else None}")\n'
                '    missing = safe_get_incident("INC-99999")\n'
                '    print(f"Missing: {missing}")'
            ),
            "why": 'End-to-end run proves pagination + error handling together.',
            "common_mistake": 'Syntax errors in except blocks are common — check colons.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'Paginated fetch', "message": 'Output shows Paginated fetch'},
            ],
        },
        {
            "id": 'r12',
            "title": 'Confirm Found INC-38192',
            "instruction": (
                'Final output should include Found: INC-38192.\n'
                '\n'
                'EXAMPLE:\n'
                'print(f"Found: {found[\'id\'] if found else None}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '    print(f"Found: {found[\'id\'] if found else None}")',
            "why": 'Found line proves safe_get_incident succeeds for real ids.',
            "common_mistake": 'None on Found means auth or id typo.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'Found: INC-38192', "message": 'Output shows Found: INC-38192'},
                {"type": 'output_contains', "value": 'Missing:', "message": 'Output shows Missing:'},
            ],
        },
    ],

    # ── reliability:paginate-only ──
    "reliability:paginate-only": [
        {
            "id": 'rp01',
            "title": 'Import os',
            "instruction": (
                'Pagination-only drill — gather every page.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'Need SOURCE_API_KEY from env.',
            "common_mistake": 'Import os first.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 'rp02',
            "title": 'Import requests + dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Standard API setup.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": 'load_dotenv', "message": 'load_dotenv'},
            ],
        },
        {
            "id": 'rp03',
            "title": 'Load key + URL',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "why": 'Paginate against the monitoring mock.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'rp04',
            "title": 'Init all_records + page',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'all_records = []\n'
                'page = 1\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'all_records = []\n'
                'page = 1'
            ),
            "why": "You'll accumulate every page into all_records.",
            "common_mistake": 'Start page at 1 (not 0) for this API.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'all_records', "message": 'all_records list'},
                {"type": 'contains', "value": 'page', "message": 'page variable'},
            ],
        },
        {
            "id": 'rp05',
            "title": 'While True GET page',
            "instruction": (
                'Add this under what you already typed. limit=2 forces many pages.\n'
                '\n'
                'EXAMPLE:\n'
                'while True:\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"page": page, "limit": 2},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    body = response.json()\n'
                '    all_records.extend(body["data"])\n'
                '    if not body["pagination"]["has_more"]:\n'
                '        break\n'
                '    page += 1\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'while True:\n'
                '    response = requests.get(\n'
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"page": page, "limit": 2},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    body = response.json()\n'
                '    all_records.extend(body["data"])\n'
                '    if not body["pagination"]["has_more"]:\n'
                '        break\n'
                '    page += 1'
            ),
            "why": 'limit=2 is small on purpose so has_more flips true then false.',
            "common_mistake": "Forget page += 1 and you'll infinite-loop.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'while', "message": 'While loop'},
                {"type": 'contains', "value": 'limit', "message": 'Pass limit param'},
                {"type": 'contains', "value": 'page', "message": 'Increment page'},
                {"type": 'contains', "value": 'extend', "message": 'Accumulate with extend()'},
                {"type": 'contains', "value": 'has_more', "message": 'Check has_more'},
            ],
        },
        {
            "id": 'rp06',
            "title": 'Print total',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Total:", len(all_records))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Total:", len(all_records))',
            "why": 'Total should match the full incident catalog size.',
            "common_mistake": 'Print after the while loop, not inside it.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'print', "message": 'Print total'},
                {"type": 'contains', "value": 'len(', "message": 'Use len() for count'},
            ],
        },
        {
            "id": 'rp07',
            "title": 'Print pages used',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Pages fetched:", page)\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Pages fetched:", page)',
            "why": 'page ends as the last page number you requested.',
            "common_mistake": 'If Pages fetched is 1 with limit=2, has_more break may be wrong.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'Pages fetched', "message": 'Print Pages fetched'},
            ],
        },
        {
            "id": 'rp08',
            "title": 'Print first id',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'if all_records:\n'
                '    print("First:", all_records[0]["id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if all_records:\n'
                '    print("First:", all_records[0]["id"])'
            ),
            "why": 'Spot-check the first record survived pagination.',
            "common_mistake": 'Guard with if all_records to avoid IndexError.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'First:', "message": 'Print First:'},
                {"type": 'contains', "value": 'all_records[0]', "message": 'Read first record'},
            ],
        },
        {
            "id": 'rp09',
            "title": 'Run pagination',
            "instruction": (
                'Click Analyze with monitoring mock up.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Total:", len(all_records))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Total:", len(all_records))',
            "why": 'A successful run prints Total with a positive count.',
            "common_mistake": 'Infinite hang → missing break on has_more.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'Total:', "message": 'Output shows Total:'},
            ],
        },
        {
            "id": 'rp10',
            "title": 'Confirm INC- in output',
            "instruction": (
                'Final output should include an INC- id.\n'
                '\n'
                'EXAMPLE:\n'
                'print("First:", all_records[0]["id"])\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("First:", all_records[0]["id"])',
            "why": 'Seeing INC- means pages returned real records.',
            "common_mistake": 'Auth problems yield empty data and no First line.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes INC- id'},
                {"type": 'output_contains', "value": 'Pages fetched', "message": 'Output includes Pages fetched'},
            ],
        },
        {
            "id": 'rp11',
            "title": 'Keep limit=2',
            "instruction": (
                'Confirm your params still use limit=2 for this drill.\n'
                '\n'
                'EXAMPLE:\n'
                'params={"page": page, "limit": 2}\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'params={"page": page, "limit": 2}',
            "why": 'Larger limits hide pagination bugs during training.',
            "common_mistake": "Don't switch to limit=100 here.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '"limit": 2', "message": 'Keep limit 2'},
            ],
        },
        {
            "id": 'rp12',
            "title": 'Re-run totals',
            "instruction": (
                'One more Analyze — Total should be stable across runs.\n'
                '\n'
                'EXAMPLE:\n'
                'print("Total:", len(all_records))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("Total:", len(all_records))',
            "why": 'Pagination should be deterministic on the mock dataset.',
            "common_mistake": 'Changing limit without resetting page logic causes duplicates.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'Total:', "message": 'Still prints Total:'},
                {"type": 'runs', "message": 'Still runs'},
            ],
        },
    ],

    # ── reliability:errors-only ──
    "reliability:errors-only": [
        {
            "id": 're01',
            "title": 'Import os',
            "instruction": (
                'Errors-only drill — safe GET with 404 handling.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'import os',
            "why": 'SOURCE_API_KEY comes from the environment.',
            "common_mistake": 'Import os first.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'os', "message": 'Import os'},
            ],
        },
        {
            "id": 're02',
            "title": 'Import requests + dotenv',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Need requests exceptions like HTTPError.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
            ],
        },
        {
            "id": 're03',
            "title": 'Load SOURCE env',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "why": 'Detail GETs still require Bearer auth.',
            "common_mistake": 'No hardcoded secrets.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SOURCE_API_KEY', "message": 'Load key'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 're04',
            "title": 'safe_get_incident try block',
            "instruction": (
                'Add this under what you already typed — start the safe helper.\n'
                '\n'
                'EXAMPLE:\n'
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        return None\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        return None'
            ),
            "why": 'Timeouts should not crash the whole sync job.',
            "common_mistake": 'Return None on timeout.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'safe_get_incident', "message": 'Define safe_get_incident()'},
                {"type": 'contains', "value": 'try:', "message": 'Use try/except'},
                {"type": 'contains', "value": 'Timeout', "message": 'Catch Timeout'},
            ],
        },
        {
            "id": 're05',
            "title": 'Catch HTTPError 404',
            "instruction": (
                'Update the function to handle 404 Not Found.\n'
                '\n'
                'EXAMPLE:\n'
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        return None\n'
                '    except requests.HTTPError as e:\n'
                '        if e.response is not None and e.response.status_code == 404:\n'
                '            print(f"{incident_id} not found")\n'
                '        return None\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def safe_get_incident(incident_id):\n'
                '    try:\n'
                '        response = requests.get(\n'
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        return response.json()\n'
                '    except requests.Timeout:\n'
                '        return None\n'
                '    except requests.HTTPError as e:\n'
                '        if e.response is not None and e.response.status_code == 404:\n'
                '            print(f"{incident_id} not found")\n'
                '        return None'
            ),
            "why": "404 means the id isn't in the system — log and continue.",
            "common_mistake": 'Check status_code == 404 before assuming not found.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '404', "message": 'Handle 404 not found'},
                {"type": 'contains', "value": 'HTTPError', "message": 'Catch HTTPError'},
                {"type": 'contains', "value": 'not found', "message": 'Print not found'},
            ],
        },
        {
            "id": 're06',
            "title": 'Test existing id',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    print(safe_get_incident("INC-38192"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    print(safe_get_incident("INC-38192"))'
            ),
            "why": 'Existing ids should print a dict (or at least include the id).',
            "common_mistake": 'Keep the __main__ guard.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-38192', "message": 'Test existing ID'},
                {"type": 'contains', "value": '__main__', "message": 'Main test block'},
            ],
        },
        {
            "id": 're07',
            "title": 'Test missing id',
            "instruction": (
                'Add this inside the __main__ block under the existing call.\n'
                '\n'
                'EXAMPLE:\n'
                'print(safe_get_incident("INC-99999"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '    print(safe_get_incident("INC-99999"))',
            "why": 'Missing ids should print not found and then None.',
            "common_mistake": 'Indent under __main__.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'INC-99999', "message": 'Test missing ID'},
            ],
        },
        {
            "id": 're08',
            "title": 'Label the outputs',
            "instruction": (
                'Update your prints with EXISTING/MISSING labels.\n'
                '\n'
                'EXAMPLE:\n'
                'print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '    print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))'
            ),
            "why": 'Labels make the two cases obvious in the console.',
            "common_mistake": 'Call the function twice — once per id.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'EXISTING', "message": 'Label EXISTING'},
                {"type": 'contains', "value": 'MISSING', "message": 'Label MISSING'},
            ],
        },
        {
            "id": 're09',
            "title": 'Run error handling',
            "instruction": (
                'Click Analyze with the mock API running.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))'
            ),
            "why": 'You should see a not found line for INC-99999.',
            "common_mistake": 'Unhandled exceptions mean your except block is incomplete.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'not found', "message": 'Output mentions not found'},
            ],
        },
        {
            "id": 're10',
            "title": 'Confirm EXISTING id',
            "instruction": (
                'Final output should include INC-38192 for the existing case.\n'
                '\n'
                'EXAMPLE:\n'
                'print("EXISTING", safe_get_incident("INC-38192"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '    print("EXISTING", safe_get_incident("INC-38192"))',
            "why": 'EXISTING line proves success path still works.',
            "common_mistake": 'If EXISTING is None, check auth.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-38192', "message": 'Output includes INC-38192'},
                {"type": 'output_contains', "value": 'MISSING', "message": 'Output includes MISSING label'},
            ],
        },
        {
            "id": 're11',
            "title": 'Keep 404 branch',
            "instruction": (
                "Don't remove the 404 print — trainers look for it.\n"
                '\n'
                'EXAMPLE:\n'
                'if e.response is not None and e.response.status_code == 404:\n'
                '            print(f"{incident_id} not found")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '        if e.response is not None and e.response.status_code == 404:\n'
                '            print(f"{incident_id} not found")'
            ),
            "why": 'Explicit 404 handling is the point of this exercise.',
            "common_mistake": 'Returning None without printing hides the miss.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '404', "message": 'Keep 404 handling'},
            ],
        },
        {
            "id": 're12',
            "title": 'Re-run both cases',
            "instruction": (
                'Click Analyze once more to confirm both paths.\n'
                '\n'
                'EXAMPLE:\n'
                'print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '    print("EXISTING", safe_get_incident("INC-38192"))\n'
                '    print("MISSING", safe_get_incident("INC-99999"))'
            ),
            "why": 'Both success and failure paths should remain stable.',
            "common_mistake": "Crashing on 404 means raise_for_status isn't caught.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'not found', "message": 'Still prints not found'},
                {"type": 'runs', "message": 'Still runs'},
            ],
        },
    ],

    # ── capstone-build:full-capstone ──
    "capstone-build:full-capstone": [
        {
            "id": 'c01',
            "title": 'Imports',
            "instruction": (
                'Capstone: wire a full sync. Start with imports + load_dotenv.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'import os\n'
                '\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Capstone reuses every skill: env, GET, transform, POST, errors.',
            "common_mistake": 'Call load_dotenv() before getenv.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": 'load_dotenv', "message": 'load_dotenv'},
            ],
        },
        {
            "id": 'c02',
            "title": 'load_config function',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def load_config():\n'
                '    source_key = os.getenv("SOURCE_API_KEY")\n'
                '    dest_key = os.getenv("DESTINATION_API_KEY")\n'
                '    if not source_key or not dest_key:\n'
                '        raise ValueError("Set SOURCE_API_KEY and DESTINATION_API_KEY in .env")\n'
                '    return {\n'
                '        "source_key": source_key,\n'
                '        "dest_key": dest_key,\n'
                '        "source_url": os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001"),\n'
                '        "dest_url": os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002"),\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def load_config():\n'
                '    source_key = os.getenv("SOURCE_API_KEY")\n'
                '    dest_key = os.getenv("DESTINATION_API_KEY")\n'
                '    if not source_key or not dest_key:\n'
                '        raise ValueError("Set SOURCE_API_KEY and DESTINATION_API_KEY in .env")\n'
                '    return {\n'
                '        "source_key": source_key,\n'
                '        "dest_key": dest_key,\n'
                '        "source_url": os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001"),\n'
                '        "dest_url": os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002"),\n'
                '    }'
            ),
            "why": 'Failing fast on missing keys beats cryptic 401s later.',
            "common_mistake": 'Raise ValueError if either key is missing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'load_config', "message": 'Define load_config()'},
                {"type": 'contains', "value": 'ValueError', "message": 'Raise on missing keys'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'c03',
            "title": 'transform_incident',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(incident):\n'
                '    priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(incident):\n'
                '    priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                '    }'
            ),
            "why": 'Transform before every POST.',
            "common_mistake": 'external_id maps from id.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_incident', "message": 'transform_incident'},
                {"type": 'contains', "value": 'external_id', "message": 'Map external_id'},
            ],
        },
        {
            "id": 'c04',
            "title": 'create_ticket(config, ticket)',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def create_ticket(config, ticket):\n'
                '    response = requests.post(\n'
                '        f"{config[\'dest_url\']}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {config[\'dest_key\']}"},\n'
                '        json=ticket,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def create_ticket(config, ticket):\n'
                '    response = requests.post(\n'
                '        f"{config[\'dest_url\']}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {config[\'dest_key\']}"},\n'
                '        json=ticket,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()'
            ),
            "why": "Pass config so keys/URLs aren't globals.",
            "common_mistake": 'Use dest_key, not source_key, on POST.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'create_ticket', "message": 'create_ticket'},
                {"type": 'contains', "value": 'requests.post', "message": 'POST tickets'},
                {"type": 'contains', "value": 'dest_key', "message": 'Use dest_key'},
            ],
        },
        {
            "id": 'c05',
            "title": 'fetch_all_open_incidents paginated',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_all_open_incidents(config):\n'
                '    all_incidents = []\n'
                '    page = 1\n'
                '    headers = {"Authorization": f"Bearer {config[\'source_key\']}"}\n'
                '    while True:\n'
                '        response = requests.get(\n'
                '            f"{config[\'source_url\']}/v1/incidents",\n'
                '            headers=headers,\n'
                '            params={"status": "open", "page": page, "limit": 100},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        body = response.json()\n'
                '        all_incidents.extend(body["data"])\n'
                '        if not body["pagination"]["has_more"]:\n'
                '            break\n'
                '        page += 1\n'
                '    return all_incidents\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_all_open_incidents(config):\n'
                '    all_incidents = []\n'
                '    page = 1\n'
                '    headers = {"Authorization": f"Bearer {config[\'source_key\']}"}\n'
                '    while True:\n'
                '        response = requests.get(\n'
                '            f"{config[\'source_url\']}/v1/incidents",\n'
                '            headers=headers,\n'
                '            params={"status": "open", "page": page, "limit": 100},\n'
                '            timeout=30,\n'
                '        )\n'
                '        response.raise_for_status()\n'
                '        body = response.json()\n'
                '        all_incidents.extend(body["data"])\n'
                '        if not body["pagination"]["has_more"]:\n'
                '            break\n'
                '        page += 1\n'
                '    return all_incidents'
            ),
            "why": "Capstone fetch must paginate — don't assume one page.",
            "common_mistake": 'Filter status=open in params.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_all_open_incidents', "message": 'Paginated fetch'},
                {"type": 'contains', "value": 'while', "message": 'Pagination loop'},
                {"type": 'contains', "value": 'has_more', "message": 'Check has_more'},
            ],
        },
        {
            "id": 'c06',
            "title": 'sync() skeleton',
            "instruction": (
                'Add this under what you already typed — filter first.\n'
                '\n'
                'EXAMPLE:\n'
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    to_sync = [i for i in incidents if i["severity"] in {"critical", "high"}]\n'
                '    return to_sync\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    to_sync = [i for i in incidents if i["severity"] in {"critical", "high"}]\n'
                '    return to_sync'
            ),
            "why": 'Urgent capstone sync keeps critical + high.',
            "common_mistake": 'Build to_sync before POSTing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'sync', "message": 'Define sync()'},
                {"type": 'contains', "value": 'critical', "message": 'Include critical'},
                {"type": 'contains', "value": 'high', "message": 'Include high'},
            ],
        },
        {
            "id": 'c07',
            "title": 'POST loop with SKIP on 409',
            "instruction": (
                'Update sync() with filter + create + 409 handling.\n'
                '\n'
                'EXAMPLE:\n'
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in {"critical", "high"}:\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(config, ticket)\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in {"critical", "high"}:\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(config, ticket)\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise'
            ),
            "why": 'Duplicates and non-urgent rows both print SKIP {id}.',
            "common_mistake": 'Handle status_code 409 explicitly.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '409', "message": 'Handle duplicates'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
                {"type": 'contains', "value": 'create_ticket', "message": 'Call create_ticket'},
            ],
        },
        {
            "id": 'c08',
            "title": 'Entry point',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    sync()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    sync()'
            ),
            "why": 'The course runner executes the file — main guard calls sync().',
            "common_mistake": 'Call sync() inside __main__.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '__main__', "message": 'Main guard'},
                {"type": 'contains', "value": 'sync()', "message": 'Call sync()'},
            ],
        },
        {
            "id": 'c09',
            "title": 'Print start banner',
            "instruction": (
                'Optional polish: banner prints around the sync work.\n'
                '\n'
                'EXAMPLE:\n'
                'def sync():\n'
                '    print("CAPSTONE SYNC START")\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    to_sync = [i for i in incidents if i["severity"] in {"critical", "high"}]\n'
                '    for incident in to_sync:\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(config, ticket)\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise\n'
                '    print("CAPSTONE SYNC DONE")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'print("CAPSTONE SYNC START")',
            "why": 'Banners make long runs easier to scan in class.',
            "common_mistake": 'Keep SKIP/CREATED prints either way.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'SKIP', "message": 'Keep SKIP prints'},
            ],
        },
        {
            "id": 'c10',
            "title": 'Run full capstone',
            "instruction": (
                'Update sync to SKIP non-urgent severities too, then Analyze.\n'
                '\n'
                'EXAMPLE:\n'
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    to_sync = [i for i in incidents if i["severity"] in {"critical", "high"}]\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in {"critical", "high"}:\n'
                '            print(f"SKIP {incident[\'id"]}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(config, ticket)\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    sync()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def sync():\n'
                '    config = load_config()\n'
                '    incidents = fetch_all_open_incidents(config)\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] not in {"critical", "high"}:\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        ticket = transform_incident(incident)\n'
                '        try:\n'
                '            created = create_ticket(config, ticket)\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise'
            ),
            "why": 'Live sync should print SKIP for non-urgent and/or duplicates.',
            "common_mistake": 'ValueError means .env keys are missing.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'sync', "message": 'Keep sync()'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output includes SKIP'},
            ],
        },
        {
            "id": 'c11',
            "title": 'Confirm INC- in output',
            "instruction": (
                'Output should mention INC- ids on SKIP/CREATED lines.\n'
                '\n'
                'EXAMPLE:\n'
                'sync()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    sync()'
            ),
            "why": 'Incident ids prove you synced real mock records.',
            "common_mistake": 'No INC- text → prints missing inside the loop.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes INC- id'},
            ],
        },
        {
            "id": 'c12',
            "title": 'Confirm ticket language',
            "instruction": (
                'Prefer CREATED lines that include a destination ticket id when new.\n'
                '\n'
                'EXAMPLE:\n'
                'print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")',
            "why": 'CREATED/SKIP vocabulary matches ops runbooks.',
            "common_mistake": 'Re-running often yields more SKIP after first CREATED.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'CREATED', "message": 'Print CREATED on success'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Still see SKIP in output'},
            ],
        },
    ],

    # ── capstone-build:critical-capstone ──
    "capstone-build:critical-capstone": [
        {
            "id": 'cb01',
            "title": 'Imports',
            "instruction": (
                'Critical-only capstone with stats. Start with imports.\n'
                '\n'
                'EXAMPLE:\n'
                'import os\n'
                '\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'import os\n'
                '\n'
                'import requests\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()'
            ),
            "why": 'Same foundation as the full capstone.',
            "common_mistake": 'Call load_dotenv().',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_import', "module": 'requests', "message": 'Import requests'},
                {"type": 'contains', "value": 'load_dotenv', "message": 'load_dotenv'},
            ],
        },
        {
            "id": 'cb02',
            "title": 'load_config',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def load_config():\n'
                '    source_key = os.getenv("SOURCE_API_KEY")\n'
                '    dest_key = os.getenv("DESTINATION_API_KEY")\n'
                '    if not source_key or not dest_key:\n'
                '        raise ValueError("Missing API keys")\n'
                '    return {\n'
                '        "source_key": source_key,\n'
                '        "dest_key": dest_key,\n'
                '        "source_url": os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001"),\n'
                '        "dest_url": os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002"),\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def load_config():\n'
                '    source_key = os.getenv("SOURCE_API_KEY")\n'
                '    dest_key = os.getenv("DESTINATION_API_KEY")\n'
                '    if not source_key or not dest_key:\n'
                '        raise ValueError("Missing API keys")\n'
                '    return {\n'
                '        "source_key": source_key,\n'
                '        "dest_key": dest_key,\n'
                '        "source_url": os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001"),\n'
                '        "dest_url": os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002"),\n'
                '    }'
            ),
            "why": 'Validate both keys before syncing.',
            "common_mistake": 'Include URLs in the returned config.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'load_config', "message": 'load_config()'},
                {"type": 'contains', "value": 'ValueError', "message": 'Raise ValueError'},
                {"type": 'no_hardcoded_secrets', "message": 'No hardcoded secrets'},
            ],
        },
        {
            "id": 'cb03',
            "title": 'transform_incident priority 1',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1,\n'
                '    }\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def transform_incident(incident):\n'
                '    return {\n'
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": 1,\n'
                '    }'
            ),
            "why": 'Critical-only tickets always get priority 1.',
            "common_mistake": "Don't map high in this exercise.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'transform_incident', "message": 'transform_incident()'},
                {"type": 'contains', "value": 'priority', "message": 'Set priority'},
            ],
        },
        {
            "id": 'cb04',
            "title": 'create_ticket',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def create_ticket(config, ticket):\n'
                '    response = requests.post(\n'
                '        f"{config[\'dest_url\']}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {config[\'dest_key\']}"},\n'
                '        json=ticket,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def create_ticket(config, ticket):\n'
                '    response = requests.post(\n'
                '        f"{config[\'dest_url\']}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {config[\'dest_key\']}"},\n'
                '        json=ticket,\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()'
            ),
            "why": 'POST with destination key from config.',
            "common_mistake": 'json=ticket sends the transformed payload.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'create_ticket', "message": 'create_ticket'},
                {"type": 'contains', "value": 'requests.post', "message": 'POST'},
            ],
        },
        {
            "id": 'cb05',
            "title": 'fetch open incidents',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def fetch_open_incidents(config):\n'
                '    response = requests.get(\n'
                '        f"{config[\'source_url\']}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {config[\'source_key\']}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def fetch_open_incidents(config):\n'
                '    response = requests.get(\n'
                '        f"{config[\'source_url\']}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {config[\'source_key\']}"},\n'
                '        params={"status": "open"},\n'
                '        timeout=30,\n'
                '    )\n'
                '    response.raise_for_status()\n'
                '    return response.json()["data"]'
            ),
            "why": 'Fetch open incidents, then keep critical only.',
            "common_mistake": 'Use source_key for GET.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'fetch_open_incidents', "message": 'fetch_open_incidents'},
            ],
        },
        {
            "id": 'cb06',
            "title": 'Critical filter expression',
            "instruction": (
                'Add this idea under what you already typed (comment ok) — critical equality only.\n'
                '\n'
                'EXAMPLE:\n'
                '# inside sync later:\n'
                'to_sync = [i for i in incidents if i["severity"] == "critical"]\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": 'to_sync = [i for i in incidents if i["severity"] == "critical"]',
            "why": 'Hospital SLA: severity must equal critical.',
            "common_mistake": 'Do not include high in the filter.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical', "message": 'Filter critical'},
                {"type": 'not_contains', "value": '"high"', "message": 'Exclude high severity'},
            ],
        },
        {
            "id": 'cb07',
            "title": 'sync with stats',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'def sync():\n'
                '    config = load_config()\n'
                '    stats = {"created": 0, "skipped": 0}\n'
                '    incidents = fetch_open_incidents(config)\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] != "critical":\n'
                '            stats["skipped"] += 1\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(config, transform_incident(incident))\n'
                '            stats["created"] += 1\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                stats["skipped"] += 1\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise\n'
                '    print(f"created={stats[\'created\']} skipped={stats[\'skipped\']}")\n'
                '    return stats\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'def sync():\n'
                '    config = load_config()\n'
                '    stats = {"created": 0, "skipped": 0}\n'
                '    incidents = fetch_open_incidents(config)\n'
                '    for incident in incidents:\n'
                '        if incident["severity"] != "critical":\n'
                '            stats["skipped"] += 1\n'
                '            print(f"SKIP {incident[\'id\']}")\n'
                '            continue\n'
                '        try:\n'
                '            created = create_ticket(config, transform_incident(incident))\n'
                '            stats["created"] += 1\n'
                '            print(f"CREATED {incident[\'id\']} -> {created.get(\'id\')}")\n'
                '        except requests.HTTPError as e:\n'
                '            if e.response is not None and e.response.status_code == 409:\n'
                '                stats["skipped"] += 1\n'
                '                print(f"SKIP {incident[\'id\']}")\n'
                '            else:\n'
                '                raise\n'
                '    print(f"created={stats[\'created\']} skipped={stats[\'skipped\']}")\n'
                '    return stats'
            ),
            "why": 'Stats summarize created vs skipped for the hospital SLA run.',
            "common_mistake": 'Increment skipped for non-critical and for 409.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'has_function', "name": 'sync', "message": 'Define sync()'},
                {"type": 'contains', "value": 'created', "message": 'Track created'},
                {"type": 'contains', "value": 'print', "message": 'Print summary'},
                {"type": 'contains', "value": 'SKIP', "message": 'Print SKIP'},
            ],
        },
        {
            "id": 'cb08',
            "title": 'Entry point',
            "instruction": (
                'Add this under what you already typed.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    sync()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    sync()'
            ),
            "why": 'Execute sync when the file runs.',
            "common_mistake": "Don't forget the main guard.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": '__main__', "message": 'Main guard'},
                {"type": 'contains', "value": 'sync()', "message": 'Call sync()'},
            ],
        },
        {
            "id": 'cb09',
            "title": 'Run critical capstone',
            "instruction": (
                'Click Analyze — both mocks + .env required.\n'
                '\n'
                'EXAMPLE:\n'
                'if __name__ == "__main__":\n'
                '    sync()\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                'if __name__ == "__main__":\n'
                '    sync()'
            ),
            "why": 'Expect SKIP lines and a created=/skipped= summary.',
            "common_mistake": 'Missing dest key → POST failures.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'runs', "message": 'Script runs'},
                {"type": 'output_contains', "value": 'SKIP', "message": 'Output includes SKIP'},
                {"type": 'output_contains', "value": 'created=', "message": 'Output includes created='},
            ],
        },
        {
            "id": 'cb10',
            "title": 'Confirm skipped=',
            "instruction": (
                'Summary must include skipped=.\n'
                '\n'
                'EXAMPLE:\n'
                'print(f"created={stats[\'created\']} skipped={stats[\'skipped\']}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '    print(f"created={stats[\'created\']} skipped={stats[\'skipped\']}")',
            "why": 'skipped counts non-critical rows plus duplicates.',
            "common_mistake": "If skipped is always 0, filter isn't counting.",
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'skipped=', "message": 'Output includes skipped='},
            ],
        },
        {
            "id": 'cb11',
            "title": 'Confirm INC- ids',
            "instruction": (
                'SKIP/CREATED lines should include INC- ids.\n'
                '\n'
                'EXAMPLE:\n'
                'print(f"SKIP {incident[\'id\']}")\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": '            print(f"SKIP {incident[\'id\']}")',
            "why": 'Ids tie the stats back to concrete incidents.',
            "common_mistake": 'Printing only numbers hides which rows were skipped.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'output_contains', "value": 'INC-', "message": 'Output includes INC- id'},
            ],
        },
        {
            "id": 'cb12',
            "title": 'Keep critical-only rule',
            "instruction": (
                'Final review — do not widen the filter to high.\n'
                '\n'
                'EXAMPLE:\n'
                'if incident["severity"] != "critical":\n'
                '            continue\n'
                '\n'
                "Type it yourself — don't paste. Click Analyze when done."
            ),
            "example": (
                '        if incident["severity"] != "critical":\n'
                '            continue'
            ),
            "why": 'This exercise is critical-only on purpose.',
            "common_mistake": 'Adding high breaks the hospital SLA scenario.',
            "reveal_after_fails": 2,
            "checks": [
                {"type": 'contains', "value": 'critical', "message": 'Keep critical filter'},
                {"type": 'not_contains', "value": '"high"', "message": 'Still exclude high'},
                {"type": 'runs', "message": 'Still runs'},
            ],
        },
    ],

    "practice-methods:drill": [
        {
            "id": "pm1",
            "title": "GET retrieves",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("GET retrieves data")\n\n'
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": 'print("GET retrieves data")',
            "checks": [
                {"type": "contains", "value": "print", "message": "Use print()"},
                {"type": "contains", "value": "GET", "message": "Mention GET"},
                {"type": "contains", "value": "retriev", "message": "Say GET retrieves (or retrieve)"},
            ],
        },
        {
            "id": "pm2",
            "title": "POST creates",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("POST creates a new resource")\n\n'
                "Add this on a new line under your GET print. Click Analyze when done."
            ),
            "example": 'print("POST creates a new resource")',
            "checks": [
                {"type": "contains", "value": "POST", "message": "Mention POST"},
                {"type": "contains", "value": "creat", "message": "Say POST creates"},
            ],
        },
        {
            "id": "pm3",
            "title": "PATCH partially updates",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("PATCH partially updates a resource")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("PATCH partially updates a resource")',
            "checks": [
                {"type": "contains", "value": "PATCH", "message": "Mention PATCH"},
                {"type": "contains", "value": "partial", "message": "Say PATCH partially updates"},
            ],
        },
        {
            "id": "pm4",
            "title": "PUT replaces",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("PUT replaces a whole resource")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("PUT replaces a whole resource")',
            "checks": [
                {"type": "contains", "value": "PUT", "message": "Mention PUT"},
                {"type": "contains", "value": "replac", "message": "Say PUT replaces"},
            ],
        },
        {
            "id": "pm5",
            "title": "DELETE removes",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("DELETE removes a resource")\n\n'
                "Add this last line. Click Analyze when done."
            ),
            "example": 'print("DELETE removes a resource")',
            "checks": [
                {"type": "contains", "value": "DELETE", "message": "Mention DELETE"},
                {"type": "contains", "value": "remov", "message": "Say DELETE removes"},
                {"type": "contains", "value": "GET", "message": "Keep your GET line"},
                {"type": "contains", "value": "POST", "message": "Keep your POST line"},
            ],
        },
    ],

    # ── Practice: Status code drill ──
    "practice-status:drill": [
        {
            "id": "ps1",
            "title": "200 OK",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("200 OK — success, keep going")\n\n'
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": 'print("200 OK — success, keep going")',
            "checks": [
                {"type": "contains", "value": "200", "message": "Include 200"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
        {
            "id": "ps2",
            "title": "201 Created",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("201 Created — resource was created")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("201 Created — resource was created")',
            "checks": [
                {"type": "contains", "value": "201", "message": "Include 201"},
                {"type": "contains", "value": "creat", "message": "Mention created/create"},
            ],
        },
        {
            "id": "ps3",
            "title": "401 Unauthorized",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("401 Unauthorized — check your API key / Bearer token")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("401 Unauthorized — check your API key / Bearer token")',
            "checks": [
                {"type": "contains", "value": "401", "message": "Include 401"},
                {"type": "regex", "pattern": r"(?i)(key|token|auth|bearer)", "message": "Hint at fixing auth/key/token"},
            ],
        },
        {
            "id": "ps4",
            "title": "404 Not Found",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("404 Not Found — check the URL or resource id")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("404 Not Found — check the URL or resource id")',
            "checks": [
                {"type": "contains", "value": "404", "message": "Include 404"},
                {"type": "regex", "pattern": r"(?i)(url|path|id|not found)", "message": "Mention URL/id/not found"},
            ],
        },
        {
            "id": "ps5",
            "title": "409 Conflict",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("409 Conflict — duplicate; skip or update instead")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("409 Conflict — duplicate; skip or update instead")',
            "checks": [
                {"type": "contains", "value": "409", "message": "Include 409"},
                {"type": "regex", "pattern": r"(?i)(dup|conflict|skip|exist)", "message": "Mention duplicate/conflict/skip"},
            ],
        },
        {
            "id": "ps6",
            "title": "429 Too Many Requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("429 Too Many Requests — wait / backoff and retry")\n\n'
                "Add this line. Click Analyze when done."
            ),
            "example": 'print("429 Too Many Requests — wait / backoff and retry")',
            "checks": [
                {"type": "contains", "value": "429", "message": "Include 429"},
                {"type": "regex", "pattern": r"(?i)(wait|backoff|retry|rate)", "message": "Mention wait/backoff/retry"},
            ],
        },
        {
            "id": "ps7",
            "title": "500 Server Error",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("500 Server Error — retry later; not your code\'s fault")\n\n'
                "Add this last line. Click Analyze when done."
            ),
            "example": 'print("500 Server Error — retry later; not your code\'s fault")',
            "checks": [
                {"type": "contains", "value": "500", "message": "Include 500"},
                {"type": "contains", "value": "200", "message": "Keep your earlier status lines"},
                {"type": "contains", "value": "401", "message": "Keep 401 line"},
            ],
        },
    ],

    # ── Baby 1: print() ──
    "baby-print:main": [
        {
            "id": "bp1",
            "title": "Open the editor",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "# my first line\n\n"
                "Type that comment so the file isn't empty. Click Analyze when done."
            ),
            "example": "# my first line",
            "checks": [
                {"type": "contains", "value": "#", "message": "Add a comment line starting with #"},
            ],
        },
        {
            "id": "bp2",
            "title": "Type print()",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Hello, API Bootcamp")\n\n'
                "Add this under your comment. Click Analyze when done."
            ),
            "example": 'print("Hello, API Bootcamp")',
            "checks": [
                {"type": "contains", "value": "print", "message": "Use print()"},
                {"type": "contains", "value": "Hello", "message": "Include Hello in the string"},
            ],
        },
        {
            "id": "bp3",
            "title": "Keep the full greeting",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Hello, API Bootcamp")\n\n'
                "Make sure the string includes API Bootcamp. Click Analyze when done."
            ),
            "example": 'print("Hello, API Bootcamp")',
            "checks": [
                {"type": "contains", "value": "print", "message": "Keep print()"},
                {"type": "contains", "value": "API Bootcamp", "message": "Include API Bootcamp"},
            ],
        },
        {
            "id": "bp4",
            "title": "Run it",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Hello, API Bootcamp")\n\n'
                "Keep that line. Click Run (or Analyze) — output should show Hello."
            ),
            "example": 'print("Hello, API Bootcamp")',
            "checks": [
                {"type": "contains", "value": "print", "message": "Keep print()"},
                {"type": "contains", "value": "Hello", "message": "Keep Hello in the string"},
                {"type": "output_contains", "value": "Hello", "message": "Running prints Hello"},
            ],
        },
    ],

    # ── Baby 2: import requests ──
    "baby-import:main": [
        {
            "id": "bi1",
            "title": "Import requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n\n"
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": "import requests",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
            ],
        },
        {
            "id": "bi2",
            "title": "Confirm it loaded",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n"
                'print("requests loaded")\n\n'
                "Add the print under the import. Click Analyze when done."
            ),
            "example": 'import requests\nprint("requests loaded")',
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "print", "message": "Print a confirmation"},
            ],
        },
        {
            "id": "bi3",
            "title": "Exact confirmation text",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("requests loaded")\n\n'
                "Use that exact phrase so you know the import worked. Click Analyze when done."
            ),
            "example": 'print("requests loaded")',
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Keep import requests"},
                {"type": "contains", "value": "requests loaded", "message": "Print 'requests loaded'"},
            ],
        },
        {
            "id": "bi4",
            "title": "Run confirmation",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n"
                'print("requests loaded")\n\n'
                "Click Analyze (or Run) — you should see requests loaded in the output."
            ),
            "example": 'import requests\nprint("requests loaded")',
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "print", "message": "Keep the print"},
                {"type": "output_contains", "value": "requests loaded", "message": "Output shows requests loaded"},
            ],
        },
    ],

    # ── Baby 3: GET /health ──
    "baby-health:main": [
        {
            "id": "bh1",
            "title": "Import requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n\n"
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": "import requests",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
            ],
        },
        {
            "id": "bh2",
            "title": "Set the URL",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'url = "http://127.0.0.1:5001/health"\n\n'
                "Add this under the import. No Authorization needed. Click Analyze when done."
            ),
            "example": 'url = "http://127.0.0.1:5001/health"',
            "checks": [
                {"type": "contains", "value": "/health", "message": "URL includes /health"},
                {"type": "contains", "value": "5001", "message": "Point at port 5001"},
            ],
        },
        {
            "id": "bh3",
            "title": "Call requests.get",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.get(url, timeout=30)\n\n"
                "Add this under your url line. Click Analyze when done."
            ),
            "example": "response = requests.get(url, timeout=30)",
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "timeout", "message": "Pass timeout=30"},
                {"type": "not_contains", "value": "Authorization", "message": "Health needs no auth header"},
            ],
        },
        {
            "id": "bh4",
            "title": "Print status code",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "print(response.status_code)\n\n"
                "Add this last line. Click Analyze when done. Mock APIs must be running."
            ),
            "example": "print(response.status_code)",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "/health", "message": "Hit /health"},
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "status_code", "message": "Print status_code"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
    ],

    # ── Baby 4: Read JSON ──
    "baby-json:main": [
        {
            "id": "bj1",
            "title": "Import + GET health",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n\n"
                'url = "http://127.0.0.1:5001/health"\n'
                "response = requests.get(url, timeout=30)\n\n"
                "Type those three lines. Click Analyze when done."
            ),
            "example": (
                "import requests\n\n"
                'url = "http://127.0.0.1:5001/health"\n'
                "response = requests.get(url, timeout=30)"
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "/health", "message": "Call /health"},
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
            ],
        },
        {
            "id": "bj2",
            "title": "raise_for_status",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response.raise_for_status()\n\n"
                "Add this after the get. Click Analyze when done."
            ),
            "example": "response.raise_for_status()",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "Call raise_for_status()"},
            ],
        },
        {
            "id": "bj3",
            "title": "Parse JSON",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "body = response.json()\n\n"
                "Add this under raise_for_status. Click Analyze when done."
            ),
            "example": "body = response.json()",
            "checks": [
                {"type": "contains", "value": "json()", "message": "Call response.json()"},
            ],
        },
        {
            "id": "bj4",
            "title": "Print service name",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print(body["service"])\n\n'
                "Add this last line. Click Analyze when done."
            ),
            "example": 'print(body["service"])',
            "checks": [
                {"type": "contains", "value": "service", "message": "Read the service field"},
                {"type": "contains", "value": "print", "message": "Print the service name"},
                {"type": "contains", "value": "json()", "message": "Keep response.json()"},
            ],
        },
    ],

    # ── Baby 5: Store the URL ──
    "baby-variables:main": [
        {
            "id": "bv1",
            "title": "Import requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n\n"
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": "import requests",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
            ],
        },
        {
            "id": "bv2",
            "title": "BASE variable",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'BASE = "http://127.0.0.1:5001"\n\n'
                "Add this under the import — base only, no /health yet. Click Analyze when done."
            ),
            "example": 'BASE = "http://127.0.0.1:5001"',
            "checks": [
                {"type": "contains", "value": "BASE", "message": "Define BASE"},
                {"type": "contains", "value": "5001", "message": "Include port 5001"},
            ],
        },
        {
            "id": "bv3",
            "title": "GET with f-string",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'response = requests.get(f"{BASE}/health", timeout=30)\n\n'
                "Add this under BASE. Click Analyze when done."
            ),
            "example": 'response = requests.get(f"{BASE}/health", timeout=30)',
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "BASE", "message": "Use BASE in the URL"},
                {"type": "contains", "value": "/health", "message": "Hit /health"},
            ],
        },
        {
            "id": "bv4",
            "title": "Print JSON",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "print(response.json())\n\n"
                "Add this last line. Click Analyze when done."
            ),
            "example": "print(response.json())",
            "checks": [
                {"type": "contains", "value": "json()", "message": "Call response.json()"},
                {"type": "contains", "value": "print", "message": "Print the JSON"},
                {"type": "contains", "value": "BASE", "message": "Keep BASE variable"},
            ],
        },
    ],

    # ── Baby 6: Bearer auth (hardcoded OK) ──
    "baby-auth:main": [
        {
            "id": "ba1",
            "title": "Import requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import requests\n\n"
                "Now type that in the editor. Click Analyze when done."
            ),
            "example": "import requests",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
            ],
        },
        {
            "id": "ba2",
            "title": "Hardcode API key (OK here)",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = "dev-source-key-12345"\n\n'
                "Hardcoding is ALLOWED in this lesson only. Add the line. Click Analyze when done."
            ),
            "example": 'API_KEY = "dev-source-key-12345"',
            "checks": [
                {"type": "contains", "value": "API_KEY", "message": "Define API_KEY"},
                {"type": "contains", "value": "dev-source-key", "message": "Use the practice key value"},
            ],
        },
        {
            "id": "ba3",
            "title": "Build Bearer headers",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n\n'
                "Add this under API_KEY. Click Analyze when done."
            ),
            "example": 'headers = {"Authorization": f"Bearer {API_KEY}"}',
            "checks": [
                {"type": "contains", "value": "Authorization", "message": "Set Authorization header"},
                {"type": "contains", "value": "Bearer", "message": "Use Bearer scheme"},
                {"type": "contains", "value": "headers", "message": "Store headers dict"},
            ],
        },
        {
            "id": "ba4",
            "title": "GET /v1/incidents",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'response = requests.get(\n'
                '    "http://127.0.0.1:5001/v1/incidents",\n'
                "    headers=headers,\n"
                "    timeout=30,\n"
                ")\n\n"
                "Add this under headers. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    "http://127.0.0.1:5001/v1/incidents",\n'
                "    headers=headers,\n"
                "    timeout=30,\n"
                ")"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "/v1/incidents", "message": "Hit /v1/incidents"},
                {"type": "contains", "value": "headers", "message": "Pass headers="},
            ],
        },
        {
            "id": "ba5",
            "title": "Print status code",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "print(response.status_code)\n\n"
                "Add this last line. Click Analyze when done."
            ),
            "example": "print(response.status_code)",
            "checks": [
                {"type": "contains", "value": "status_code", "message": "Print status_code"},
                {"type": "contains", "value": "print", "message": "Use print()"},
                {"type": "contains", "value": "Bearer", "message": "Keep Bearer auth"},
            ],
        },
    ],

    # ── Baby 7: os.getenv ──
    "baby-getenv:main": [
        {
            "id": "bg1",
            "title": "Import os + requests",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n\n"
                "Type both imports. Your .env should already have SOURCE_API_KEY. Click Analyze when done."
            ),
            "example": "import os\nimport requests",
            "checks": [
                {"type": "has_import", "module": "os", "message": "Import os"},
                {"type": "has_import", "module": "requests", "message": "Import requests"},
            ],
        },
        {
            "id": "bg2",
            "title": "Load key with getenv",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n\n'
                "No hardcoded secret this time. Add the line. Click Analyze when done."
            ),
            "example": 'API_KEY = os.getenv("SOURCE_API_KEY")',
            "checks": [
                {"type": "contains", "value": "os.getenv", "message": "Use os.getenv()"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded API keys"},
            ],
        },
        {
            "id": "bg3",
            "title": "Bearer headers",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n\n'
                "Add this under API_KEY. Click Analyze when done."
            ),
            "example": 'headers = {"Authorization": f"Bearer {API_KEY}"}',
            "checks": [
                {"type": "contains", "value": "Bearer", "message": "Use Bearer auth"},
                {"type": "contains", "value": "Authorization", "message": "Set Authorization"},
            ],
        },
        {
            "id": "bg4",
            "title": "GET incidents",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'response = requests.get(\n'
                '    "http://127.0.0.1:5001/v1/incidents",\n'
                "    headers=headers,\n"
                "    timeout=30,\n"
                ")\n"
                "print(response.status_code)\n\n"
                "Add the get + print. Click Analyze when done."
            ),
            "example": (
                'response = requests.get(\n'
                '    "http://127.0.0.1:5001/v1/incidents",\n'
                "    headers=headers,\n"
                "    timeout=30,\n"
                ")\n"
                "print(response.status_code)"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "/v1/incidents", "message": "Hit /v1/incidents"},
                {"type": "contains", "value": "print", "message": "Print something"},
                {"type": "no_hardcoded_secrets", "message": "Keep secrets out of the file"},
            ],
        },
    ],

    # ── Baby 8: load_dotenv ──
    "baby-dotenv:main": [
        {
            "id": "bd1",
            "title": "Imports",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "Type all three. Click Analyze when done."
            ),
            "example": "import os\nimport requests\nfrom dotenv import load_dotenv",
            "checks": [
                {"type": "has_import", "module": "os", "message": "Import os"},
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv", "message": "Import load_dotenv"},
            ],
        },
        {
            "id": "bd2",
            "title": "Call load_dotenv()",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "load_dotenv()\n\n"
                "Add this right after imports so .env is loaded. Click Analyze when done."
            ),
            "example": "load_dotenv()",
            "checks": [
                {"type": "contains", "value": "load_dotenv()", "message": "Call load_dotenv()"},
            ],
        },
        {
            "id": "bd3",
            "title": "Load key + URL",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n\n'
                "Add both lines. Click Analyze when done."
            ),
            "example": (
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "checks": [
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "contains", "value": "SOURCE_API_URL", "message": "Load SOURCE_API_URL"},
                {"type": "contains", "value": "os.getenv", "message": "Use os.getenv()"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "bd4",
            "title": "GET with auth",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                'response = requests.get(f"{BASE}/v1/incidents", headers=headers, timeout=30)\n'
                "print(response.status_code)\n\n"
                "Add these three lines. Click Analyze when done."
            ),
            "example": (
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                'response = requests.get(f"{BASE}/v1/incidents", headers=headers, timeout=30)\n'
                "print(response.status_code)"
            ),
            "checks": [
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
                {"type": "contains", "value": "requests.get", "message": "GET request"},
                {"type": "contains", "value": "/v1/incidents", "message": "Hit incidents"},
                {"type": "contains", "value": "load_dotenv", "message": "Keep load_dotenv"},
            ],
        },
    ],

    # ── Baby 9: Query params ──
    "baby-params:main": [
        {
            "id": "bpp1",
            "title": "Setup + dotenv",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n\n'
                "Type the setup block. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "checks": [
                {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load API key"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "bpp2",
            "title": "Headers + params",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                'params = {"status": "open"}\n\n'
                "Add both dicts. Click Analyze when done."
            ),
            "example": 'headers = {"Authorization": f"Bearer {API_KEY}"}\nparams = {"status": "open"}',
            "checks": [
                {"type": "contains", "value": "params", "message": "Define params"},
                {"type": "contains", "value": "status", "message": "Filter status"},
                {"type": "contains", "value": "open", "message": "status=open"},
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
            ],
        },
        {
            "id": "bpp3",
            "title": "GET with params",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                "    params=params,\n"
                "    timeout=30,\n"
                ")\n\n"
                "Pass params= so the API filters. Click Analyze when done."
            ),
            "example": (
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                "    params=params,\n"
                "    timeout=30,\n"
                ")"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "params", "message": "Pass params="},
                {"type": "contains", "value": "/v1/incidents", "message": "Hit incidents"},
            ],
        },
        {
            "id": "bpp4",
            "title": "Print count",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "data = response.json()\n"
                'print(len(data["data"]))\n\n'
                "Add these lines. Click Analyze when done."
            ),
            "example": 'data = response.json()\nprint(len(data["data"]))',
            "checks": [
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
                {"type": "contains", "value": "len(", "message": "Print count with len()"},
                {"type": "contains", "value": "print", "message": "Print the count"},
            ],
        },
    ],

    # ── Baby 10: raise_for_status + count ──
    "baby-raise:main": [
        {
            "id": "br1",
            "title": "Imports + dotenv",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n\n"
                "Type imports + load_dotenv(). Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()"
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv()", "message": "Call load_dotenv()"},
            ],
        },
        {
            "id": "br2",
            "title": "Key, URL, headers",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n\n'
                "Add these three lines. Click Analyze when done."
            ),
            "example": (
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}'
            ),
            "checks": [
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "br3",
            "title": "GET open incidents",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n\n"
                "Add the GET. Click Analyze when done."
            ),
            "example": (
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "GET request"},
                {"type": "contains", "value": "params", "message": "Pass params"},
                {"type": "contains", "value": "open", "message": "status=open"},
            ],
        },
        {
            "id": "br4",
            "title": "raise_for_status()",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response.raise_for_status()\n\n"
                "Add this right after the get — fail loudly on 4xx/5xx. Click Analyze when done."
            ),
            "example": "response.raise_for_status()",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "Call raise_for_status()"},
            ],
        },
        {
            "id": "br5",
            "title": "Parse + count",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "data = response.json()\n"
                'print(len(data["data"]))\n\n'
                "Add these lines. Click Analyze when done."
            ),
            "example": 'data = response.json()\nprint(len(data["data"]))',
            "checks": [
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
                {"type": "contains", "value": 'data["data"]', "message": "Read data['data'] list"},
                {"type": "contains", "value": "len(", "message": "Use len() for count"},
                {"type": "contains", "value": "raise_for_status", "message": "Keep raise_for_status"},
            ],
        },
    ],

    # ── Baby 11: Loop fields ──
    "baby-loop:main": [
        {
            "id": "bl1",
            "title": "Setup imports",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n\n"
                "Type this setup. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()"
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv()", "message": "Call load_dotenv()"},
            ],
        },
        {
            "id": "bl2",
            "title": "Auth + GET + parse",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "data = response.json()\n\n"
                "Add auth through JSON parse. Click Analyze when done."
            ),
            "example": (
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "data = response.json()"
            ),
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "raise_for_status"},
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
                {"type": "contains", "value": "requests.get", "message": "GET request"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "bl3",
            "title": "for loop",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'for incident in data["data"]:\n'
                "    pass\n\n"
                "Add the for loop (pass is temporary). Click Analyze when done."
            ),
            "example": 'for incident in data["data"]:\n    pass',
            "checks": [
                {"type": "regex", "pattern": r"for\s+\w+\s+in\s+data", "message": "Loop over data"},
                {"type": "contains", "value": 'data["data"]', "message": "Iterate data['data']"},
            ],
        },
        {
            "id": "bl4",
            "title": "Print id",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'for incident in data["data"]:\n'
                '    print(incident["id"])\n\n'
                "Replace pass with printing id. Click Analyze when done."
            ),
            "example": 'for incident in data["data"]:\n    print(incident["id"])',
            "checks": [
                {"type": "regex", "pattern": r"for\s+\w+\s+in", "message": "Keep the for loop"},
                {"type": "contains", "value": '["id"]', "message": "Print id"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
        {
            "id": "bl5",
            "title": "Print id, severity, facility",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'for incident in data["data"]:\n'
                '    print(incident["id"], incident["severity"], incident["facility"])\n\n'
                "Expand the print to all three fields. Click Analyze when done."
            ),
            "example": (
                'for incident in data["data"]:\n'
                '    print(incident["id"], incident["severity"], incident["facility"])'
            ),
            "checks": [
                {"type": "regex", "pattern": r"for\s+\w+\s+in", "message": "Keep the for loop"},
                {"type": "contains", "value": '["id"]', "message": "Print id"},
                {"type": "contains", "value": "severity", "message": "Print severity"},
                {"type": "contains", "value": "facility", "message": "Print facility"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
    ],

    # ── py-vars: name/count/active ──
    "py-vars:main": [
        {
            "id": "pv1",
            "title": "String variable",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'name = "Acme Fleet"\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'name = "Acme Fleet"',
            "checks": [
                {"type": "contains", "value": "name", "message": "Create name variable"},
                {"type": "contains", "value": "Acme", "message": "Set name to Acme Fleet"},
            ],
        },
        {
            "id": "pv2",
            "title": "Number variable",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "count = 10\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "count = 10",
            "checks": [
                {"type": "contains", "value": "count", "message": "Create count variable"},
                {"type": "contains", "value": "10", "message": "Set count to 10"},
            ],
        },
        {
            "id": "pv3",
            "title": "Boolean variable",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "active = True\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "active = True",
            "checks": [
                {"type": "contains", "value": "active", "message": "Create active variable"},
                {"type": "contains", "value": "True", "message": "Set active to True"},
            ],
        },
        {
            "id": "pv4",
            "title": "Print all three",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "print(name)\n"
                "print(count)\n"
                "print(active)\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "print(name)\nprint(count)\nprint(active)",
            "checks": [
                {"type": "contains", "value": "print(name)", "message": "Print name"},
                {"type": "contains", "value": "print(count)", "message": "Print count"},
                {"type": "contains", "value": "print(active)", "message": "Print active"},
            ],
        },
    ],

    # ── py-dict: incident dictionary ──
    "py-dict:main": [
        {
            "id": "pd1",
            "title": "Start the dict",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incident = {\n"
                '    "id": "INC-38192",\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": 'incident = {\n    "id": "INC-38192",\n}',
            "checks": [
                {"type": "regex", "pattern": r"incident\s*=\s*\{", "message": "Create incident dict"},
                {"type": "contains", "value": "INC-38192", "message": "Include incident id"},
            ],
        },
        {
            "id": "pd2",
            "title": "Add severity + facility",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "severity": "critical",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "severity": "critical",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "severity", "message": "Include severity"},
                {"type": "contains", "value": "facility", "message": "Include facility"},
            ],
        },
        {
            "id": "pd3",
            "title": "Add message",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "severity": "critical",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "severity": "critical",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "message", "message": "Include message"},
                {"type": "contains", "value": "Pump", "message": "Include pump message text"},
            ],
        },
        {
            "id": "pd4",
            "title": "Print fields",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print(incident["id"])\n'
                'print(incident["severity"])\n'
                'print(incident["facility"])\n'
                'print(incident["message"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print(incident["id"])\n'
                'print(incident["severity"])\n'
                'print(incident["facility"])\n'
                'print(incident["message"])'
            ),
            "checks": [
                {"type": "contains", "value": 'incident["id"]', "message": "Print id"},
                {"type": "contains", "value": "severity", "message": "Print severity"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
    ],

    # ── py-list-loop ──
    "py-list-loop:main": [
        {
            "id": "pl1",
            "title": "List of 3 incidents",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incidents = [\n"
                '    {"id": "INC-001", "severity": "critical", "facility": "Plant A"},\n'
                '    {"id": "INC-002", "severity": "low", "facility": "Plant B"},\n'
                '    {"id": "INC-003", "severity": "high", "facility": "Plant C"},\n'
                "]\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incidents = [\n"
                '    {"id": "INC-001", "severity": "critical", "facility": "Plant A"},\n'
                '    {"id": "INC-002", "severity": "low", "facility": "Plant B"},\n'
                '    {"id": "INC-003", "severity": "high", "facility": "Plant C"},\n'
                "]"
            ),
            "checks": [
                {"type": "contains", "value": "incidents", "message": "Create incidents list"},
                {"type": "contains", "value": "INC-001", "message": "Include first incident"},
                {"type": "contains", "value": "INC-003", "message": "Include third incident"},
            ],
        },
        {
            "id": "pl2",
            "title": "for loop skeleton",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for item in incidents:\n"
                "    pass\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "for item in incidents:\n    pass",
            "checks": [
                {"type": "regex", "pattern": r"for\s+\w+\s+in\s+incidents", "message": "Loop over incidents"},
            ],
        },
        {
            "id": "pl3",
            "title": "Print each id",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for item in incidents:\n"
                '    print(item["id"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'for item in incidents:\n    print(item["id"])',
            "checks": [
                {"type": "regex", "pattern": r"for\s+\w+\s+in\s+incidents", "message": "Keep the for loop"},
                {"type": "contains", "value": '["id"]', "message": "Print each id"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
        {
            "id": "pl4",
            "title": "Confirm three ids",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for item in incidents:\n"
                '    print(item["id"])\n\n'
                "Keep that loop. Click Analyze (or Run) — you should see three ids."
            ),
            "example": 'for item in incidents:\n    print(item["id"])',
            "checks": [
                {"type": "contains", "value": "INC-001", "message": "Keep INC-001 in the list"},
                {"type": "contains", "value": "INC-002", "message": "Keep INC-002 in the list"},
                {"type": "contains", "value": "INC-003", "message": "Keep INC-003 in the list"},
                {"type": "contains", "value": "print", "message": "Print inside the loop"},
            ],
        },
    ],

    # ── py-if ──
    "py-if:main": [
        {
            "id": "pi1",
            "title": "Incidents list",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incidents = [\n"
                '    {"id": "INC-001", "severity": "critical"},\n'
                '    {"id": "INC-002", "severity": "low"},\n'
                '    {"id": "INC-003", "severity": "high"},\n'
                "]\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incidents = [\n"
                '    {"id": "INC-001", "severity": "critical"},\n'
                '    {"id": "INC-002", "severity": "low"},\n'
                '    {"id": "INC-003", "severity": "high"},\n'
                "]"
            ),
            "checks": [
                {"type": "contains", "value": "incidents", "message": "Create incidents list"},
                {"type": "contains", "value": "critical", "message": "Include critical"},
            ],
        },
        {
            "id": "pi2",
            "title": "SYNC_SEVERITIES set",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'SYNC_SEVERITIES = {"critical", "high"}\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = {"critical", "high"}',
            "checks": [
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Define SYNC_SEVERITIES"},
                {"type": "contains", "value": "critical", "message": "Include critical"},
                {"type": "contains", "value": "high", "message": "Include high"},
            ],
        },
        {
            "id": "pi3",
            "title": "if filter loop",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for item in incidents:\n"
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(item["id"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "for item in incidents:\n"
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(item["id"])'
            ),
            "checks": [
                {"type": "contains", "value": "if ", "message": "Use if"},
                {"type": "contains", "value": "in SYNC_SEVERITIES", "message": "Check membership in SYNC_SEVERITIES"},
                {"type": "contains", "value": "print", "message": "Print matching ids"},
            ],
        },
        {
            "id": "pi4",
            "title": "Only critical and high",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for item in incidents:\n"
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(item["id"])\n\n'
                "Keep that filter. Click Analyze — only INC-001 and INC-003 should print."
            ),
            "example": (
                "for item in incidents:\n"
                '    if item["severity"] in SYNC_SEVERITIES:\n'
                '        print(item["id"])'
            ),
            "checks": [
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Keep SYNC_SEVERITIES"},
                {"type": "contains", "value": "if ", "message": "Keep the if filter"},
                {"type": "contains", "value": "print", "message": "Keep print"},
            ],
        },
    ],

    # ── py-function ──
    "py-function:main": [
        {
            "id": "pf1",
            "title": "Define the function",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def severity_to_priority(severity):\n"
                "    pass\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "def severity_to_priority(severity):\n    pass",
            "checks": [
                {"type": "has_function", "name": "severity_to_priority", "message": "Define severity_to_priority()"},
            ],
        },
        {
            "id": "pf2",
            "title": "Map critical and high",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                "    return 4\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                "    return 4"
            ),
            "checks": [
                {"type": "has_function", "name": "severity_to_priority", "message": "Keep severity_to_priority()"},
                {"type": "contains", "value": "return 1", "message": "critical → 1"},
                {"type": "contains", "value": "return 2", "message": "high → 2"},
            ],
        },
        {
            "id": "pf3",
            "title": "Add medium",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                '    if severity == "medium":\n'
                "        return 3\n"
                "    return 4\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                '    if severity == "medium":\n'
                "        return 3\n"
                "    return 4"
            ),
            "checks": [
                {"type": "contains", "value": "medium", "message": "Handle medium"},
                {"type": "contains", "value": "return 3", "message": "medium → 3"},
                {"type": "contains", "value": "return 4", "message": "Default return 4"},
            ],
        },
        {
            "id": "pf4",
            "title": "Call the function",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print(severity_to_priority("critical"))\n'
                'print(severity_to_priority("high"))\n'
                'print(severity_to_priority("low"))\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print(severity_to_priority("critical"))\n'
                'print(severity_to_priority("high"))\n'
                'print(severity_to_priority("low"))'
            ),
            "checks": [
                {"type": "contains", "value": "severity_to_priority(", "message": "Call severity_to_priority"},
                {"type": "contains", "value": "print", "message": "Print the results"},
            ],
        },
    ],

    # ── py-transform ──
    "py-transform:main": [
        {
            "id": "pt1",
            "title": "Incident dict",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}"
            ),
            "checks": [
                {"type": "regex", "pattern": r"incident\s*=\s*\{", "message": "Create incident dict"},
                {"type": "contains", "value": "facility", "message": "Include facility"},
            ],
        },
        {
            "id": "pt2",
            "title": "severity_to_priority helper",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                '    if severity == "medium":\n'
                "        return 3\n"
                "    return 4\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def severity_to_priority(severity):\n"
                '    if severity == "critical":\n'
                "        return 1\n"
                '    if severity == "high":\n'
                "        return 2\n"
                '    if severity == "medium":\n'
                "        return 3\n"
                "    return 4"
            ),
            "checks": [
                {"type": "has_function", "name": "severity_to_priority", "message": "Define severity_to_priority()"},
            ],
        },
        {
            "id": "pt3",
            "title": "transform_incident",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def transform_incident(inc):\n"
                "    return {\n"
                '        "external_id": inc["id"],\n'
                '        "site": inc["facility"],\n'
                '        "description": inc.get("message", "No description"),\n'
                '        "priority": severity_to_priority(inc["severity"]),\n'
                "    }\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def transform_incident(inc):\n"
                "    return {\n"
                '        "external_id": inc["id"],\n'
                '        "site": inc["facility"],\n'
                '        "description": inc.get("message", "No description"),\n'
                '        "priority": severity_to_priority(inc["severity"]),\n'
                "    }"
            ),
            "checks": [
                {"type": "has_function", "name": "transform_incident", "message": "Define transform_incident()"},
                {"type": "contains", "value": "external_id", "message": "Map external_id"},
                {"type": "contains", "value": "site", "message": "Map site"},
                {"type": "contains", "value": "priority", "message": "Map priority"},
            ],
        },
        {
            "id": "pt4",
            "title": "Call and print",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "ticket = transform_incident(incident)\n"
                "print(ticket)\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "ticket = transform_incident(incident)\nprint(ticket)",
            "checks": [
                {"type": "contains", "value": "transform_incident(", "message": "Call transform_incident"},
                {"type": "contains", "value": "print", "message": "Print the ticket"},
            ],
        },
    ],


    # ── filter-fetch ──
    "filter-fetch:main": [
        {
            "id": "ff1",
            "title": "Imports + dotenv",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()"
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv()", "message": "Call load_dotenv()"},
            ],
        },
        {
            "id": "ff2",
            "title": "Load key and URL",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}'
            ),
            "checks": [
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "contains", "value": "Bearer", "message": "Bearer auth header"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "ff3",
            "title": "GET open incidents",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "open", "message": "status=open"},
                {"type": "contains", "value": "raise_for_status", "message": "raise_for_status"},
            ],
        },
        {
            "id": "ff4",
            "title": "Print count",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "data = response.json()\n"
                'print("Count:", len(data["data"]))\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'data = response.json()\nprint("Count:", len(data["data"]))',
            "checks": [
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
                {"type": "contains", "value": "len(", "message": "Use len() for count"},
                {"type": "contains", "value": "print", "message": "Print the count"},
            ],
        },
    ],

    # ── filter-python ──
    "filter-python:main": [
        {
            "id": "fp1",
            "title": "Setup + GET",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'incidents = response.json()["data"]\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'incidents = response.json()["data"]'
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "GET incidents"},
                {"type": "contains", "value": "incidents", "message": "Store incidents list"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "fp2",
            "title": "SYNC_SEVERITIES",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'SYNC_SEVERITIES = {"critical", "high"}\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'SYNC_SEVERITIES = {"critical", "high"}',
            "checks": [
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Define SYNC_SEVERITIES"},
            ],
        },
        {
            "id": "fp3",
            "title": "Filter in a list",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "urgent = [\n"
                "    i for i in incidents\n"
                '    if i["severity"] in SYNC_SEVERITIES\n'
                "]\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "urgent = [\n"
                "    i for i in incidents\n"
                '    if i["severity"] in SYNC_SEVERITIES\n'
                "]"
            ),
            "checks": [
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Filter with SYNC_SEVERITIES"},
                {"type": "contains", "value": "severity", "message": "Check severity"},
            ],
        },
        {
            "id": "fp4",
            "title": "Print filtered count",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Urgent count:", len(urgent))\n'
                "for i in urgent:\n"
                '    print(i["id"], i["severity"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Urgent count:", len(urgent))\n'
                "for i in urgent:\n"
                '    print(i["id"], i["severity"])'
            ),
            "checks": [
                {"type": "contains", "value": "len(urgent)", "message": "Print urgent count"},
                {"type": "contains", "value": "print", "message": "Print each urgent incident"},
            ],
        },
    ],

    # ── filter-api ──
    "filter-api:main": [
        {
            "id": "fa1",
            "title": "Setup",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'headers = {"Authorization": f"Bearer {API_KEY}"}'
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "fa2",
            "title": "severity=critical param",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open", "severity": "critical"},\n'
                "    timeout=30,\n"
                ")\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                "    headers=headers,\n"
                '    params={"status": "open", "severity": "critical"},\n'
                "    timeout=30,\n"
                ")"
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "GET request"},
                {"type": "contains", "value": "severity", "message": "Pass severity param"},
                {"type": "contains", "value": "critical", "message": "severity=critical"},
            ],
        },
        {
            "id": "fa3",
            "title": "raise_for_status",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response.raise_for_status()\n"
                "data = response.json()\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "response.raise_for_status()\ndata = response.json()",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "raise_for_status"},
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
            ],
        },
        {
            "id": "fa4",
            "title": "Print results",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Critical open:", len(data["data"]))\n'
                'for i in data["data"]:\n'
                '    print(i["id"], i["severity"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Critical open:", len(data["data"]))\n'
                'for i in data["data"]:\n'
                '    print(i["id"], i["severity"])'
            ),
            "checks": [
                {"type": "contains", "value": "len(", "message": "Print count"},
                {"type": "contains", "value": "print", "message": "Print each incident"},
            ],
        },
    ],

    # ── filter-facility ──
    "filter-facility:main": [
        {
            "id": "fc1",
            "title": "Setup + GET open",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {API_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'incidents = response.json()["data"]\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {API_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'incidents = response.json()["data"]'
            ),
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "GET incidents"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "fc2",
            "title": "Keyword constant",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'KEYWORD = "Water Treatment"\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'KEYWORD = "Water Treatment"',
            "checks": [
                {"type": "contains", "value": "Water Treatment", "message": "Define Water Treatment keyword"},
            ],
        },
        {
            "id": "fc3",
            "title": "Filter by facility",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "matches = [\n"
                "    i for i in incidents\n"
                '    if KEYWORD in i.get("facility", "")\n'
                "]\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "matches = [\n"
                "    i for i in incidents\n"
                '    if KEYWORD in i.get("facility", "")\n'
                "]"
            ),
            "checks": [
                {"type": "contains", "value": "facility", "message": "Check facility field"},
                {"type": "contains", "value": "KEYWORD", "message": "Use KEYWORD in filter"},
            ],
        },
        {
            "id": "fc4",
            "title": "Print matches",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Matches:", len(matches))\n'
                "for i in matches:\n"
                '    print(i["id"], i["facility"])\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Matches:", len(matches))\n'
                "for i in matches:\n"
                '    print(i["id"], i["facility"])'
            ),
            "checks": [
                {"type": "contains", "value": "len(matches)", "message": "Print match count"},
                {"type": "contains", "value": "facility", "message": "Print facility"},
            ],
        },
    ],


    # ── sync-transform (no HTTP) ──
    "sync-transform:main": [
        {
            "id": "st1",
            "title": "One incident dict",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "incident = {\n"
                '    "id": "INC-38192",\n'
                '    "facility": "Water Treatment Plant 4",\n'
                '    "severity": "critical",\n'
                '    "message": "Pump pressure below threshold",\n'
                "}"
            ),
            "checks": [
                {"type": "regex", "pattern": r"incident\s*=\s*\{", "message": "Create incident dict"},
                {"type": "contains", "value": "INC-38192", "message": "Include id"},
            ],
        },
        {
            "id": "st2",
            "title": "priority_map",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "priority_map = {\n"
                '    "critical": 1,\n'
                '    "high": 2,\n'
                '    "medium": 3,\n'
                '    "low": 4,\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "priority_map = {\n"
                '    "critical": 1,\n'
                '    "high": 2,\n'
                '    "medium": 3,\n'
                '    "low": 4,\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "priority_map", "message": "Create priority_map"},
                {"type": "contains", "value": "critical", "message": "Map critical"},
            ],
        },
        {
            "id": "st3",
            "title": "Build ticket payload",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "ticket = {\n"
                '    "external_id": incident["id"],\n'
                '    "site": incident["facility"],\n'
                '    "description": incident["message"],\n'
                '    "priority": priority_map[incident["severity"]],\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "ticket = {\n"
                '    "external_id": incident["id"],\n'
                '    "site": incident["facility"],\n'
                '    "description": incident["message"],\n'
                '    "priority": priority_map[incident["severity"]],\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "external_id", "message": "Map external_id"},
                {"type": "contains", "value": "site", "message": "Map site"},
                {"type": "contains", "value": "priority", "message": "Map priority"},
                {"type": "not_contains", "value": "requests.", "message": "No HTTP in this lesson"},
            ],
        },
        {
            "id": "st4",
            "title": "Print ticket",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "print(ticket)\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "print(ticket)",
            "checks": [
                {"type": "contains", "value": "print(ticket)", "message": "Print the ticket payload"},
            ],
        },
    ],

    # ── sync-post-one ──
    "sync-post-one:main": [
        {
            "id": "spo1",
            "title": "Imports + dest env",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")'
            ),
            "checks": [
                {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Load DESTINATION_API_KEY"},
                {"type": "contains", "value": "5002", "message": "Point at dest port 5002"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "spo2",
            "title": "Ticket payload",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "payload = {\n"
                '    "external_id": "INC-TRAIN-001",\n'
                '    "site": "Training Plant",\n'
                '    "description": "Postman/Python drill ticket",\n'
                '    "priority": 2,\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "payload = {\n"
                '    "external_id": "INC-TRAIN-001",\n'
                '    "site": "Training Plant",\n'
                '    "description": "Postman/Python drill ticket",\n'
                '    "priority": 2,\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "external_id", "message": "Include external_id"},
                {"type": "contains", "value": "payload", "message": "Create payload dict"},
            ],
        },
        {
            "id": "spo3",
            "title": "POST the ticket",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response = requests.post(\n"
                '    f"{DEST_URL}/v1/tickets",\n'
                '    headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "    json=payload,\n"
                "    timeout=30,\n"
                ")\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "response = requests.post(\n"
                '    f"{DEST_URL}/v1/tickets",\n'
                '    headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "    json=payload,\n"
                "    timeout=30,\n"
                ")"
            ),
            "checks": [
                {"type": "contains", "value": "requests.post", "message": "Use requests.post()"},
                {"type": "contains", "value": "json=payload", "message": "Send json=payload"},
                {"type": "contains", "value": "/v1/tickets", "message": "POST to /v1/tickets"},
            ],
        },
        {
            "id": "spo4",
            "title": "Check status",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "response.raise_for_status()\n"
                "print(response.status_code)\n"
                "print(response.json())\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "response.raise_for_status()\n"
                "print(response.status_code)\n"
                "print(response.json())"
            ),
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "raise_for_status"},
                {"type": "contains", "value": "status_code", "message": "Print status_code"},
            ],
        },
    ],

    # ── sync-409 ──
    "sync-409:main": [
        {
            "id": "s4091",
            "title": "Setup + payload",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "payload = {\n"
                '    "external_id": "INC-DUP-001",\n'
                '    "site": "Dup Drill",\n'
                '    "description": "First create, then duplicate",\n'
                '    "priority": 1,\n'
                "}\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "payload = {\n"
                '    "external_id": "INC-DUP-001",\n'
                '    "site": "Dup Drill",\n'
                '    "description": "First create, then duplicate",\n'
                '    "priority": 1,\n'
                "}"
            ),
            "checks": [
                {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Load dest key"},
                {"type": "contains", "value": "INC-DUP-001", "message": "Use fixed external_id"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "s4092",
            "title": "create_ticket helper",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def create_ticket(payload):\n"
                "    response = requests.post(\n"
                '        f"{DEST_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "        json=payload,\n"
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    return response.json()\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def create_ticket(payload):\n"
                "    response = requests.post(\n"
                '        f"{DEST_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "        json=payload,\n"
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    return response.json()"
            ),
            "checks": [
                {"type": "has_function", "name": "create_ticket", "message": "Define create_ticket()"},
                {"type": "contains", "value": "requests.post", "message": "POST inside helper"},
            ],
        },
        {
            "id": "s4093",
            "title": "First POST (create)",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "try:\n"
                "    create_ticket(payload)\n"
                '    print("CREATED")\n'
                "except requests.HTTPError as e:\n"
                "    if e.response.status_code == 409:\n"
                '        print("SKIP")\n'
                "    else:\n"
                "        raise\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "try:\n"
                "    create_ticket(payload)\n"
                '    print("CREATED")\n'
                "except requests.HTTPError as e:\n"
                "    if e.response.status_code == 409:\n"
                '        print("SKIP")\n'
                "    else:\n"
                "        raise"
            ),
            "checks": [
                {"type": "contains", "value": "HTTPError", "message": "Catch HTTPError"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP on duplicate"},
            ],
        },
        {
            "id": "s4094",
            "title": "Second POST (duplicate)",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "# post again with the same external_id\n"
                "try:\n"
                "    create_ticket(payload)\n"
                '    print("CREATED")\n'
                "except requests.HTTPError as e:\n"
                "    if e.response.status_code == 409:\n"
                '        print("SKIP")\n'
                "    else:\n"
                "        raise\n\n"
                "Duplicate the try/except block so you POST twice. Click Analyze when done."
            ),
            "example": (
                "try:\n"
                "    create_ticket(payload)\n"
                '    print("CREATED")\n'
                "except requests.HTTPError as e:\n"
                "    if e.response.status_code == 409:\n"
                '        print("SKIP")\n'
                "    else:\n"
                "        raise\n\n"
                "try:\n"
                "    create_ticket(payload)\n"
                '    print("CREATED")\n'
                "except requests.HTTPError as e:\n"
                "    if e.response.status_code == 409:\n"
                '        print("SKIP")\n'
                "    else:\n"
                "        raise"
            ),
            "checks": [
                {"type": "contains", "value": "409", "message": "Keep 409 handling"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP"},
                {"type": "contains", "value": "create_ticket", "message": "Call create_ticket twice"},
            ],
        },
    ],

    # ── sync-loop ──
    "sync-loop:main": [
        {
            "id": "sl1",
            "title": "Config both APIs",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                'SYNC_SEVERITIES = {"critical", "high"}\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                'SYNC_SEVERITIES = {"critical", "high"}'
            ),
            "checks": [
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Source key"},
                {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Dest key"},
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "SYNC_SEVERITIES set"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "sl2",
            "title": "transform_incident",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def transform_incident(incident):\n"
                "    priority_map = {\n"
                '        "critical": 1, "high": 2, "medium": 3, "low": 4,\n'
                "    }\n"
                "    return {\n"
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                "    }\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def transform_incident(incident):\n"
                "    priority_map = {\n"
                '        "critical": 1, "high": 2, "medium": 3, "low": 4,\n'
                "    }\n"
                "    return {\n"
                '        "external_id": incident["id"],\n'
                '        "site": incident["facility"],\n'
                '        "description": incident["message"],\n'
                '        "priority": priority_map[incident["severity"]],\n'
                "    }"
            ),
            "checks": [
                {"type": "has_function", "name": "transform_incident", "message": "Define transform_incident()"},
                {"type": "contains", "value": "external_id", "message": "Map external_id"},
            ],
        },
        {
            "id": "sl3",
            "title": "Fetch + create helpers",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def fetch_open_incidents():\n"
                "    response = requests.get(\n"
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                '    return response.json()["data"]\n\n'
                "def create_ticket(payload):\n"
                "    response = requests.post(\n"
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                "        json=payload,\n"
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    return response.json()\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def fetch_open_incidents():\n"
                "    response = requests.get(\n"
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"status": "open"},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                '    return response.json()["data"]\n\n'
                "def create_ticket(payload):\n"
                "    response = requests.post(\n"
                '        f"{DESTINATION_API_URL}/v1/tickets",\n'
                '        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},\n'
                "        json=payload,\n"
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    return response.json()"
            ),
            "checks": [
                {"type": "has_function", "name": "fetch_open_incidents", "message": "Define fetch_open_incidents()"},
                {"type": "has_function", "name": "create_ticket", "message": "Define create_ticket()"},
            ],
        },
        {
            "id": "sl4",
            "title": "Sync loop with 409",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "for incident in fetch_open_incidents():\n"
                '    if incident["severity"] not in SYNC_SEVERITIES:\n'
                "        continue\n"
                "    ticket = transform_incident(incident)\n"
                "    try:\n"
                "        create_ticket(ticket)\n"
                '        print("CREATED", incident["id"])\n'
                "    except requests.HTTPError as e:\n"
                "        if e.response.status_code == 409:\n"
                '            print("SKIP", incident["id"])\n'
                "        else:\n"
                "            raise\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "for incident in fetch_open_incidents():\n"
                '    if incident["severity"] not in SYNC_SEVERITIES:\n'
                "        continue\n"
                "    ticket = transform_incident(incident)\n"
                "    try:\n"
                "        create_ticket(ticket)\n"
                '        print("CREATED", incident["id"])\n'
                "    except requests.HTTPError as e:\n"
                "        if e.response.status_code == 409:\n"
                '            print("SKIP", incident["id"])\n'
                "        else:\n"
                "            raise"
            ),
            "checks": [
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Filter by SYNC_SEVERITIES"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP on duplicate"},
                {"type": "contains", "value": "transform_incident", "message": "Transform before POST"},
            ],
        },
    ],


    # ── page-loop ──
    "page-loop:main": [
        {
            "id": "pg1",
            "title": "Setup",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "pg2",
            "title": "Start page loop",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "all_records = []\n"
                "page = 1\n"
                "while True:\n"
                "    pass\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": "all_records = []\npage = 1\nwhile True:\n    pass",
            "checks": [
                {"type": "contains", "value": "while", "message": "Use while loop"},
                {"type": "contains", "value": "all_records", "message": "Accumulate in all_records"},
            ],
        },
        {
            "id": "pg3",
            "title": "GET with limit=2",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "all_records = []\n"
                "page = 1\n"
                "while True:\n"
                "    response = requests.get(\n"
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"page": page, "limit": 2},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    body = response.json()\n"
                '    all_records.extend(body["data"])\n'
                '    if not body["pagination"]["has_more"]:\n'
                "        break\n"
                "    page += 1\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "all_records = []\n"
                "page = 1\n"
                "while True:\n"
                "    response = requests.get(\n"
                '        f"{SOURCE_API_URL}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                '        params={"page": page, "limit": 2},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    body = response.json()\n"
                '    all_records.extend(body["data"])\n'
                '    if not body["pagination"]["has_more"]:\n'
                "        break\n"
                "    page += 1"
            ),
            "checks": [
                {"type": "contains", "value": "limit", "message": "Pass limit param"},
                {"type": "contains", "value": "has_more", "message": "Check has_more"},
                {"type": "contains", "value": "extend", "message": "extend all_records"},
                {"type": "contains", "value": "page +=", "message": "Increment page"},
            ],
        },
        {
            "id": "pg4",
            "title": "Print total",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Total:", len(all_records))\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print("Total:", len(all_records))',
            "checks": [
                {"type": "contains", "value": "len(all_records)", "message": "Print total with len()"},
                {"type": "contains", "value": "print", "message": "Print the total"},
            ],
        },
    ],

    # ── err-safe-get ──
    "err-safe-get:main": [
        {
            "id": "es1",
            "title": "Setup",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "import os\n"
                "import requests\n"
                "from dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")\n'
                'SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")'
            ),
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
            ],
        },
        {
            "id": "es2",
            "title": "safe_get_incident",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                "def safe_get_incident(incident_id):\n"
                "    try:\n"
                "        response = requests.get(\n"
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                "            timeout=30,\n"
                "        )\n"
                "        response.raise_for_status()\n"
                "        return response.json()\n"
                "    except requests.Timeout:\n"
                "        return None\n"
                "    except requests.HTTPError as e:\n"
                "        if e.response.status_code == 404:\n"
                '            print(f"{incident_id} not found")\n'
                "        return None\n\n"
                "Now type it. Click Analyze when done."
            ),
            "example": (
                "def safe_get_incident(incident_id):\n"
                "    try:\n"
                "        response = requests.get(\n"
                '            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",\n'
                '            headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},\n'
                "            timeout=30,\n"
                "        )\n"
                "        response.raise_for_status()\n"
                "        return response.json()\n"
                "    except requests.Timeout:\n"
                "        return None\n"
                "    except requests.HTTPError as e:\n"
                "        if e.response.status_code == 404:\n"
                '            print(f"{incident_id} not found")\n'
                "        return None"
            ),
            "checks": [
                {"type": "has_function", "name": "safe_get_incident", "message": "Define safe_get_incident()"},
                {"type": "contains", "value": "try:", "message": "Use try/except"},
                {"type": "contains", "value": "404", "message": "Handle 404"},
                {"type": "contains", "value": "HTTPError", "message": "Catch HTTPError"},
            ],
        },
        {
            "id": "es3",
            "title": "Try a real ID",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print(safe_get_incident("INC-38192"))\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print(safe_get_incident("INC-38192"))',
            "checks": [
                {"type": "contains", "value": "INC-38192", "message": "Look up INC-38192"},
                {"type": "contains", "value": "safe_get_incident", "message": "Call safe_get_incident"},
            ],
        },
        {
            "id": "es4",
            "title": "Try a missing ID",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print(safe_get_incident("INC-38192"))\n'
                'print(safe_get_incident("INC-99999"))\n\n'
                "Add the missing-ID call. Click Analyze when done."
            ),
            "example": (
                'print(safe_get_incident("INC-38192"))\n'
                'print(safe_get_incident("INC-99999"))'
            ),
            "checks": [
                {"type": "contains", "value": "INC-38192", "message": "Keep real ID lookup"},
                {"type": "contains", "value": "INC-99999", "message": "Look up missing INC-99999"},
            ],
        },
    ],

    # ── doc-readme ──
    "doc-readme:main": [
        {
            "id": "dr1",
            "title": "Purpose section",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("## Purpose")\n'
                'print("Sync critical/high open incidents into work-order tickets.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("## Purpose")\n'
                'print("Sync critical/high open incidents into work-order tickets.")'
            ),
            "checks": [
                {"type": "contains", "value": "Purpose", "message": "Print Purpose section"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
        {
            "id": "dr2",
            "title": "Env vars section",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("## Env vars")\n'
                'print("SOURCE_API_KEY, SOURCE_API_URL, DESTINATION_API_KEY, DESTINATION_API_URL")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("## Env vars")\n'
                'print("SOURCE_API_KEY, SOURCE_API_URL, DESTINATION_API_KEY, DESTINATION_API_URL")'
            ),
            "checks": [
                {"type": "contains", "value": "Env vars", "message": "Print Env vars section"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "List SOURCE_API_KEY"},
                {"type": "contains", "value": "DESTINATION_API_KEY", "message": "List DESTINATION_API_KEY"},
            ],
        },
        {
            "id": "dr3",
            "title": "Field mapping section",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("## Field mapping")\n'
                'print("id -> external_id")\n'
                'print("facility -> site")\n'
                'print("message -> description")\n'
                'print("severity -> priority")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("## Field mapping")\n'
                'print("id -> external_id")\n'
                'print("facility -> site")\n'
                'print("message -> description")\n'
                'print("severity -> priority")'
            ),
            "checks": [
                {"type": "contains", "value": "Field mapping", "message": "Print Field mapping section"},
                {"type": "contains", "value": "external_id", "message": "Map to external_id"},
                {"type": "contains", "value": "priority", "message": "Map severity to priority"},
            ],
        },
        {
            "id": "dr4",
            "title": "Errors section",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("## Errors")\n'
                'print("409 Conflict = ticket already exists — skip and continue")\n'
                'print("404 Not Found = missing incident — log and continue")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("## Errors")\n'
                'print("409 Conflict = ticket already exists — skip and continue")\n'
                'print("404 Not Found = missing incident — log and continue")'
            ),
            "checks": [
                {"type": "contains", "value": "Errors", "message": "Print Errors section"},
                {"type": "contains", "value": "409", "message": "Document 409"},
                {"type": "contains", "value": "404", "message": "Document 404"},
            ],
        },
    ],

    # ── demo-discovery ──
    "demo-discovery:main": [
        {
            "id": "dd1",
            "title": "Q1 — Current process",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Q1: How do alerts become work today?")\n'
                'print("A1: Ops copy/paste from monitoring into the CMMS by hand.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Q1: How do alerts become work today?")\n'
                'print("A1: Ops copy/paste from monitoring into the CMMS by hand.")'
            ),
            "checks": [
                {"type": "contains", "value": "Q1", "message": "Print Q1"},
                {"type": "contains", "value": "A1", "message": "Print A1"},
            ],
        },
        {
            "id": "dd2",
            "title": "Q2 — Pain",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Q2: What breaks when volume spikes?")\n'
                'print("A2: Critical alerts get delayed or duplicated tickets.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Q2: What breaks when volume spikes?")\n'
                'print("A2: Critical alerts get delayed or duplicated tickets.")'
            ),
            "checks": [
                {"type": "contains", "value": "Q2", "message": "Print Q2"},
                {"type": "contains", "value": "A2", "message": "Print A2"},
            ],
        },
        {
            "id": "dd3",
            "title": "Q3 — Success criteria",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Q3: What does success look like in 30 days?")\n'
                'print("A3: Critical/high open incidents auto-create tickets with no duplicates.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Q3: What does success look like in 30 days?")\n'
                'print("A3: Critical/high open incidents auto-create tickets with no duplicates.")'
            ),
            "checks": [
                {"type": "contains", "value": "Q3", "message": "Print Q3"},
                {"type": "contains", "value": "A3", "message": "Print A3"},
            ],
        },
        {
            "id": "dd4",
            "title": "Q4 — Systems",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("Q4: Which systems must talk?")\n'
                'print("A4: Monitoring API (source) and CMMS tickets API (destination).")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": (
                'print("Q4: Which systems must talk?")\n'
                'print("A4: Monitoring API (source) and CMMS tickets API (destination).")'
            ),
            "checks": [
                {"type": "contains", "value": "Q4", "message": "Print Q4"},
                {"type": "contains", "value": "A4", "message": "Print A4"},
                {"type": "contains", "value": "source", "message": "Mention source"},
                {"type": "contains", "value": "destination", "message": "Mention destination"},
            ],
        },
    ],

    # ── demo-talktrack ──
    "demo-talktrack:main": [
        {
            "id": "dt1",
            "title": "Problem",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("PROBLEM: Manual copy/paste from alerts to tickets wastes time and misses criticals.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print("PROBLEM: Manual copy/paste from alerts to tickets wastes time and misses criticals.")',
            "checks": [
                {"type": "contains", "value": "PROBLEM", "message": "Print PROBLEM line"},
                {"type": "contains", "value": "print", "message": "Use print()"},
            ],
        },
        {
            "id": "dt2",
            "title": "Success criteria",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("SUCCESS: Critical/high open incidents become tickets automatically; 409s are skipped.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print("SUCCESS: Critical/high open incidents become tickets automatically; 409s are skipped.")',
            "checks": [
                {"type": "contains", "value": "SUCCESS", "message": "Print SUCCESS line"},
                {"type": "contains", "value": "409", "message": "Mention 409 handling"},
            ],
        },
        {
            "id": "dt3",
            "title": "Demo steps",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("DEMO STEPS: 1) GET open incidents 2) Filter critical/high 3) Transform 4) POST tickets")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print("DEMO STEPS: 1) GET open incidents 2) Filter critical/high 3) Transform 4) POST tickets")',
            "checks": [
                {"type": "contains", "value": "DEMO STEPS", "message": "Print DEMO STEPS line"},
                {"type": "contains", "value": "GET", "message": "Mention GET"},
                {"type": "contains", "value": "POST", "message": "Mention POST"},
            ],
        },
        {
            "id": "dt4",
            "title": "Close",
            "instruction": (
                "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
                "EXAMPLE:\n"
                'print("CLOSE: Next step is a 2-week POC on one site with shared success metrics.")\n\n'
                "Now type it. Click Analyze when done."
            ),
            "example": 'print("CLOSE: Next step is a 2-week POC on one site with shared success metrics.")',
            "checks": [
                {"type": "contains", "value": "CLOSE", "message": "Print CLOSE line"},
                {"type": "contains", "value": "POC", "message": "Mention POC next step"},
            ],
        },
    ],
}

try:
    from mastery_steps import MASTERY_STEPS
except ImportError:  # pragma: no cover
    from course.mastery_steps import MASTERY_STEPS

LESSON_STEPS.update(MASTERY_STEPS)

