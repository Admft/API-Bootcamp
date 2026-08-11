"""Solution for Exercise 02."""

incident = {
    "id": "INC-38192",
    "facility": "Water Treatment Plant 4",
    "severity": "critical",
    "message": "Pump pressure below threshold",
}

print(incident["facility"])

SYNC_SEVERITIES = ["critical", "high"]


def should_sync(incident_dict, allowed_severities):
    return incident_dict["severity"] in allowed_severities


def severity_to_priority(severity):
    priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}
    return priority_map[severity]


if __name__ == "__main__":
    assert should_sync({"severity": "critical"}, SYNC_SEVERITIES) is True
    assert should_sync({"severity": "low"}, SYNC_SEVERITIES) is False
    assert severity_to_priority("critical") == 1
    print("Solution 02 OK")
