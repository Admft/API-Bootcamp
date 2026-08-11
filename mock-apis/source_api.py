"""
Mock Monitoring API — simulates a utility/operations incident system.

Run standalone:  python source_api.py
Default port:    5001
Auth:            Bearer dev-source-key-12345  OR  X-API-Key header
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
VALID_KEYS = {"dev-source-key-12345"}

INCIDENTS = [
    {
        "id": "INC-38192",
        "facility": "Water Treatment Plant 4",
        "severity": "critical",
        "status": "open",
        "message": "Pump pressure below threshold",
    },
    {
        "id": "INC-38193",
        "facility": "Substation North",
        "severity": "high",
        "status": "open",
        "message": "Transformer temperature elevated",
    },
    {
        "id": "INC-38194",
        "facility": "Gas Distribution Hub 2",
        "severity": "medium",
        "status": "open",
        "message": "Pressure regulator fluctuation",
    },
    {
        "id": "INC-38195",
        "facility": "Water Treatment Plant 4",
        "severity": "low",
        "status": "open",
        "message": "Routine sensor calibration due",
    },
    {
        "id": "INC-38196",
        "facility": "Emergency Operations Center",
        "severity": "critical",
        "status": "open",
        "message": "Backup generator failed self-test",
    },
    {
        "id": "INC-38197",
        "facility": "Regional Data Center",
        "severity": "high",
        "status": "closed",
        "message": "Cooling unit offline — resolved",
    },
    {
        "id": "INC-38198",
        "facility": "Pipeline Section 7B",
        "severity": "critical",
        "status": "open",
        "message": "Flow rate anomaly detected",
    },
    {
        "id": "INC-38199",
        "facility": "Wastewater Plant 1",
        "severity": "medium",
        "status": "open",
        "message": "Chemical dosing pump delay",
    },
    {
        "id": "INC-38200",
        "facility": "Solar Farm East",
        "severity": "low",
        "status": "open",
        "message": "Inverter efficiency below baseline",
    },
    {
        "id": "INC-38201",
        "facility": "Hospital Grid Tie-In",
        "severity": "critical",
        "status": "open",
        "message": "Voltage sag on critical feeder",
    },
    {
        "id": "INC-38202",
        "facility": "Dam Control Station",
        "severity": "high",
        "status": "open",
        "message": "Gate actuator response slow",
    },
    {
        "id": "INC-38203",
        "facility": "Telecom Tower 44",
        "severity": "medium",
        "status": "closed",
        "message": "Battery backup test passed",
    },
]


def authenticate():
    auth_header = request.headers.get("Authorization", "")
    api_key = request.headers.get("X-API-Key", "")

    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        if token in VALID_KEYS:
            return None

    if api_key in VALID_KEYS:
        return None

    return jsonify({"error": "Unauthorized", "message": "Invalid or missing API key"}), 401


@app.route("/v1/incidents", methods=["GET"])
def list_incidents():
    auth_error = authenticate()
    if auth_error:
        return auth_error

    status = request.args.get("status")
    severity = request.args.get("severity")
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 100))

    filtered = INCIDENTS
    if status:
        filtered = [i for i in filtered if i["status"] == status]
    if severity:
        filtered = [i for i in filtered if i["severity"] == severity]

    start = (page - 1) * limit
    end = start + limit
    page_data = filtered[start:end]

    return jsonify(
        {
            "data": page_data,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": len(filtered),
                "has_more": end < len(filtered),
            },
        }
    )


@app.route("/v1/incidents/<incident_id>", methods=["GET"])
def get_incident(incident_id):
    auth_error = authenticate()
    if auth_error:
        return auth_error

    for incident in INCIDENTS:
        if incident["id"] == incident_id:
            return jsonify(incident)

    return jsonify({"error": "Not found", "message": f"Incident {incident_id} not found"}), 404


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "monitoring-api"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
