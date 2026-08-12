"""Mastery-gate, docs/Postman bridge, and SE explain steps — merged into LESSON_STEPS."""


def _step(step_id, title, instruction, example, checks, why="", common_mistake="", context=""):
    return {
        "id": step_id,
        "title": title,
        "instruction": instruction,
        "example": example,
        "context": context,
        "why": why,
        "common_mistake": common_mistake,
        "reveal_after_fails": 2,
        "checks": checks,
    }


def _look(example_body, extra=""):
    return (
        "Here's exactly what to type (look, then type it yourself — don't paste):\n\n"
        "EXAMPLE:\n"
        f"{example_body}\n\n"
        f"{extra}Click Analyze when done."
    )


def _exam(example_body, extra=""):
    return (
        "EXAM MODE — examples are hidden until you fail Analyze twice. Build it yourself.\n\n"
        "Target shape (for reveal):\n"
        f"{example_body}\n\n"
        f"{extra}Click Analyze when done."
    )


MASTERY_STEPS = {
    # ── review-http-python ──
    "review-http-python:main": [
        _step(
            "rh1",
            "Imports + dotenv",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\nload_dotenv()"
            ),
            "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\nload_dotenv()",
            [
                {"type": "has_import", "module": "os", "message": "Import os"},
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
            ],
            why="Review starts with the same setup every production script needs.",
            common_mistake="Forgetting load_dotenv() so getenv returns None.",
        ),
        _step(
            "rh2",
            "Health check",
            _look(
                'health = requests.get("http://127.0.0.1:5001/health", timeout=30)\n'
                "print(health.status_code)"
            ),
            'health = requests.get("http://127.0.0.1:5001/health", timeout=30)\nprint(health.status_code)',
            [
                {"type": "contains", "value": "/health", "message": "Hit /health"},
                {"type": "contains", "value": "5001", "message": "Use port 5001"},
                {"type": "not_contains", "value": "Authorization", "message": "Health needs no auth"},
            ],
            why="Health proves the API is up before you chase auth bugs.",
            common_mistake="Putting Bearer on /health (unnecessary and confusing).",
        ),
        _step(
            "rh3",
            "Open incidents",
            _look(
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("OPEN", len(response.json()["data"]))'
            ),
            (
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("OPEN", len(response.json()["data"]))'
            ),
            [
                {"type": "contains", "value": "os.getenv", "message": "Load key from env"},
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
                {"type": "contains", "value": "status", "message": "Filter status=open"},
                {"type": "contains", "value": "raise_for_status", "message": "Fail loudly"},
                {"type": "output_contains", "value": "OPEN", "message": "Print OPEN count"},
            ],
            why="Open-incident list is the core SE demo GET.",
            common_mistake="Hardcoding the API key instead of getenv.",
        ),
    ],

    # ── debug-first-request ──
    "debug-first-request:main": [
        _step(
            "df1",
            "Spot the wrong port",
            (
                "Starter is broken on purpose (wrong port 5999). Apply the debug ritual:\n"
                "read the error → check URL/port → fix one thing.\n\n"
                "EXAMPLE (fixed URL):\n"
                'response = requests.get("http://127.0.0.1:5001/health", timeout=30)\n\n'
                "Change 5999 → 5001. Click Analyze when done."
            ),
            'response = requests.get("http://127.0.0.1:5001/health", timeout=30)',
            [
                {"type": "contains", "value": "5001", "message": "Use monitoring port 5001"},
                {"type": "not_contains", "value": "5999", "message": "Remove the wrong port 5999"},
            ],
            why="Wrong host/port looks like 'API is down' — always verify URL first.",
            common_mistake="Rewriting the whole script instead of changing one digit.",
        ),
        _step(
            "df2",
            "Print status + JSON",
            _look(
                'response = requests.get("http://127.0.0.1:5001/health", timeout=30)\n'
                "print(response.status_code)\n"
                "print(response.json())"
            ),
            (
                'response = requests.get("http://127.0.0.1:5001/health", timeout=30)\n'
                "print(response.status_code)\n"
                "print(response.json())"
            ),
            [
                {"type": "contains", "value": "status_code", "message": "Print status_code"},
                {"type": "contains", "value": "json()", "message": "Print JSON body"},
                {"type": "output_contains", "value": "200", "message": "Health returns 200"},
            ],
            why="Confirming 200 proves the fix worked.",
            common_mistake="Leaving timeout off — hangs look like mystery failures.",
        ),
    ],

    # ── exam-open-incidents ──
    "exam-open-incidents:main": [
        _step(
            "eo1",
            "Exam: setup",
            _exam(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\nload_dotenv()"
            ),
            "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\nload_dotenv()",
            [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
            ],
            why="Exam checks that setup is automatic muscle memory.",
            common_mistake="Skipping dotenv and getting 401.",
        ),
        _step(
            "eo2",
            "Exam: GET open + print",
            _exam(
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("COUNT", len(response.json()["data"]))'
            ),
            (
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("COUNT", len(response.json()["data"]))'
            ),
            [
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
                {"type": "contains", "value": "status", "message": "status=open"},
                {"type": "contains", "value": "raise_for_status", "message": "raise_for_status"},
                {"type": "output_contains", "value": "COUNT", "message": "Print COUNT"},
            ],
            why="Blank-file GET is the first interview-ready skill.",
            common_mistake="Forgetting params status=open.",
        ),
    ],

    # ── explain-auth ──
    "explain-auth:main": [
        _step(
            "ea1",
            "Bearer one-liner",
            _look(
                'print("Bearer: the API key proves who you are in the Authorization header.")'
            ),
            'print("Bearer: the API key proves who you are in the Authorization header.")',
            [
                {"type": "contains", "value": "Bearer", "message": "Mention Bearer"},
                {"type": "contains", "value": "Authorization", "message": "Mention Authorization"},
            ],
            why="Customers need plain-language auth, not jargon.",
            common_mistake="Saying 'token' without saying where it goes.",
        ),
        _step(
            "ea2",
            "Env one-liner",
            _look(
                'print("Env: load keys with load_dotenv + os.getenv so secrets stay out of code.")'
            ),
            'print("Env: load keys with load_dotenv + os.getenv so secrets stay out of code.")',
            [
                {"type": "contains", "value": "getenv", "message": "Mention getenv"},
                {"type": "contains", "value": "load_dotenv", "message": "Mention load_dotenv"},
                {"type": "output_contains", "value": "Env", "message": "Print Env line"},
            ],
            why="SEs must explain why keys never ship in Git.",
            common_mistake="Hardcoding demo keys in shared scripts.",
        ),
    ],

    # ── docs-read-endpoints ──
    "docs-read-endpoints:main": [
        _step(
            "dr1",
            "Health from docs",
            (
                "Open mock-apis/README.md. Type what the docs say for health:\n\n"
                "EXAMPLE:\n"
                'print("METHOD GET")\n'
                'print("PATH /health")\n'
                'print("AUTH none")\n\n'
                "Click Analyze when done."
            ),
            'print("METHOD GET")\nprint("PATH /health")\nprint("AUTH none")',
            [
                {"type": "contains", "value": "GET", "message": "Print GET"},
                {"type": "contains", "value": "/health", "message": "Print /health"},
                {"type": "contains", "value": "none", "message": "Auth is none", "case_insensitive": True},
            ],
            why="Reading docs before coding prevents guessing URLs.",
            common_mistake="Assuming every endpoint needs a Bearer token.",
        ),
        _step(
            "dr2",
            "Incidents list from docs",
            _look(
                'print("METHOD GET")\n'
                'print("PATH /v1/incidents")\n'
                'print("AUTH Bearer SOURCE")'
            ),
            'print("METHOD GET")\nprint("PATH /v1/incidents")\nprint("AUTH Bearer SOURCE")',
            [
                {"type": "contains", "value": "/v1/incidents", "message": "Print incidents path"},
                {"type": "contains", "value": "Bearer", "message": "Mention Bearer"},
            ],
            why="Method + path + auth is the minimum docs extraction skill.",
            common_mistake="Mixing source and destination keys.",
        ),
        _step(
            "dr3",
            "Create ticket from docs",
            _look(
                'print("METHOD POST")\n'
                'print("PATH /v1/tickets")\n'
                'print("AUTH Bearer DEST")\n'
                'print("NOTE 409 on duplicate external_id")'
            ),
            (
                'print("METHOD POST")\n'
                'print("PATH /v1/tickets")\n'
                'print("AUTH Bearer DEST")\n'
                'print("NOTE 409 on duplicate external_id")'
            ),
            [
                {"type": "contains", "value": "POST", "message": "Print POST"},
                {"type": "contains", "value": "/v1/tickets", "message": "Print tickets path"},
                {"type": "contains", "value": "409", "message": "Mention 409"},
                {"type": "output_contains", "value": "409", "message": "Output mentions 409"},
            ],
            why="Docs also warn about conflict behavior — capture it.",
            common_mistake="Ignoring 409 until production duplicates blow up.",
        ),
    ],

    # ── py-from-postman-health ──
    "py-from-postman-health:main": [
        _step(
            "ph1",
            "Import + GET health",
            _look(
                "import requests\n\n"
                'response = requests.get("http://127.0.0.1:5001/health", timeout=30)\n'
                "print(response.status_code)"
            ),
            (
                "import requests\n\n"
                'response = requests.get("http://127.0.0.1:5001/health", timeout=30)\n'
                "print(response.status_code)"
            ),
            [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "/health", "message": "Hit /health"},
                {"type": "output_contains", "value": "200", "message": "Status prints 200"},
            ],
            why="Same click you made in Postman — now automated.",
            common_mistake="Using destination port 5002 for monitoring health.",
        ),
    ],

    # ── py-from-postman-get ──
    "py-from-postman-get:main": [
        _step(
            "pg1",
            "Env + Bearer GET",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("INCIDENTS", len(response.json()["data"]))'
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                'print("INCIDENTS", len(response.json()["data"]))'
            ),
            [
                {"type": "contains", "value": "Bearer", "message": "Bearer header"},
                {"type": "contains", "value": "status", "message": "status=open"},
                {"type": "output_contains", "value": "INCIDENTS", "message": "Print INCIDENTS count"},
            ],
            why="Postman proved the request; Python makes it repeatable.",
            common_mistake="Leaving the key hardcoded after the Postman lab.",
        ),
    ],

    # ── py-from-postman-post ──
    "py-from-postman-post:main": [
        _step(
            "pp1",
            "POST twice with 409 SKIP",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "payload = {\n"
                '    "external_id": "INC-POSTMAN-BRIDGE",\n'
                '    "site": "Postman Yard",\n'
                '    "description": "Bridge drill",\n'
                '    "priority": 1,\n'
                "}\n"
                "for _ in range(2):\n"
                "    try:\n"
                "        r = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=payload,\n"
                "            timeout=30,\n"
                "        )\n"
                "        r.raise_for_status()\n"
                '        print("CREATED", r.json()["id"])\n'
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                '            print("SKIP duplicate")\n'
                "        else:\n"
                "            raise"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "payload = {\n"
                '    "external_id": "INC-POSTMAN-BRIDGE",\n'
                '    "site": "Postman Yard",\n'
                '    "description": "Bridge drill",\n'
                '    "priority": 1,\n'
                "}\n"
                "for _ in range(2):\n"
                "    try:\n"
                "        r = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=payload,\n"
                "            timeout=30,\n"
                "        )\n"
                "        r.raise_for_status()\n"
                '        print("CREATED", r.json()["id"])\n'
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                '            print("SKIP duplicate")\n'
                "        else:\n"
                "            raise"
            ),
            [
                {"type": "contains", "value": "requests.post", "message": "Use requests.post"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP on duplicate"},
                {"type": "output_contains", "value": "SKIP", "message": "Output shows SKIP"},
            ],
            why="Duplicate create is expected in sync — treat 409 as success-skip.",
            common_mistake="Calling raise_for_status without catching 409.",
        ),
    ],

    # ── review-dicts-if-fn ──
    "review-dicts-if-fn:main": [
        _step(
            "rd1",
            "Sample incidents + filter",
            _look(
                "incidents = [\n"
                '    {"id": "INC-1", "severity": "critical", "facility": "Plant A", "message": "Pump"},\n'
                '    {"id": "INC-2", "severity": "low", "facility": "Plant B", "message": "Noise"},\n'
                '    {"id": "INC-3", "severity": "high", "facility": "Plant C", "message": "Voltage"},\n'
                "]\n"
                'SYNC = {"critical", "high"}\n'
                "urgent = [i for i in incidents if i['severity'] in SYNC]\n"
                'print("URGENT", len(urgent))'
            ),
            (
                "incidents = [\n"
                '    {"id": "INC-1", "severity": "critical", "facility": "Plant A", "message": "Pump"},\n'
                '    {"id": "INC-2", "severity": "low", "facility": "Plant B", "message": "Noise"},\n'
                '    {"id": "INC-3", "severity": "high", "facility": "Plant C", "message": "Voltage"},\n'
                "]\n"
                'SYNC = {"critical", "high"}\n'
                "urgent = [i for i in incidents if i['severity'] in SYNC]\n"
                'print("URGENT", len(urgent))'
            ),
            [
                {"type": "contains", "value": "critical", "message": "Keep critical"},
                {"type": "contains", "value": "high", "message": "Keep high"},
                {"type": "output_contains", "value": "URGENT", "message": "Print URGENT count"},
            ],
            why="Filter before transform — don't map noise.",
            common_mistake="Filtering medium instead of critical/high.",
        ),
        _step(
            "rd2",
            "Transform function",
            _look(
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n\n"
                "def transform_incident(incident):\n"
                "    return {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n\n"
                "for i in urgent:\n"
                "    ticket = transform_incident(i)\n"
                "    print(ticket['external_id'], ticket['priority'])"
            ),
            (
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n\n"
                "def transform_incident(incident):\n"
                "    return {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n\n"
                "for i in urgent:\n"
                "    ticket = transform_incident(i)\n"
                "    print(ticket['external_id'], ticket['priority'])"
            ),
            [
                {"type": "has_function", "name": "transform_incident", "message": "Define transform_incident"},
                {"type": "contains", "value": "facility", "message": "Map facility → site"},
                {"type": "contains", "value": "external_id", "message": "Set external_id"},
                {"type": "output_contains", "value": "INC-", "message": "Print transformed ids"},
            ],
            why="Field mapping is the heart of system A → B.",
            common_mistake="Using incident['site'] when source field is facility.",
        ),
    ],

    # ── debug-transform ──
    "debug-transform:main": [
        _step(
            "dt1",
            "Find KeyError site",
            (
                "Starter uses incident[\"site\"] but the dict has facility. Fix the key.\n\n"
                "EXAMPLE:\n"
                "\"site\": incident[\"facility\"],\n\n"
                "Click Analyze when done."
            ),
            '"site": incident["facility"],',
            [
                {"type": "contains", "value": 'incident["facility"]', "message": "Read facility key"},
                {"type": "not_contains", "value": 'incident["site"]', "message": "Don't read missing site key"},
            ],
            why="JSON key mismatches are the #1 transform bug.",
            common_mistake="Changing the print instead of the mapping.",
        ),
        _step(
            "dt2",
            "Verify output",
            (
                "Keep the fixed transform and prints. Analyze should run clean.\n\n"
                "EXAMPLE:\n"
                "ticket = transform_incident(incident)\n"
                "print(ticket['site'])\n"
                "print(ticket['priority'])"
            ),
            "ticket = transform_incident(incident)\nprint(ticket['site'])\nprint(ticket['priority'])",
            [
                {"type": "contains", "value": "facility", "message": "Keep facility mapping"},
                {"type": "output_contains", "value": "Water", "message": "Prints plant name"},
                {"type": "output_contains", "value": "1", "message": "Prints priority 1"},
            ],
            why="Run verify after every single fix.",
            common_mistake="Assuming KeyError gone without re-running.",
        ),
    ],

    # ── exam-transform-filter ──
    "exam-transform-filter:main": [
        _step(
            "et1",
            "Exam: filter + transform",
            _exam(
                "incidents = [\n"
                "    {'id': 'INC-A', 'severity': 'critical', 'facility': 'Yard', 'message': 'Alert'},\n"
                "    {'id': 'INC-B', 'severity': 'medium', 'facility': 'Dock', 'message': 'Warn'},\n"
                "]\n"
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "for incident in incidents:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    print('TICKET', ticket['external_id'], ticket['priority'])"
            ),
            (
                "incidents = [\n"
                "    {'id': 'INC-A', 'severity': 'critical', 'facility': 'Yard', 'message': 'Alert'},\n"
                "    {'id': 'INC-B', 'severity': 'medium', 'facility': 'Dock', 'message': 'Warn'},\n"
                "]\n"
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "for incident in incidents:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    print('TICKET', ticket['external_id'], ticket['priority'])"
            ),
            [
                {"type": "contains", "value": "critical", "message": "Filter critical"},
                {"type": "contains", "value": "external_id", "message": "Build external_id"},
                {"type": "contains", "value": "facility", "message": "Map facility"},
                {"type": "output_contains", "value": "TICKET", "message": "Print TICKET lines"},
            ],
            why="Combine filter + map without HTTP noise.",
            common_mistake="Transforming medium incidents too.",
        ),
    ],

    # ── explain-transform ──
    "explain-transform:main": [
        _step(
            "ex1",
            "Why transform",
            _look(
                'print("Transform: source facility becomes destination site so both systems agree.")'
            ),
            'print("Transform: source facility becomes destination site so both systems agree.")',
            [
                {"type": "contains", "value": "facility", "message": "Mention facility"},
                {"type": "contains", "value": "site", "message": "Mention site"},
                {"type": "output_contains", "value": "Transform", "message": "Print Transform line"},
            ],
            why="SEs must explain field mapping to non-engineers.",
            common_mistake="Saying 'we convert JSON' without naming fields.",
        ),
    ],

    # ── review-filter ──
    "review-filter:main": [
        _step(
            "rf1",
            "Fetch + filter critical/high",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "urgent = [i for i in response.json()['data'] if i['severity'] in {'critical', 'high'}]\n"
                "for i in urgent:\n"
                "    print(i['id'], i['severity'])\n"
                "print('FILTERED', len(urgent))"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "urgent = [i for i in response.json()['data'] if i['severity'] in {'critical', 'high'}]\n"
                "for i in urgent:\n"
                "    print(i['id'], i['severity'])\n"
                "print('FILTERED', len(urgent))"
            ),
            [
                {"type": "contains", "value": "Bearer", "message": "Bearer auth"},
                {"type": "contains", "value": "critical", "message": "Keep critical"},
                {"type": "contains", "value": "high", "message": "Keep high"},
                {"type": "output_contains", "value": "FILTERED", "message": "Print FILTERED count"},
            ],
            why="Review the live GET + severity filter together.",
            common_mistake="Filtering closed incidents or wrong severities.",
        ),
    ],

    # ── debug-filter ──
    "debug-filter:main": [
        _step(
            "dbf1",
            "Fix severity set",
            (
                "Starter keeps medium/low. Change the set to critical and high.\n\n"
                "EXAMPLE:\n"
                'filtered = [i for i in incidents if i["severity"] in {"critical", "high"}]\n\n'
                "Click Analyze when done."
            ),
            'filtered = [i for i in incidents if i["severity"] in {"critical", "high"}]',
            [
                {"type": "contains", "value": "critical", "message": "Include critical"},
                {"type": "contains", "value": "high", "message": "Include high"},
                {"type": "not_contains", "value": "medium", "message": "Remove medium from filter"},
            ],
            why="Wrong filter silently syncs the wrong work.",
            common_mistake="Changing print labels instead of the severity set.",
        ),
        _step(
            "dbf2",
            "Verify COUNT",
            (
                "Keep COUNT print. Run Analyze — filtered open critical/high should print.\n\n"
                "EXAMPLE:\n"
                'print("COUNT", len(filtered))'
            ),
            'print("COUNT", len(filtered))',
            [
                {"type": "contains", "value": "COUNT", "message": "Print COUNT"},
                {"type": "output_contains", "value": "COUNT", "message": "Output shows COUNT"},
            ],
            why="Always verify with a run after the fix.",
            common_mistake="Not re-running after the severity change.",
        ),
    ],

    # ── exam-get-filter ──
    "exam-get-filter:main": [
        _step(
            "eg1",
            "Exam: open critical/high",
            _exam(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "rows = [i for i in response.json()['data'] if i['severity'] in {'critical', 'high'}]\n"
                "print('EXAM', len(rows))"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "response = requests.get(\n"
                '    f"{BASE}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "response.raise_for_status()\n"
                "rows = [i for i in response.json()['data'] if i['severity'] in {'critical', 'high'}]\n"
                "print('EXAM', len(rows))"
            ),
            [
                {"type": "contains", "value": "status", "message": "status=open"},
                {"type": "contains", "value": "critical", "message": "Filter critical"},
                {"type": "contains", "value": "high", "message": "Filter high"},
                {"type": "output_contains", "value": "EXAM", "message": "Print EXAM count"},
            ],
            why="Prove filter skill without hand-holding.",
            common_mistake="Using API severity param when asked to filter in Python.",
        ),
    ],

    # ── explain-filter ──
    "explain-filter:main": [
        _step(
            "ef1",
            "API vs Python filter",
            _look(
                'print("API filter: query params shrink the payload at the source.")\n'
                'print("Python filter: keep only critical/high after you already fetched.")'
            ),
            (
                'print("API filter: query params shrink the payload at the source.")\n'
                'print("Python filter: keep only critical/high after you already fetched.")'
            ),
            [
                {"type": "contains", "value": "query", "message": "Mention query params"},
                {"type": "contains", "value": "Python", "message": "Mention Python filter"},
                {"type": "output_contains", "value": "API filter", "message": "Print API filter line"},
            ],
            why="Customers ask why you filter twice — have the answer.",
            common_mistake="Claiming only one approach is ever correct.",
        ),
    ],

    # ── review-sync ──
    "review-sync:main": [
        _step(
            "rs1",
            "Sync critical/high with SKIP",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'SRC_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SRC = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "resp = requests.get(\n"
                '    f"{SRC}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SRC_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "resp.raise_for_status()\n"
                "for incident in resp.json()['data']:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    try:\n"
                "        created = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=ticket,\n"
                "            timeout=30,\n"
                "        )\n"
                "        created.raise_for_status()\n"
                "        print('CREATED', created.json()['id'])\n"
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                "            print('SKIP', incident['id'])\n"
                "        else:\n"
                "            raise"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'SRC_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SRC = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "resp = requests.get(\n"
                '    f"{SRC}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SRC_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "resp.raise_for_status()\n"
                "for incident in resp.json()['data']:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    try:\n"
                "        created = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=ticket,\n"
                "            timeout=30,\n"
                "        )\n"
                "        created.raise_for_status()\n"
                "        print('CREATED', created.json()['id'])\n"
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                "            print('SKIP', incident['id'])\n"
                "        else:\n"
                "            raise"
            ),
            [
                {"type": "contains", "value": "requests.post", "message": "POST tickets"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP"},
                {"type": "runs", "message": "Script runs without crashing"},
            ],
            why="Full sync review stitches every prior skill.",
            common_mistake="Using SOURCE key against destination API.",
        ),
    ],

    # ── debug-409 ──
    "debug-409:main": [
        _step(
            "d409a",
            "Catch 409 instead of crashing",
            (
                "Starter calls raise_for_status on both POSTs and crashes on duplicate.\n"
                "Wrap in try/except HTTPError; on 409 print SKIP.\n\n"
                "EXAMPLE:\n"
                "from requests.exceptions import HTTPError\n"
                "...\n"
                "try:\n"
                "    response.raise_for_status()\n"
                "    print('CREATED', response.json()['id'])\n"
                "except HTTPError as exc:\n"
                "    if exc.response is not None and exc.response.status_code == 409:\n"
                "        print('SKIP duplicate')\n"
                "    else:\n"
                "        raise"
            ),
            (
                "from requests.exceptions import HTTPError\n"
                "try:\n"
                "    response.raise_for_status()\n"
                "    print('CREATED', response.json()['id'])\n"
                "except HTTPError as exc:\n"
                "    if exc.response is not None and exc.response.status_code == 409:\n"
                "        print('SKIP duplicate')\n"
                "    else:\n"
                "        raise"
            ),
            [
                {"type": "contains", "value": "HTTPError", "message": "Catch HTTPError"},
                {"type": "contains", "value": "409", "message": "Check status 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP"},
            ],
            why="409 means already synced — skip, don't abort the batch.",
            common_mistake="Swallowing all errors instead of only 409.",
        ),
        _step(
            "d409b",
            "Verify SKIP on second POST",
            (
                "Keep the two-attempt loop. Second create should print SKIP.\n\n"
                "Click Analyze — output must include SKIP."
            ),
            "print('SKIP duplicate')",
            [
                {"type": "output_contains", "value": "SKIP", "message": "Output shows SKIP"},
            ],
            why="Prove idempotent behavior with a real duplicate.",
            common_mistake="Changing external_id so the second POST never conflicts.",
        ),
    ],

    # ── exam-sync-two-systems ──
    "exam-sync-two-systems:main": [
        _step(
            "es1",
            "Exam: sync open critical/high",
            _exam(
                "# Same pattern as review-sync: GET open → filter → transform → POST → SKIP 409\n"
                "print('SYNC DONE')"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'SRC_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SRC = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "resp = requests.get(\n"
                '    f"{SRC}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SRC_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "resp.raise_for_status()\n"
                "for incident in resp.json()['data']:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    try:\n"
                "        created = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=ticket,\n"
                "            timeout=30,\n"
                "        )\n"
                "        created.raise_for_status()\n"
                "        print('CREATED', created.json()['id'])\n"
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                "            print('SKIP', incident['id'])\n"
                "        else:\n"
                "            raise\n"
                "print('SYNC DONE')"
            ),
            [
                {"type": "contains", "value": "requests.get", "message": "GET incidents"},
                {"type": "contains", "value": "requests.post", "message": "POST tickets"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "critical", "message": "Filter critical"},
                {"type": "runs", "message": "Script runs"},
                {"type": "output_contains", "value": "SYNC DONE", "message": "Print SYNC DONE"},
            ],
            why="Blank-file sync is the course's core deliverable.",
            common_mistake="Missing 409 handling so re-runs crash.",
        ),
    ],

    # ── explain-409 ──
    "explain-409:main": [
        _step(
            "e409",
            "409 customer language",
            _look(
                'print("409: ticket already exists for that external_id — we skip, not fail.")'
            ),
            'print("409: ticket already exists for that external_id — we skip, not fail.")',
            [
                {"type": "contains", "value": "409", "message": "Mention 409"},
                {"type": "contains", "value": "skip", "message": "Mention skip", "case_insensitive": True},
                {"type": "output_contains", "value": "409", "message": "Print 409 line"},
            ],
            why="Duplicate handling is a trust moment in demos.",
            common_mistake="Calling 409 an auth error.",
        ),
    ],

    # ── review-page-errors ──
    "review-page-errors:main": [
        _step(
            "rp1",
            "Paginate with has_more",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "all_rows = []\n"
                "page = 1\n"
                "while True:\n"
                "    response = requests.get(\n"
                '        f"{BASE}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {KEY}"},\n'
                '        params={"status": "open", "page": page, "limit": 2},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    body = response.json()\n"
                "    all_rows.extend(body['data'])\n"
                "    if not body['pagination']['has_more']:\n"
                "        break\n"
                "    page += 1\n"
                "print('TOTAL', len(all_rows))"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "all_rows = []\n"
                "page = 1\n"
                "while True:\n"
                "    response = requests.get(\n"
                '        f"{BASE}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {KEY}"},\n'
                '        params={"status": "open", "page": page, "limit": 2},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    body = response.json()\n"
                "    all_rows.extend(body['data'])\n"
                "    if not body['pagination']['has_more']:\n"
                "        break\n"
                "    page += 1\n"
                "print('TOTAL', len(all_rows))"
            ),
            [
                {"type": "contains", "value": "has_more", "message": "Check has_more"},
                {"type": "contains", "value": "limit", "message": "Pass limit"},
                {"type": "output_contains", "value": "TOTAL", "message": "Print TOTAL"},
            ],
            why="Without has_more you miss pages or loop forever.",
            common_mistake="Hard-coding page < N instead of reading pagination.",
        ),
        _step(
            "rp2",
            "Safe GET missing ID",
            _look(
                "from requests.exceptions import HTTPError\n\n"
                "try:\n"
                "    missing = requests.get(\n"
                '        f"{BASE}/v1/incidents/INC-99999",\n'
                '        headers={"Authorization": f"Bearer {KEY}"},\n'
                "        timeout=30,\n"
                "    )\n"
                "    missing.raise_for_status()\n"
                "except HTTPError:\n"
                "    print('MISSING ok')"
            ),
            (
                "from requests.exceptions import HTTPError\n\n"
                "try:\n"
                "    missing = requests.get(\n"
                '        f"{BASE}/v1/incidents/INC-99999",\n'
                '        headers={"Authorization": f"Bearer {KEY}"},\n'
                "        timeout=30,\n"
                "    )\n"
                "    missing.raise_for_status()\n"
                "except HTTPError:\n"
                "    print('MISSING ok')"
            ),
            [
                {"type": "contains", "value": "INC-99999", "message": "Look up missing id"},
                {"type": "contains", "value": "HTTPError", "message": "Catch HTTPError"},
                {"type": "output_contains", "value": "MISSING", "message": "Print MISSING ok"},
            ],
            why="404 on one id must not kill the whole job.",
            common_mistake="Bare except: that hides real outages.",
        ),
    ],

    # ── debug-pagination ──
    "debug-pagination:main": [
        _step(
            "dpg1",
            "Break when not has_more",
            (
                "Starter loops page < 100 forever-ish. Break when pagination says done.\n\n"
                "EXAMPLE:\n"
                "while True:\n"
                "    ...\n"
                "    if not body['pagination']['has_more']:\n"
                "        break\n"
                "    page += 1"
            ),
            (
                "while True:\n"
                "    ...\n"
                "    if not body['pagination']['has_more']:\n"
                "        break\n"
                "    page += 1"
            ),
            [
                {"type": "contains", "value": "has_more", "message": "Use has_more"},
                {"type": "contains", "value": "break", "message": "Break the loop"},
            ],
            why="has_more is the official stop signal from the API.",
            common_mistake="Leaving while page < 100 after adding has_more.",
        ),
        _step(
            "dpg2",
            "Verify TOTAL",
            (
                "Keep print TOTAL. Analyze should finish quickly with a real count.\n\n"
                "EXAMPLE:\n"
                "print('TOTAL', len(all_rows))"
            ),
            "print('TOTAL', len(all_rows))",
            [
                {"type": "output_contains", "value": "TOTAL", "message": "Output shows TOTAL"},
            ],
            why="A fast TOTAL proves you stopped correctly.",
            common_mistake="Still looping enough times to look hung.",
        ),
    ],

    # ── exam-paginate-safe-get ──
    "exam-paginate-safe-get:main": [
        _step(
            "ep1",
            "Exam: paginate open incidents",
            _exam(
                "# Paginate limit=2 with has_more; print TOTAL\n"
                "print('TOTAL', len(all_rows))"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n\n"
                "load_dotenv()\n"
                'KEY = os.getenv("SOURCE_API_KEY")\n'
                'BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                "all_rows = []\n"
                "page = 1\n"
                "while True:\n"
                "    response = requests.get(\n"
                '        f"{BASE}/v1/incidents",\n'
                '        headers={"Authorization": f"Bearer {KEY}"},\n'
                '        params={"status": "open", "page": page, "limit": 2},\n'
                "        timeout=30,\n"
                "    )\n"
                "    response.raise_for_status()\n"
                "    body = response.json()\n"
                "    all_rows.extend(body['data'])\n"
                "    if not body['pagination']['has_more']:\n"
                "        break\n"
                "    page += 1\n"
                "print('TOTAL', len(all_rows))"
            ),
            [
                {"type": "contains", "value": "has_more", "message": "Check has_more"},
                {"type": "contains", "value": "limit", "message": "Use limit"},
                {"type": "output_contains", "value": "TOTAL", "message": "Print TOTAL"},
            ],
            why="Pagination exam without training wheels.",
            common_mistake="Forgetting to increment page.",
        ),
    ],

    # ── explain-pagination ──
    "explain-pagination:main": [
        _step(
            "epx1",
            "Pagination one-liner",
            _look(
                'print("Pagination: fetch page by page with limit until has_more is false.")'
            ),
            'print("Pagination: fetch page by page with limit until has_more is false.")',
            [
                {"type": "contains", "value": "has_more", "message": "Mention has_more"},
                {"type": "contains", "value": "limit", "message": "Mention limit"},
                {"type": "output_contains", "value": "Pagination", "message": "Print Pagination line"},
            ],
            why="Ops teams ask why scripts 'miss' alerts — incomplete pages.",
            common_mistake="Saying 'we download everything once' for large APIs.",
        ),
    ],

    # ── review-full-pipeline ──
    "review-full-pipeline:main": [
        _step(
            "rfp1",
            "Full pipeline review",
            _look(
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'SRC_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SRC = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "resp = requests.get(\n"
                '    f"{SRC}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SRC_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "resp.raise_for_status()\n"
                "created = skipped = 0\n"
                "for incident in resp.json()['data']:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    try:\n"
                "        r = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=ticket,\n"
                "            timeout=30,\n"
                "        )\n"
                "        r.raise_for_status()\n"
                "        created += 1\n"
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                "            skipped += 1\n"
                "        else:\n"
                "            raise\n"
                "print('PIPELINE', created, skipped)"
            ),
            (
                "import os\n\nimport requests\nfrom dotenv import load_dotenv\n"
                "from requests.exceptions import HTTPError\n\n"
                "load_dotenv()\n"
                'SRC_KEY = os.getenv("SOURCE_API_KEY")\n'
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")\n'
                'SRC = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")\n'
                'DEST = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")\n'
                "PRIORITY = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}\n"
                "resp = requests.get(\n"
                '    f"{SRC}/v1/incidents",\n'
                '    headers={"Authorization": f"Bearer {SRC_KEY}"},\n'
                '    params={"status": "open"},\n'
                "    timeout=30,\n"
                ")\n"
                "resp.raise_for_status()\n"
                "created = skipped = 0\n"
                "for incident in resp.json()['data']:\n"
                "    if incident['severity'] not in {'critical', 'high'}:\n"
                "        continue\n"
                "    ticket = {\n"
                "        'external_id': incident['id'],\n"
                "        'site': incident['facility'],\n"
                "        'description': incident['message'],\n"
                "        'priority': PRIORITY[incident['severity']],\n"
                "    }\n"
                "    try:\n"
                "        r = requests.post(\n"
                '            f"{DEST}/v1/tickets",\n'
                '            headers={"Authorization": f"Bearer {DEST_KEY}"},\n'
                "            json=ticket,\n"
                "            timeout=30,\n"
                "        )\n"
                "        r.raise_for_status()\n"
                "        created += 1\n"
                "    except HTTPError as exc:\n"
                "        if exc.response is not None and exc.response.status_code == 409:\n"
                "            skipped += 1\n"
                "        else:\n"
                "            raise\n"
                "print('PIPELINE', created, skipped)"
            ),
            [
                {"type": "contains", "value": "load_dotenv", "message": "load_dotenv"},
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "facility", "message": "Map facility"},
                {"type": "output_contains", "value": "PIPELINE", "message": "Print PIPELINE stats"},
            ],
            why="One last guided end-to-end before the blank exam.",
            common_mistake="Forgetting DESTINATION_API_KEY name.",
        ),
    ],

    # ── debug-capstone ──
    "debug-capstone:main": [
        _step(
            "dc1",
            "Add load_dotenv + correct DEST key",
            (
                "Bugs: missing load_dotenv(); DEST_API_KEY should be DESTINATION_API_KEY.\n\n"
                "EXAMPLE:\n"
                "from dotenv import load_dotenv\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")'
            ),
            (
                "from dotenv import load_dotenv\n"
                "load_dotenv()\n"
                'DEST_KEY = os.getenv("DESTINATION_API_KEY")'
            ),
            [
                {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
                {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Use DESTINATION_API_KEY"},
                {"type": "not_contains", "value": "DEST_API_KEY", "message": "Remove wrong DEST_API_KEY"},
            ],
            why="Env name typos look like auth outages.",
            common_mistake="Hardcoding the dest key to 'make it work'.",
        ),
        _step(
            "dc2",
            "Handle 409 on POST",
            (
                "Wrap POST raise_for_status in try/except; SKIP on 409.\n\n"
                "EXAMPLE:\n"
                "from requests.exceptions import HTTPError\n"
                "try:\n"
                "    result.raise_for_status()\n"
                "    print('OK', result.json()['id'])\n"
                "except HTTPError as exc:\n"
                "    if exc.response is not None and exc.response.status_code == 409:\n"
                "        print('SKIP', incident['id'])\n"
                "    else:\n"
                "        raise"
            ),
            (
                "from requests.exceptions import HTTPError\n"
                "try:\n"
                "    result.raise_for_status()\n"
                "    print('OK', result.json()['id'])\n"
                "except HTTPError as exc:\n"
                "    if exc.response is not None and exc.response.status_code == 409:\n"
                "        print('SKIP', incident['id'])\n"
                "    else:\n"
                "        raise"
            ),
            [
                {"type": "contains", "value": "409", "message": "Handle 409"},
                {"type": "contains", "value": "SKIP", "message": "Print SKIP"},
                {"type": "runs", "message": "Script runs"},
            ],
            why="Capstone re-runs must be safe.",
            common_mistake="Fixing env but still crashing on duplicates.",
        ),
    ],

    # ── explain-poc-value ──
    "explain-poc-value:main": [
        _step(
            "epv1",
            "Success criteria",
            _look(
                'print("SUCCESS: critical/high open incidents become tickets automatically within the POC window.")'
            ),
            'print("SUCCESS: critical/high open incidents become tickets automatically within the POC window.")',
            [
                {"type": "contains", "value": "SUCCESS", "message": "Print SUCCESS"},
                {"type": "contains", "value": "critical", "message": "Mention critical"},
            ],
            why="POCs need measurable outcomes, not vibes.",
            common_mistake="Saying 'it works' without a metric.",
        ),
        _step(
            "epv2",
            "Next step",
            _look(
                'print("NEXT: 2-week pilot on one site with shared owners and monitoring.")'
            ),
            'print("NEXT: 2-week pilot on one site with shared owners and monitoring.")',
            [
                {"type": "contains", "value": "NEXT", "message": "Print NEXT"},
                {"type": "contains", "value": "pilot", "message": "Mention pilot", "case_insensitive": True},
                {"type": "output_contains", "value": "NEXT", "message": "Output shows NEXT"},
            ],
            why="Always close with a concrete ask.",
            common_mistake="Ending the demo without a next step.",
        ),
    ],

    # ── explain-401-vs-409 ──
    "explain-401-vs-409:main": [
        _step(
            "e401",
            "401 vs 409",
            _look(
                'print("401: wrong or missing credentials — fix the key.")\n'
                'print("409: duplicate create — ticket already exists; skip safely.")'
            ),
            (
                'print("401: wrong or missing credentials — fix the key.")\n'
                'print("409: duplicate create — ticket already exists; skip safely.")'
            ),
            [
                {"type": "contains", "value": "401", "message": "Explain 401"},
                {"type": "contains", "value": "409", "message": "Explain 409"},
                {"type": "output_contains", "value": "401", "message": "Print 401 line"},
            ],
            why="These two codes get mixed up in every customer call.",
            common_mistake="Treating both as 'the API is broken'.",
        ),
    ],

    # ── explain-poll-vs-webhook ──
    "explain-poll-vs-webhook:main": [
        _step(
            "epw1",
            "Poll vs webhook",
            _look(
                'print("Poll: scheduled GET when the vendor has no push events.")\n'
                'print("Webhook: vendor POSTs to you for near-real-time updates.")'
            ),
            (
                'print("Poll: scheduled GET when the vendor has no push events.")\n'
                'print("Webhook: vendor POSTs to you for near-real-time updates.")'
            ),
            [
                {"type": "contains", "value": "Poll", "message": "Explain poll"},
                {"type": "contains", "value": "Webhook", "message": "Explain webhook"},
                {"type": "output_contains", "value": "Webhook", "message": "Print Webhook line"},
            ],
            why="Architecture choice is an SE discovery skill.",
            common_mistake="Promising webhooks when the API only supports polling.",
        ),
    ],
}
