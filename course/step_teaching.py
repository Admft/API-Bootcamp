"""Enrich type-along steps with beginner-friendly 'What's going on' context.

Steps may already define `context`. If not, we build it from the step's
title / checks / example / why so first-time learners understand the idea,
not only what to type.
"""

from __future__ import annotations


def enrich_steps(steps, lesson_key: str = ""):
    """Return a shallow-copied list of steps with `context` filled in."""
    out = []
    for step in steps or []:
        enriched = dict(step)
        if not (enriched.get("context") or "").strip():
            enriched["context"] = build_context(enriched, lesson_key)
        if not (enriched.get("why") or "").strip():
            enriched["why"] = _short_why(enriched, enriched["context"])
        if not (enriched.get("common_mistake") or "").strip():
            enriched["common_mistake"] = _guess_mistake(enriched)
        out.append(enriched)
    return out


def build_context(step: dict, lesson_key: str = "") -> str:
    sid = f"{lesson_key}:{step.get('id', '')}"
    if sid in STEP_OVERRIDES:
        return STEP_OVERRIDES[sid]

    title = (step.get("title") or "").strip()
    title_key = title.lower()
    if title_key in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[title_key]

    for needles, text in CONCEPT_RULES:
        blob = " ".join(
            [
                title_key,
                (step.get("example") or "").lower(),
                " ".join(str(c.get("value", "")) for c in step.get("checks") or []).lower(),
                " ".join(str(c.get("module", "")) for c in step.get("checks") or []).lower(),
                (step.get("why") or "").lower(),
            ]
        )
        if all(n in blob for n in needles):
            return text

    why = (step.get("why") or "").strip()
    if why:
        return (
            f"{why}\n\n"
            "What is actually happening: you are adding one building block of a real "
            "integration. In production SE work this same idea shows up when you wire "
            "auth, call an endpoint, reshape fields, or prove a filter before a customer demo.\n\n"
            "Read the example slowly. Name each piece out loud (library, variable, request, "
            "field). Then type it yourself — muscle memory plus understanding sticks."
        )

    return (
        f"This step asks you to add: {title or 'the next piece of the script'}.\n\n"
        "Do not just copy characters. Pause and ask: what does this line make the "
        "computer do? How would I explain it to a teammate in one sentence? That "
        "habit is what turns type-along drills into real SE skill."
    )


def _short_why(step: dict, context: str) -> str:
    first = context.split("\n\n")[0].strip()
    if len(first) <= 160:
        return first
    return first[:157].rstrip() + "…"


def _guess_mistake(step: dict) -> str:
    title = (step.get("title") or "").lower()
    example = (step.get("example") or "").lower()
    if "import request" in example or "import requests" in example:
        return "Package name is requests (plural), not request."
    if "bearer" in example or "authorization" in example:
        return 'Header value must look like "Bearer <token>" with a capital B and a space.'
    if "getenv" in example:
        return "Use os.getenv(\"NAME\") — do not paste the secret as a quoted string."
    if "load_dotenv" in example:
        return "Call load_dotenv() with parentheses or the .env file never loads."
    if "raise_for_status" in example:
        return "Call raise_for_status() before .json() so failures are obvious."
    if "params" in example:
        return "Filter with params={...} on the request — do not invent a fake path like /open."
    if "timeout" in example:
        return "timeout is seconds (e.g. 30), not milliseconds."
    if title.startswith("200") or "status" in title:
        return "Status codes are numbers (200, 401). Memorize what they mean, not just the digits."
    return "Type carefully — a missing quote, colon, or parenthesis is the usual trip-up."


# Exact overrides: "lesson_key:step_id"
STEP_OVERRIDES = {
    "baby-print:main:bp1": (
        "A Python file is just text the computer will run line by line.\n\n"
        "Lines that start with # are comments. Python ignores them. We use them as notes "
        "for humans (and to prove the editor is working before we write real code)."
    ),
    "baby-print:main:bp2": (
        "print(...) is how a program shows you something on screen.\n\n"
        "The text inside quotes is a string — a piece of text data. Later you will print "
        "API responses the same way: call a function, pass it something, see the result."
    ),
    "baby-print:main:bp3": (
        "Exact text matters in APIs and in tests.\n\n"
        "Here we are training precision: the string must include API Bootcamp. In real "
        "integrations, wrong field names or wrong spelling break the whole flow."
    ),
    "baby-print:main:bp4": (
        "Running code is how you prove it works.\n\n"
        "Analyze (and later Run) checks that Python can execute what you typed. In SE "
        "work, 'it looks right' is not enough — you always verify with an actual run."
    ),
    "baby-import:main:bi1": (
        "import brings in a library someone else already wrote.\n\n"
        "requests is the popular Python library for HTTP (GET/POST to APIs). Without "
        "importing it, Python does not know what requests.get means."
    ),
    "baby-import:main:bi2": (
        "After an import, you can use that library's functions.\n\n"
        "Printing a confirmation is a tiny sanity check: if this line runs, the import "
        "succeeded and your environment can load the package."
    ),
    "baby-health:main:bh1": (
        "Before you call APIs with secrets, practice the simplest GET possible.\n\n"
        "Health endpoints answer: 'is this service up?' They are often public and tiny "
        "— perfect for learning the HTTP round-trip without auth complexity."
    ),
    "baby-health:main:bh2": (
        "A base URL is the host + port of the API (here, the local mock on 5001).\n\n"
        "Storing it in a variable means you change one place later instead of hunting "
        "through every request. SEs do this in every POC."
    ),
    "baby-health:main:bh3": (
        "requests.get(url) sends an HTTP GET to that address and waits for a response.\n\n"
        "Under the hood: your laptop opens a network connection, asks for a resource, "
        "and gets back status + body. That is the same idea Postman uses — just from code."
    ),
    "baby-health:main:bh4": (
        "response.status_code is the HTTP status number (200 means OK).\n\n"
        "Always look at status before trusting the body. A pretty JSON blob with a 401 "
        "still means 'you are not allowed.'"
    ),
    "baby-auth:main:ba2": (
        "An API key proves who you are.\n\n"
        "In this baby lesson we hardcode a practice key so you can see the shape. In real "
        "work you NEVER commit keys — you load them from environment variables (.env)."
    ),
    "baby-auth:main:ba3": (
        "Bearer auth puts the key in an Authorization header.\n\n"
        "Format is always: Bearer <space><token>. The server reads that header and decides "
        "if the request is allowed. Missing or wrong Bearer → 401 Unauthorized."
    ),
    "baby-getenv:main:bg2": (
        "os.getenv('NAME') reads a secret from the environment — not from your source file.\n\n"
        "That way demos, CI, and laptops can each have different keys without changing code. "
        "This is table stakes for SE POCs and customer deployments."
    ),
    "baby-dotenv:main:bd2": (
        "load_dotenv() reads a local .env file into the process environment.\n\n"
        "Importing dotenv alone does nothing. You must call the function. After that, "
        "os.getenv can see SOURCE_API_KEY and the other training secrets."
    ),
    "baby-json:main:bj3": (
        "response.json() parses the response body from JSON text into Python dicts/lists.\n\n"
        "APIs speak JSON. Python prefers native structures. .json() is the bridge. After "
        "this call you can do body['service'] instead of parsing text by hand."
    ),
    "baby-raise:main:br4": (
        "raise_for_status() turns bad HTTP statuses into Python exceptions.\n\n"
        "Without it, a 404 or 500 still looks like a 'successful' requests call — you only "
        "notice when .json() looks weird. Fail loudly; debug faster."
    ),
    "baby-params:main:bpm2": (
        "Query params are filters the API applies on the server.\n\n"
        "params={'status': 'open'} becomes ?status=open on the URL. That is cleaner than "
        "downloading everything and filtering only in Python (though you will do both)."
    ),
    "baby-loop:main:bl3": (
        "A for loop walks each item in a list one at a time.\n\n"
        "API list endpoints return many records. You almost always loop: print fields, "
        "filter severities, or POST each one to another system."
    ),
    "py-vars:main:pv1": (
        "A variable is a named box that holds a value.\n\n"
        "name = \"Acme Fleet\" stores text under the label name so you can reuse it. "
        "Integrations are full of variables: URLs, keys, ids, counters."
    ),
    "py-vars:main:pv2": (
        "Numbers are a different type than text.\n\n"
        "count = 10 has no quotes — it is an integer you can add and compare. Ticket "
        "priority and page numbers are usually integers."
    ),
    "py-vars:main:pv3": (
        "Booleans are True/False flags.\n\n"
        "APIs and filters use them constantly (active, synced, dry_run). Note the capital "
        "T in True — lowercase true is not valid Python."
    ),
    "py-dict:main:pd1": (
        "A dict (dictionary) is a JSON object in Python: keys map to values.\n\n"
        "Incidents, tickets, and API payloads are almost always dicts. Curly braces {} "
        "start one. Square brackets [] are for lists."
    ),
    "py-list-loop:main:pl1": (
        "A list holds an ordered sequence of items — often many dicts from an API.\n\n"
        "When monitoring returns 50 incidents, you get a list. Loops + filters operate on lists."
    ),
    "py-if:main:pi2": (
        "A set (or list) of allowed values makes filter rules obvious.\n\n"
        "SYNC_SEVERITIES = {'critical', 'high'} is the business rule in code: only sync "
        "these. Change the set later without rewriting the whole loop."
    ),
    "py-if:main:pi3": (
        "if checks a condition before running a block of code.\n\n"
        "Here: if this incident's severity is in our allow-list, keep it; else skip. "
        "That is the heart of 'only sync what matters' integrations."
    ),
    "py-function:main:pf1": (
        "A function packages reusable logic under a name.\n\n"
        "def severity_to_priority(...): means 'here is how we map severities.' You call it "
        "many times instead of copy-pasting the same if/elif everywhere."
    ),
    "py-transform:main:pt1": (
        "Transform means rename/reshape fields from source → destination.\n\n"
        "Monitoring might say facility; ticketing wants site. Your job as an integrator "
        "is the mapping, not hoping the two vendors match."
    ),
    "practice-status:drill:ps1": (
        "HTTP status codes are the API's short answer about what happened.\n\n"
        "200 OK means success for a typical GET. Learn the common codes so in a customer "
        "call you can diagnose 'is it auth, URL, or their server?' in seconds."
    ),
    "practice-status:drill:ps3": (
        "401 Unauthorized almost always means bad/missing credentials.\n\n"
        "Fix: check API key, Bearer spelling, and that load_dotenv actually ran. This is "
        "the #1 POC failure mode."
    ),
    "practice-status:drill:ps4": (
        "404 Not Found means the URL or id does not exist on that server.\n\n"
        "Fix: path typos, wrong port, or a resource id that was deleted. Different from 401."
    ),
    "practice-status:drill:ps5": (
        "409 Conflict often means 'this already exists' (duplicate create).\n\n"
        "In sync jobs you usually skip or update instead of failing the whole batch."
    ),
    "practice-status:drill:ps6": (
        "429 means you are calling too fast (rate limited).\n\n"
        "Fix: wait, exponential backoff, and retry. Production integrations must handle this."
    ),
    "practice-status:drill:ps7": (
        "5xx errors are the server's fault (or an outage), not your JSON shape.\n\n"
        "Retry later; do not rewrite your transform because of a 500."
    ),
    "practice-methods:drill:pm1": (
        "GET reads data. It should not create or delete anything.\n\n"
        "Safe to retry. Used for lists, detail fetches, and health checks."
    ),
    "practice-methods:drill:pm2": (
        "POST creates something new (a ticket, an event, a record).\n\n"
        "Often returns 201 Created. Sending the same POST twice may create duplicates or 409."
    ),
    "practice-methods:drill:pm3": (
        "PATCH updates only the fields you send.\n\n"
        "Prefer PATCH when you change status or one property without replacing the whole object."
    ),
    "practice-methods:drill:pm4": (
        "PUT usually replaces the whole resource with the body you send.\n\n"
        "More heavy-handed than PATCH — know which your destination API expects."
    ),
    "practice-methods:drill:pm5": (
        "DELETE removes a resource.\n\n"
        "Be careful in demos; prefer dry-run modes against production-like systems."
    ),
    "filter-python:main:fp2": (
        "Filtering in Python means: download (or already have) records, then keep a subset.\n\n"
        "Use this when the API cannot filter the way you need, or when rules are complex. "
        "Tradeoff: you may pull more data than necessary."
    ),
    "filter-api:main:fa2": (
        "Filtering via API params pushes the work to the server.\n\n"
        "severity=critical means the API only returns matching rows. Faster and cleaner "
        "when the vendor supports it — always ask in discovery."
    ),
    "sync-post-one:main:sp1": (
        "Sync = read from system A, transform, write to system B.\n\n"
        "This lesson posts one ticket so you see the full path before looping a batch."
    ),
    "sync-409:main:s409": (
        "Idempotent sync handles 'already exists' gracefully.\n\n"
        "If POST returns 409, skip or PATCH — do not crash. Real customer environments "
        "re-run jobs; duplicates are normal."
    ),
    "page-loop:main:pg1": (
        "Pagination means APIs return data in pages (chunks), not one giant dump.\n\n"
        "You loop page=1, page=2, ... until a page is empty or a cursor ends. Miss this "
        "and your demo silently shows only the first 25 records."
    ),
    "err-safe-get:main:es2": (
        "Safe helpers catch expected failures and return a clear result.\n\n"
        "Trying a missing id should not explode your whole script — return None or a "
        "message so the rest of the batch continues."
    ),
    "doc-readme:main:dr1": (
        "SE work is not done when the script runs — others must run it too.\n\n"
        "A short README: purpose, env vars, field map, and error behavior turns your POC "
        "into a reusable asset for the next SE."
    ),
    "demo-talktrack:main:dt1": (
        "Discovery before demo: state the customer problem in their words.\n\n"
        "If you cannot say the pain clearly, the API walkthrough will feel like a feature tour."
    ),
    "demo-discovery:main:dd1": (
        "Good discovery questions uncover process, pain, success criteria, and systems.\n\n"
        "You are not collecting trivia — you are finding which integration story to tell."
    ),
    "demo-discovery:main:dd2": (
        "Pain questions find what hurts today — time wasted, missed SLAs, manual copy-paste.\n\n"
        "Your integration demo should clearly reduce that pain, not just show cool API calls."
    ),
    "demo-discovery:main:dd3": (
        "Success criteria are how the customer will judge a win.\n\n"
        "Examples: 'critical alerts create tickets in under 2 minutes' or 'no duplicate tickets.' "
        "Write them down; demo against them."
    ),
    "demo-discovery:main:dd4": (
        "Systems questions map the landscape: monitoring, CMMS/ticketing, ERP, identity.\n\n"
        "You need source + destination (+ maybe identity) before you promise a sync."
    ),
    "demo-talktrack:main:dt4": (
        "Close by tying the demo back to success criteria and next steps.\n\n"
        "Ask for a technical validation workshop or a scoped POC — do not end on 'any questions?' only."
    ),
    "practice-status:drill:ps2": (
        "201 Created means a POST successfully made a new resource.\n\n"
        "Different from 200: the server is telling you something new exists (often with a Location "
        "header or an id in the body). Listen for this after ticket creates."
    ),
    "baby-import:main:bi3": (
        "Exact confirmation text is a precision drill.\n\n"
        "APIs and graders are picky. Training yourself to match required strings builds the same "
        "care you need for field names like external_id vs id."
    ),
    "baby-json:main:bj4": (
        "After parsing JSON, read a specific field — here, service.\n\n"
        "body['service'] (or .get) is how you pull meaning out of an API response. Wrong key → "
        "KeyError; that usually means you guessed the schema instead of inspecting it."
    ),
    "py-vars:main:pv4": (
        "Print all variables to prove each assignment worked.\n\n"
        "Debugging habit: after setup, print the config you think you have (never print live secrets "
        "in real customer demos — mask them)."
    ),
    "py-dict:main:pd2": (
        "Add the fields your later filter will care about — severity and facility.\n\n"
        "Dicts grow key by key. Same as filling a JSON object in Postman before you POST."
    ),
    "py-dict:main:pd3": (
        "message (or description) is the human-readable alert text.\n\n"
        "Tickets need a title/body humans can act on. Pull it from the source event; do not invent it."
    ),
    "py-dict:main:pd4": (
        "Print dict fields with incident['key'] to practice bracket access.\n\n"
        "This is identical to reading JSON in a real response. Get comfortable before networking."
    ),
    "py-list-loop:main:pl2": (
        "for x in my_list: is the skeleton every batch job uses.\n\n"
        "Indented lines under the for run once per item. Forget indentation and Python will error "
        "or only run once."
    ),
    "py-list-loop:main:pl3": (
        "Print each id while looping to verify you are iterating the list, not the dict keys.\n\n"
        "If you accidentally loop a dict, you get keys — a common mix-up."
    ),
    "py-list-loop:main:pl4": (
        "Confirm every expected id appeared — proves length and content together.\n\n"
        "Same idea as checking three tickets got created after a sync demo."
    ),
    "py-if:main:pi1": (
        "Start with a small hard-coded list of incident dicts.\n\n"
        "Offline data lets you practice filter logic with no network. Later you swap in API results."
    ),
    "py-if:main:pi4": (
        "Assert only critical and high survived the filter.\n\n"
        "If a medium/low slipped through, your if condition is wrong — fix before wiring POST."
    ),
    "sync-transform:main:st1": (
        "One realistic incident dict is enough to design the mapping.\n\n"
        "Nail transform on a single example, then apply it inside a loop for the full feed."
    ),
    "sync-transform:main:st4": (
        "Print the ticket dict and read it like a customer would.\n\n"
        "Check external_id, priority, site/title fields. If anything still looks like the source "
        "schema, the transform is incomplete."
    ),
    "practice-methods:drill:pm5": (
        "DELETE removes a resource from the destination system.\n\n"
        "In demos, prefer soft-delete or dry-run flags when the API offers them. Accidental deletes "
        "during a live POC are hard to recover from mid-call."
    ),
}

# Normalized title → context (used across many lessons)
TITLE_OVERRIDES = {
    "import os": (
        "os is Python's doorway to the operating system environment.\n\n"
        "You import it so you can call os.getenv(...) and read secrets/config that live "
        "outside your code. That keeps API keys out of git."
    ),
    "import requests": (
        "requests is the library that speaks HTTP for you.\n\n"
        "Instead of hand-building TCP sockets, you call requests.get / requests.post. "
        "Almost every Python API POC an SE writes starts with this import."
    ),
    "imports": (
        "Imports load tools your script needs before any real work happens.\n\n"
        "Think of them as opening the toolbox: os for secrets, requests for HTTP, dotenv "
        "for local .env files. Order them at the top — that is the convention."
    ),
    "imports + dotenv": (
        "First load libraries, then load local secrets.\n\n"
        "import lines make tools available; load_dotenv() actually reads .env into the "
        "environment so getenv works. Skip either piece and auth fails mysteriously."
    ),
    "call load_dotenv()": (
        "load_dotenv() reads key=value pairs from a .env file into environment variables.\n\n"
        "It is a function call — parentheses required. After it runs, os.getenv('SOURCE_API_KEY') "
        "can see the training key without hardcoding."
    ),
    "setup": (
        "Setup is the boring-but-critical prologue every integration needs.\n\n"
        "Imports, dotenv, API key, base URL, headers. Get this wrong and every later step "
        "looks 'broken' when the real issue is auth or the wrong host."
    ),
    "setup imports": (
        "Start by importing the libraries this script will use.\n\n"
        "No network calls yet — just make sure Python can see requests/os/dotenv. This "
        "isolates 'environment problems' from 'API logic problems.'"
    ),
    "setup + dotenv": (
        "Wire up imports and load .env before any GET/POST.\n\n"
        "If dotenv is missing, getenv returns None, Bearer headers become 'Bearer None', "
        "and you get a confusing 401."
    ),
    "setup + get": (
        "Fetch the data first, then transform or filter it.\n\n"
        "Pattern: authenticate → GET list → work on response['data']. Most sync jobs "
        "start exactly this way."
    ),
    "setup + get open": (
        "Pull open incidents from the monitoring mock as your working set.\n\n"
        "Open = currently needing attention. Filtering to open keeps the demo focused on "
        "actionable ops noise, not historical clutter."
    ),
    "bearer headers": (
        "Headers are extra metadata sent with an HTTP request.\n\n"
        "Authorization: Bearer <token> is how this API knows who you are. You build a "
        "small dict of headers and pass headers=... into requests.get/post."
    ),
    "build bearer headers": (
        "Build a headers dict once and reuse it on every call.\n\n"
        '{"Authorization": f"Bearer {api_key}"} is the standard shape. One typo in Bearer '
        "and every request fails auth."
    ),
    "get /v1/incidents": (
        "GET /v1/incidents asks the monitoring API for the incident list.\n\n"
        "The path is the resource. Combined with the base URL and headers, this is a full "
        "authenticated read — the core motion of every ops integration."
    ),
    "get open incidents": (
        "Request only open incidents so the payload matches the demo story.\n\n"
        "Usually via params like status=open. Smaller responses are easier to reason about "
        "in a live SE walkthrough."
    ),
    "get with auth": (
        "Same GET as before, but now the Authorization header must be present.\n\n"
        "You are proving end-to-end: secrets loaded → header built → server accepts → body returns."
    ),
    "get with params": (
        "Pass a params dict so requests adds ?key=value to the URL for you.\n\n"
        "You stay in Python data structures instead of hand-concatenating query strings "
        "(error-prone when values need encoding)."
    ),
    "get with f-string": (
        "An f-string lets you build a URL from variables: f\"{BASE}/health\".\n\n"
        "Readable and safe for path segments you control. Prefer params= for query filters."
    ),
    "print status code": (
        "Printing status_code is the fastest feedback loop while learning.\n\n"
        "200/201 → keep going. 401 → fix auth. 404 → fix URL/id. Make this reflex before "
        "you dig into JSON."
    ),
    "print count": (
        "A count proves your filter and auth actually returned what you expected.\n\n"
        "len(data['data']) is a classic SE check before showing a customer 'we pulled N open alerts.'"
    ),
    "print json": (
        "Printing JSON (or the parsed dict) lets you see the real shape of the API.\n\n"
        "Field names matter later for transforms. Always inspect once before writing mapping code."
    ),
    "print results": (
        "Show the filtered results so you can visually confirm the rule worked.\n\n"
        "In a demo, narrate what the customer should see: 'only critical rows remain.'"
    ),
    "print matches": (
        "Print the rows that matched your facility/keyword rule.\n\n"
        "This is client-side search practice — useful when the API lacks a perfect filter."
    ),
    "print filtered count": (
        "Compare filtered count vs raw count to prove the rule.\n\n"
        "If both are equal, your filter did nothing (or everything matched). Great debugging habit."
    ),
    "print id": (
        "Start by printing one field per item — usually the id.\n\n"
        "Ids become external_id when you create tickets. Confirm you can see them before "
        "adding more fields."
    ),
    "print id, severity, facility": (
        "Print the fields ops people actually care about in a triage glance.\n\n"
        "Id + severity + facility is enough to tell a story: what, how bad, where."
    ),
    "parse json": (
        "Turn the HTTP body into a Python object with response.json().\n\n"
        "After this, you navigate with keys like body['data'][0]['severity']. Raw text is "
        "harder to filter and transform."
    ),
    "parse + count": (
        "Parse the envelope, then count items in data.\n\n"
        "Many APIs wrap lists as {\"data\": [...]}. Counting the wrapper dict itself is a "
        "common beginner mistake."
    ),
    "raise_for_status": (
        "Fail fast on HTTP errors before you touch the body.\n\n"
        "raise_for_status() raises if status is 4xx/5xx. Put it right after the request."
    ),
    "raise_for_status()": (
        "Fail fast on HTTP errors before you touch the body.\n\n"
        "raise_for_status() raises if status is 4xx/5xx. Put it right after the request."
    ),
    "for loop": (
        "Looping is how you process each API record the same way.\n\n"
        "for item in items: runs the indented block once per element — print, filter, or POST."
    ),
    "set the url": (
        "Put the full endpoint URL (or base + path) in a variable.\n\n"
        "Hardcoding the string in five places guarantees you will update four of them later."
    ),
    "base variable": (
        "BASE (or SOURCE_API_URL) is the host root without a specific resource path.\n\n"
        "You append /health or /v1/incidents as needed. Port 5001 is monitoring; 5002 is ticketing "
        "in this bootcamp."
    ),
    "load key with getenv": (
        "Read the API key from the environment at runtime.\n\n"
        "api_key = os.getenv('SOURCE_API_KEY'). If this is None, stop and fix .env — do not "
        "continue with a broken Bearer header."
    ),
    "load key + url": (
        "Load both the secret and the base URL from env/defaults.\n\n"
        "Keys must come from getenv. URLs can default to localhost for class, but still "
        "belong in variables."
    ),
    "load key and url": (
        "Load both the secret and the base URL from env/defaults.\n\n"
        "Keys must come from getenv. URLs can default to localhost for class, but still "
        "belong in variables."
    ),
    "hardcode api key (ok here)": (
        "This baby step hardcodes a key only so you can see the header shape clearly.\n\n"
        "The next lessons replace this with getenv + dotenv. Never commit real customer keys."
    ),
    "key, url, headers": (
        "Assemble the three ingredients every authenticated call needs.\n\n"
        "Key (who you are), URL (where to talk), headers (how you present the key). Then GET."
    ),
    "auth + get + parse": (
        "One combined motion: authenticate, fetch, parse.\n\n"
        "After this block you hold a Python list of incidents ready for a loop — the sync backbone."
    ),
    "sync_severities": (
        "Name the business rule in a constant.\n\n"
        "SYNC_SEVERITIES documents intent for the next SE who reads your POC: only these "
        "severities create tickets."
    ),
    "filter in a list": (
        "Build a new list that only contains rows matching your rule.\n\n"
        "list comprehensions or append-inside-if both work. Output should be smaller than input."
    ),
    "filter by facility": (
        "Keep incidents whose facility/site text matches a keyword.\n\n"
        "Client-side string search is common when APIs lack rich search — disclose the "
        "limitation in discovery."
    ),
    "keyword constant": (
        "Store the search keyword in a named variable.\n\n"
        "Easier to change for a demo ('Memorial' vs 'Plant 3') than editing the if condition."
    ),
    "severity=critical param": (
        "Ask the API to return only critical rows using a query parameter.\n\n"
        "Server-side filter = less data over the wire and a clearer demo narrative."
    ),
    "start page loop": (
        "Initialize page (or cursor) before entering the while/for pagination loop.\n\n"
        "You will increment after each successful fetch until there is no next page."
    ),
    "get with limit=2": (
        "A tiny limit forces multiple pages on purpose in training.\n\n"
        "In production limits are larger, but the loop structure is identical."
    ),
    "print total": (
        "Accumulate a running total across pages so you know the full population.\n\n"
        "If you only print the last page, you under-count — a classic pagination bug."
    ),
    "safe_get_incident": (
        "Wrap GET-by-id in a helper that handles 404 without killing the script.\n\n"
        "Batch jobs need per-item error handling; one bad id should not stop the rest."
    ),
    "try a real id": (
        "Prove the happy path with a known-good id from the mock data.\n\n"
        "Always demo success before failure — builds trust, then shows resilience."
    ),
    "try a missing id": (
        "Prove the failure path with an id that does not exist.\n\n"
        "Customers ask 'what if the asset was deleted?' — show a calm, handled response."
    ),
    "purpose section": (
        "README Purpose tells a teammate what problem this script solves in one screen.\n\n"
        "Write for another SE at 11pm before a POC — clarity beats cleverness."
    ),
    "env vars section": (
        "Document every required environment variable and where to get values.\n\n"
        "Missing this is why POCs that 'worked on my laptop' fail on someone else's."
    ),
    "field mapping section": (
        "Write the source→destination field map in English/table form.\n\n"
        "This is the integration contract. Code implements it; docs explain it."
    ),
    "errors section": (
        "Document how the script behaves on 401/404/409/5xx.\n\n"
        "Support and SEs need this when a customer forwards a stack trace mid-call."
    ),
}


CONCEPT_RULES = [
    (("import os",), TITLE_OVERRIDES["import os"]),
    (("import requests",), TITLE_OVERRIDES["import requests"]),
    (("load_dotenv",), TITLE_OVERRIDES["call load_dotenv()"]),
    (("getenv",), TITLE_OVERRIDES["load key with getenv"]),
    (("authorization", "bearer"), TITLE_OVERRIDES["bearer headers"]),
    (("raise_for_status",), TITLE_OVERRIDES["raise_for_status"]),
    (("status_code",), TITLE_OVERRIDES["print status code"]),
    ((".json()",), TITLE_OVERRIDES["parse json"]),
    (("params",), TITLE_OVERRIDES["get with params"]),
    (("timeout",), (
        "timeout=... tells requests how long to wait before giving up.\n\n"
        "Without a timeout, a hung API can freeze your demo indefinitely. Always set one "
        "(seconds). Reliability is part of the SE story, not an afterthought."
    )),
    (("external_id",), (
        "external_id links a ticket back to the source system's id.\n\n"
        "That is how you avoid duplicates and how support traces 'this ticket came from "
        "incident INC-123.' Always preserve the source primary key in the transform."
    )),
    (("priority",), (
        "Priority is usually a number the destination system understands.\n\n"
        "Source systems often say critical/high/low as words. Your transform maps those "
        "words onto the ticket schema (e.g. critical → 1)."
    )),
    (("transform",), (
        "Transform reshapes one system's fields into another system's schema.\n\n"
        "This is the core of integration work: not just calling APIs, but making meaning "
        "line up between vendors."
    )),
    (("post", "ticket"), (
        "POST sends a new ticket (or record) to the destination API.\n\n"
        "Body is usually JSON from your transform. Check for 201/200 success and handle 409 "
        "duplicates in real sync jobs."
    )),
    (("paginat",), TITLE_OVERRIDES["start page loop"]),
    (("409",), (
        "409 Conflict often means 'this already exists' (duplicate create).\n\n"
        "In sync jobs you usually skip or update instead of failing the whole batch."
    )),
]


def public_step_fields(step: dict) -> dict:
    """Fields safe to send to the browser for the steps panel."""
    return {
        "id": step.get("id", ""),
        "title": step.get("title", ""),
        "instruction": step.get("instruction", ""),
        "example": step.get("example", ""),
        "context": step.get("context", ""),
        "why": step.get("why", ""),
        "common_mistake": step.get("common_mistake", ""),
        "reveal_after_fails": step.get("reveal_after_fails", 2),
    }
