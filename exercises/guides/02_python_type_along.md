# Type-Along 02 — Python Basics (45 min)

**Use the on-screen steps with examples** — type one step, click Analyze, then go to the next. Don't binge the whole guide.

**Create a new empty file:** `exercises/my-work/02_basics.py`

Type each step. Save and run after every checkpoint.

---

## Step 1 — Your first incident dictionary

Type this:

```python
incident = {
    "id": "INC-38192",
    "facility": "Water Treatment Plant 4",
    "severity": "critical",
    "message": "Pump pressure below threshold",
}
```

**Checkpoint — run:**
```powershell
python exercises/my-work/02_basics.py
```

No output yet? Good — no errors means you're fine.

---

## Step 2 — Read from a dictionary

Add below what you typed:

```python
print(incident["facility"])
print(incident["severity"])
```

**Run it.** You should see:
```
Water Treatment Plant 4
critical
```

**What you learned:** Dictionaries use `key` in square brackets. JSON from APIs works the same way.

---

## Step 3 — A list of incidents

Add:

```python
incidents = [
    {"id": "INC-001", "severity": "critical", "facility": "Plant A"},
    {"id": "INC-002", "severity": "low", "facility": "Plant B"},
    {"id": "INC-003", "severity": "high", "facility": "Plant C"},
]
```

Loop through them:

```python
for item in incidents:
    print(item["id"], item["severity"])
```

**Run it.** Three lines printed? Good.

---

## Step 4 — Filter with an if statement

Delete the simple loop (or comment it out). Add:

```python
SYNC_SEVERITIES = ["critical", "high"]

for item in incidents:
    if item["severity"] in SYNC_SEVERITIES:
        print(f"WILL SYNC: {item['id']} — {item['facility']}")
    else:
        print(f"SKIP: {item['id']}")
```

**Run it.** You should see WILL SYNC for INC-001 and INC-003, SKIP for INC-002.

**What you learned:** This is exactly what integration scripts do — loop data, filter what matters.

---

## Step 5 — A transformation function

Add:

```python
def severity_to_priority(severity):
    if severity == "critical":
        return 1
    if severity == "high":
        return 2
    if severity == "medium":
        return 3
    return 4
```

Test it:

```python
print(severity_to_priority("critical"))
print(severity_to_priority("low"))
```

**Run it.** Should print `1` then `4`.

---

## Step 6 — Map source → destination (the core skill)

Add:

```python
def transform_incident(inc):
    return {
        "external_id": inc["id"],
        "site": inc["facility"],
        "description": inc.get("message", "No description"),
        "priority": severity_to_priority(inc["severity"]),
    }
```

Test with your first incident:

```python
ticket = transform_incident(incident)
print(ticket)
```

**Run it.** You should see a dictionary with `external_id`, `site`, `description`, `priority`.

This is **schema mapping** — the heart of every integration job.

---

## Step 7 — Wrap in main

Add at the bottom:

```python
if __name__ == "__main__":
    print("=== Exercise 02 complete ===")
    for item in incidents:
        if item["severity"] in SYNC_SEVERITIES:
            ticket = transform_incident(item)
            print(f"Ticket ready: {ticket['external_id']} priority={ticket['priority']}")
```

**Run it**, then verify:

```powershell
python exercises/verify/verify_02.py
```

If verify passes, move to **Guide 03**.

---

## Stuck?

<details>
<summary>incident["facility"] gives KeyError</summary>
Check spelling of keys. Python is case-sensitive: `"facility"` not `"Facility"`.
</details>

<details>
<summary>SyntaxError on the f-string</summary>
Make sure you're on Python 3. f-strings need the `f` prefix: `f"text {variable}"`
</details>

Peek at `solutions/exercises/02_python_basics.py` only after two failed verify attempts.
