"""BROKEN — wrong JSON key (site instead of facility)."""
incident = {
    "id": "INC-38192",
    "severity": "critical",
    "facility": "Water Treatment Plant 4",
    "message": "Pump pressure below threshold",
}

PRIORITY = {"critical": 1, "high": 2, "medium": 3, "low": 4}


def transform_incident(incident):
    return {
        "external_id": incident["id"],
        "site": incident["site"],  # BUG: should be facility
        "description": incident["message"],
        "priority": PRIORITY[incident["severity"]],
    }


ticket = transform_incident(incident)
print(ticket["site"])
print(ticket["priority"])
