"""Step checks keyed by lesson:exercise — used by Analyze."""

# Shared check snippets
_SETUP_IMPORTS = [
    {"type": "has_import", "module": "requests", "message": "Import requests"},
    {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
    {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
    {"type": "no_hardcoded_secrets", "message": "No hardcoded API keys"},
]

LESSON_STEPS = {
    # ── HTTP: A — open incidents ──
    "http-type-along:open-incidents": [
        {
            "id": "h1",
            "title": "Imports",
            "instruction": "Import os, requests, dotenv. Call load_dotenv().",
            "checks": [
                {"type": "has_import", "module": "os", "message": "Import os"},
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "load_dotenv", "message": "Call load_dotenv()"},
            ],
        },
        {
            "id": "h2",
            "title": "Environment",
            "instruction": "Load SOURCE_API_KEY and SOURCE_API_URL with os.getenv().",
            "checks": [
                {"type": "contains", "value": "os.getenv", "message": "Use os.getenv()"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load SOURCE_API_KEY"},
                {"type": "no_hardcoded_secrets", "message": "Don't hardcode secrets"},
            ],
        },
        {
            "id": "h3",
            "title": "GET open incidents",
            "instruction": "GET /v1/incidents?status=open with Bearer auth and timeout=30.",
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "regex", "pattern": r"Bearer", "message": "Bearer authentication"},
                {"type": "contains", "value": "status", "message": "Filter status=open"},
            ],
        },
        {
            "id": "h4",
            "title": "Parse & print count",
            "instruction": "raise_for_status(), parse data list, print how many incidents.",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "Check HTTP status"},
                {"type": "contains", "value": "json()", "message": "Parse JSON"},
                {"type": "contains", "value": "print", "message": "Print incident count"},
            ],
        },
    ],
    # ── HTTP: B — health check ──
    "http-type-along:health-check": [
        {
            "id": "hb1",
            "title": "Import requests",
            "instruction": "Import requests. Set BASE_URL to http://127.0.0.1:5001 (or from env).",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "5001", "message": "Point at monitoring API port 5001"},
            ],
        },
        {
            "id": "hb2",
            "title": "GET /health",
            "instruction": "GET /health — no auth header needed for this endpoint.",
            "checks": [
                {"type": "contains", "value": "requests.get", "message": "Use requests.get()"},
                {"type": "contains", "value": "/health", "message": "Hit /health endpoint"},
                {"type": "not_contains", "value": "Authorization", "message": "Health check needs no auth"},
            ],
        },
        {
            "id": "hb3",
            "title": "Verify service",
            "instruction": "Parse JSON and print the service name from the response.",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "Check response status"},
                {"type": "contains", "value": "json()", "message": "Parse JSON body"},
                {"type": "contains", "value": "service", "message": "Read the service field"},
                {"type": "contains", "value": "print", "message": "Print the result"},
            ],
        },
    ],
    # ── HTTP: C — single incident ──
    "http-type-along:single-incident": [
        {
            "id": "hs1",
            "title": "Setup",
            "instruction": "Import os, requests, dotenv. Load SOURCE_API_KEY from environment.",
            "checks": [
                {"type": "has_import", "module": "requests", "message": "Import requests"},
                {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load API key from env"},
                {"type": "no_hardcoded_secrets", "message": "No hardcoded keys"},
            ],
        },
        {
            "id": "hs2",
            "title": "GET by ID",
            "instruction": "GET /v1/incidents/INC-38201 with Bearer auth.",
            "checks": [
                {"type": "contains", "value": "INC-38201", "message": "Request incident INC-38201"},
                {"type": "regex", "pattern": r"Bearer", "message": "Use Bearer token"},
                {"type": "contains", "value": "requests.get", "message": "Use GET request"},
            ],
        },
        {
            "id": "hs3",
            "title": "Print details",
            "instruction": "Print facility and message from the JSON response.",
            "checks": [
                {"type": "contains", "value": "raise_for_status", "message": "Handle HTTP errors"},
                {"type": "contains", "value": "facility", "message": "Access facility field"},
                {"type": "contains", "value": "message", "message": "Access message field"},
                {"type": "contains", "value": "print", "message": "Print the details"},
            ],
        },
    ],
    # ── Python: A — water plant ──
    "python-type-along:water-plant": [
        {
            "id": "p1",
            "title": "Incident dict",
            "instruction": "Create incident dict: id INC-38192, facility Water Treatment Plant 4, severity critical.",
            "checks": [
                {"type": "regex", "pattern": r"incident\s*=\s*\{", "message": "Create incident dictionary"},
                {"type": "contains", "value": "facility", "message": "Include facility"},
                {"type": "contains", "value": "severity", "message": "Include severity"},
            ],
        },
        {
            "id": "p2",
            "title": "Filter list",
            "instruction": "List of 3 incidents, SYNC_SEVERITIES, loop with if to skip low.",
            "checks": [
                {"type": "contains", "value": "incidents", "message": "Create incidents list"},
                {"type": "contains", "value": "SYNC_SEVERITIES", "message": "Define SYNC_SEVERITIES"},
                {"type": "contains", "value": "for ", "message": "Loop with for"},
            ],
        },
        {
            "id": "p3",
            "title": "Transform",
            "instruction": "severity_to_priority() and transform_incident() → external_id, site, priority.",
            "checks": [
                {"type": "has_function", "name": "severity_to_priority", "message": "Define severity_to_priority()"},
                {"type": "has_function", "name": "transform_incident", "message": "Define transform_incident()"},
                {"type": "contains", "value": "external_id", "message": "Map external_id"},
            ],
        },
    ],
    # ── Python: B — gas pipeline (different field names) ──
    "python-type-along:gas-pipeline": [
        {
            "id": "gp1",
            "title": "Source event",
            "instruction": "Create event dict with eventId, locationName, severity, message (gas pipeline alert).",
            "checks": [
                {"type": "regex", "pattern": r"event\s*=\s*\{", "message": "Create event dictionary"},
                {"type": "contains", "value": "eventId", "message": "Use eventId key (source schema)"},
                {"type": "contains", "value": "locationName", "message": "Use locationName key"},
            ],
        },
        {
            "id": "gp2",
            "title": "Transform event",
            "instruction": "Write transform_event(event) mapping eventId→external_id, locationName→site.",
            "checks": [
                {"type": "has_function", "name": "transform_event", "message": "Define transform_event()"},
                {"type": "contains", "value": "external_id", "message": "Map to external_id"},
                {"type": "contains", "value": "locationName", "message": "Read locationName from source"},
            ],
        },
        {
            "id": "gp3",
            "title": "Priority map",
            "instruction": "Map CRITICAL/HIGH/MEDIUM strings to priority numbers 1/2/3.",
            "checks": [
                {"type": "contains", "value": "priority", "message": "Include priority in output"},
                {"type": "contains", "value": "CRITICAL", "message": "Handle CRITICAL severity"},
                {"type": "contains", "value": "return", "message": "Return transformed dict"},
            ],
        },
    ],
    # ── Python: C — hospital feed ──
    "python-type-along:hospital-feed": [
        {
            "id": "hf1",
            "title": "Event feed",
            "instruction": "List `feed` with 3+ dicts including id, severity, facility, message.",
            "checks": [
                {"type": "contains", "value": "feed", "message": "Create feed list"},
                {"type": "regex", "pattern": r"for\s+\w+\s+in\s+feed", "message": "Loop over feed"},
            ],
        },
        {
            "id": "hf2",
            "title": "Critical only",
            "instruction": "Only process events where severity == 'critical'.",
            "checks": [
                {"type": "contains", "value": "critical", "message": "Filter critical severity"},
                {"type": "contains", "value": "if ", "message": "Use if condition"},
            ],
        },
        {
            "id": "hf3",
            "title": "Build ticket",
            "instruction": "build_ticket(event) returns external_id, site, description, priority=1.",
            "checks": [
                {"type": "has_function", "name": "build_ticket", "message": "Define build_ticket()"},
                {"type": "contains", "value": "description", "message": "Include description"},
                {"type": "contains", "value": "priority", "message": "Set priority"},
            ],
        },
    ],
    # ── GET filter: A — critical + high ──
    "get-filter:critical-high": [
        {"id": "g1", "title": "Setup", "instruction": "Import requests, load_dotenv, SOURCE_API_KEY from env.", "checks": _SETUP_IMPORTS},
        {"id": "g2", "title": "GET + auth", "instruction": "GET /v1/incidents?status=open with Bearer header.", "checks": [
            {"type": "contains", "value": "requests.get", "message": "GET request"},
            {"type": "regex", "pattern": r"Bearer", "message": "Bearer auth"},
            {"type": "contains", "value": "raise_for_status", "message": "Check status"},
        ]},
        {"id": "g3", "title": "Filter in Python", "instruction": "Parse data, filter to critical and high into `filtered`.", "checks": [
            {"type": "contains", "value": "filtered", "message": "Create filtered list"},
            {"type": "contains", "value": "critical", "message": "Include critical"},
            {"type": "contains", "value": "high", "message": "Include high"},
        ]},
        {"id": "g4", "title": "Report", "instruction": "Print each filtered incident id and facility.", "checks": [
            {"type": "regex", "pattern": r"for\s+\w+\s+in\s+filtered", "message": "Loop filtered"},
            {"type": "contains", "value": "print", "message": "Print results"},
        ]},
    ],
    # ── GET filter: B — API-side filter ──
    "get-filter:api-filter": [
        {"id": "gf1", "title": "Setup", "instruction": "Standard imports and SOURCE_API_KEY from env.", "checks": _SETUP_IMPORTS},
        {"id": "gf2", "title": "Query param filter", "instruction": "Pass status=open AND severity=critical in params (let API filter).", "checks": [
            {"type": "contains", "value": "params", "message": "Use params dict"},
            {"type": "contains", "value": "severity", "message": "Pass severity param"},
            {"type": "contains", "value": "critical", "message": "Filter critical at API"},
        ]},
        {"id": "gf3", "title": "Print results", "instruction": "Parse data and print count + each incident id.", "checks": [
            {"type": "contains", "value": "json()", "message": "Parse JSON"},
            {"type": "contains", "value": "print", "message": "Print incidents"},
            {"type": "contains", "value": "len(", "message": "Print count with len()"},
        ]},
    ],
    # ── GET filter: C — facility keyword ──
    "get-filter:facility-search": [
        {"id": "gs1", "title": "Setup + GET", "instruction": "GET all open incidents with auth.", "checks": _SETUP_IMPORTS + [
            {"type": "contains", "value": "requests.get", "message": "GET incidents"},
        ]},
        {"id": "gs2", "title": "Keyword filter", "instruction": "Filter where facility contains 'Water Treatment' (case-sensitive or in check).", "checks": [
            {"type": "contains", "value": "facility", "message": "Check facility field"},
            {"type": "contains", "value": "Water", "message": "Filter for Water Treatment facilities"},
            {"type": "contains", "value": "if ", "message": "Use if to filter"},
        ]},
        {"id": "gs3", "title": "Output", "instruction": "Print matching facilities and count.", "checks": [
            {"type": "contains", "value": "print", "message": "Print matches"},
        ]},
    ],
    # ── Sync: A — critical + high ──
    "sync-systems:sync-all-urgent": [
        {"id": "s1", "title": "Config", "instruction": "Load SOURCE + DESTINATION keys from env.", "checks": [
            {"type": "contains", "value": "SOURCE_API_KEY", "message": "Source key"},
            {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Dest key"},
            {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
        ]},
        {"id": "s2", "title": "Transform", "instruction": "transform_incident() with external_id, site, description, priority.", "checks": [
            {"type": "has_function", "name": "transform_incident", "message": "Define transform_incident()"},
            {"type": "contains", "value": "external_id", "message": "Map external_id"},
        ]},
        {"id": "s3", "title": "Fetch + POST", "instruction": "fetch_open_incidents() and create_ticket() with requests.post json=.", "checks": [
            {"type": "has_function", "name": "fetch_open_incidents", "message": "Define fetch function"},
            {"type": "has_function", "name": "create_ticket", "message": "Define create_ticket()"},
            {"type": "contains", "value": "requests.post", "message": "POST tickets"},
        ]},
        {"id": "s4", "title": "Main loop", "instruction": "main() filters critical/high, handles 409 duplicates.", "checks": [
            {"type": "has_function", "name": "main", "message": "Define main()"},
            {"type": "contains", "value": "409", "message": "Handle 409 conflict"},
        ]},
    ],
    # ── Sync: B — critical only ──
    "sync-systems:sync-critical-only": [
        {"id": "sc1", "title": "Config", "instruction": "Load both API keys from environment.", "checks": [
            {"type": "contains", "value": "DESTINATION_API_KEY", "message": "Destination key"},
            {"type": "no_hardcoded_secrets", "message": "No hardcoded secrets"},
        ]},
        {"id": "sc2", "title": "Critical filter", "instruction": "SYNC only severity == 'critical' (not high).", "checks": [
            {"type": "contains", "value": "critical", "message": "Filter critical only"},
            {"type": "not_contains", "value": '"high"', "message": "Do not sync high — critical only"},
        ]},
        {"id": "sc3", "title": "Sync loop", "instruction": "fetch, transform, POST. Skip on 409.", "checks": [
            {"type": "contains", "value": "requests.post", "message": "POST to destination"},
            {"type": "contains", "value": "409", "message": "Handle duplicates"},
            {"type": "contains", "value": "transform", "message": "Transform before POST"},
        ]},
    ],
    # ── Sync: C — with stats ──
    "sync-systems:sync-with-stats": [
        {"id": "ss1", "title": "Stats dict", "instruction": "Track stats = {created: 0, skipped: 0, failed: 0}.", "checks": [
            {"type": "contains", "value": "created", "message": "Track created count"},
            {"type": "contains", "value": "skipped", "message": "Track skipped count"},
            {"type": "contains", "value": "failed", "message": "Track failed count"},
        ]},
        {"id": "ss2", "title": "Sync functions", "instruction": "fetch_open_incidents(), create_ticket(), transform_incident().", "checks": [
            {"type": "has_function", "name": "fetch_open_incidents", "message": "Fetch function"},
            {"type": "has_function", "name": "create_ticket", "message": "Create ticket function"},
        ]},
        {"id": "ss3", "title": "Print summary", "instruction": "After loop, print final created/skipped/failed totals.", "checks": [
            {"type": "contains", "value": "print", "message": "Print summary"},
            {"type": "contains", "value": "409", "message": "Increment skipped on 409"},
        ]},
    ],
    # ── Reliability: A — full ──
    "reliability:full-reliability": [
        {"id": "r1", "title": "Setup", "instruction": "Import requests, load SOURCE_API_KEY.", "checks": [
            {"type": "has_import", "module": "requests", "message": "Import requests"},
            {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load API key"},
        ]},
        {"id": "r2", "title": "Pagination", "instruction": "fetch_all_incidents(limit=3) with while + has_more.", "checks": [
            {"type": "has_function", "name": "fetch_all_incidents", "message": "Define fetch_all_incidents()"},
            {"type": "contains", "value": "has_more", "message": "Check has_more"},
            {"type": "contains", "value": "while", "message": "Use while loop"},
        ]},
        {"id": "r3", "title": "Safe GET", "instruction": "safe_get_incident(id) with Timeout + HTTPError handling.", "checks": [
            {"type": "has_function", "name": "safe_get_incident", "message": "Define safe_get_incident()"},
            {"type": "contains", "value": "HTTPError", "message": "Catch HTTPError"},
            {"type": "contains", "value": "Timeout", "message": "Catch Timeout"},
        ]},
    ],
    # ── Reliability: B — paginate only ──
    "reliability:paginate-only": [
        {"id": "rp1", "title": "Setup", "instruction": "requests + SOURCE_API_KEY + BASE URL.", "checks": [
            {"type": "has_import", "module": "requests", "message": "Import requests"},
            {"type": "contains", "value": "SOURCE_API_KEY", "message": "Load key"},
        ]},
        {"id": "rp2", "title": "Paginate limit=2", "instruction": "while loop, page increment, limit=2, extend all_records list.", "checks": [
            {"type": "contains", "value": "while", "message": "While loop"},
            {"type": "contains", "value": "limit", "message": "Pass limit param"},
            {"type": "contains", "value": "page", "message": "Increment page"},
            {"type": "contains", "value": "extend", "message": "Accumulate with extend()"},
        ]},
        {"id": "rp3", "title": "Print total", "instruction": "Print total number of incidents fetched.", "checks": [
            {"type": "contains", "value": "print", "message": "Print total"},
            {"type": "contains", "value": "len(", "message": "Use len() for count"},
        ]},
    ],
    # ── Reliability: C — errors only ──
    "reliability:errors-only": [
        {"id": "re1", "title": "safe_get_incident", "instruction": "try/except for Timeout, HTTPError (404 vs others), return None on fail.", "checks": [
            {"type": "has_function", "name": "safe_get_incident", "message": "Define safe_get_incident()"},
            {"type": "contains", "value": "try:", "message": "Use try/except"},
            {"type": "contains", "value": "404", "message": "Handle 404 not found"},
        ]},
        {"id": "re2", "title": "Test cases",
            "instruction": "Test INC-38192 (exists), INC-99999 (missing), print results.",
            "checks": [
            {"type": "contains", "value": "INC-38192", "message": "Test existing ID"},
            {"type": "contains", "value": "INC-99999", "message": "Test missing ID"},
            {"type": "contains", "value": "__main__", "message": "Main test block"},
        ]},
    ],
    # ── Capstone: A — full ──
    "capstone-build:full-capstone": [
        {"id": "c1", "title": "load_config", "instruction": "Validate SOURCE + DESTINATION keys, raise ValueError if missing.", "checks": [
            {"type": "has_function", "name": "load_config", "message": "Define load_config()"},
            {"type": "contains", "value": "ValueError", "message": "Raise on missing keys"},
        ]},
        {"id": "c2", "title": "Fetch paginated", "instruction": "fetch_all_open_incidents(config) with pagination.", "checks": [
            {"type": "has_function", "name": "fetch_all_open_incidents", "message": "Paginated fetch"},
            {"type": "contains", "value": "while", "message": "Pagination loop"},
        ]},
        {"id": "c3", "title": "sync()", "instruction": "Filter critical/high, transform, POST, handle 409.", "checks": [
            {"type": "has_function", "name": "sync", "message": "Define sync()"},
            {"type": "contains", "value": "409", "message": "Handle duplicates"},
        ]},
        {"id": "c4", "title": "Entry point", "instruction": "if __name__ == '__main__': sync()", "checks": [
            {"type": "contains", "value": "__main__", "message": "Main guard"},
            {"type": "contains", "value": "sync()", "message": "Call sync()"},
        ]},
    ],
    # ── Capstone: B — critical only + stats ──
    "capstone-build:critical-capstone": [
        {"id": "cb1", "title": "Config + transform", "instruction": "load_config() and transform_incident().", "checks": [
            {"type": "has_function", "name": "load_config", "message": "load_config()"},
            {"type": "has_function", "name": "transform_incident", "message": "transform_incident()"},
        ]},
        {"id": "cb2", "title": "Critical only", "instruction": "Sync only severity == critical (hospital SLA scenario).", "checks": [
            {"type": "contains", "value": "critical", "message": "Filter critical"},
            {"type": "not_contains", "value": '"high"', "message": "Exclude high severity"},
        ]},
        {"id": "cb3", "title": "Stats + sync", "instruction": "sync() tracks created/skipped, prints summary.", "checks": [
            {"type": "has_function", "name": "sync", "message": "Define sync()"},
            {"type": "contains", "value": "created", "message": "Track created"},
            {"type": "contains", "value": "print", "message": "Print summary"},
        ]},
    ],
}
