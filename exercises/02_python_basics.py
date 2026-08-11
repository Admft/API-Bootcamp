"""
LEGACY — prefer the type-along: exercises/guides/02_python_type_along.md
Create exercises/my-work/02_basics.py and type it yourself.
"""

# TODO 1: Create a dictionary representing one incident
# Keys: id, facility, severity, message
incident = None  # replace None

# TODO 2: Print the facility name from the dictionary
# print(...)

# TODO 3: Create a list of severity levels you want to sync (critical and high)
SYNC_SEVERITIES = []  # e.g. ["critical", "high"]

# TODO 4: Write a function that returns True if an incident should be synced
def should_sync(incident_dict, allowed_severities):
    """Return True if incident severity is in allowed_severities."""
    pass  # replace with your code

# TODO 5: Write a function that maps severity string to priority number
def severity_to_priority(severity):
    """
    critical → 1
    high     → 2
    medium   → 3
    low      → 4
    """
    pass  # replace with your code

# --- Tests (don't modify below) ---
if __name__ == "__main__":
    assert incident is not None, "TODO 1: create the incident dictionary"
    assert "facility" in incident, "TODO 1: incident needs a facility key"

    assert len(SYNC_SEVERITIES) >= 2, "TODO 3: add severity levels"

    assert should_sync({"severity": "critical"}, SYNC_SEVERITIES) is True
    assert should_sync({"severity": "low"}, SYNC_SEVERITIES) is False

    assert severity_to_priority("critical") == 1
    assert severity_to_priority("high") == 2

    print("All Exercise 02 checks passed!")
