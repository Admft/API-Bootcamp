"""
Mock Ticketing API — simulates ServiceNow / work-order destination system.

Run standalone:  python destination_api.py
Default port:    5002
Auth:            Bearer dev-dest-key-67890
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
VALID_KEYS = {"dev-dest-key-67890"}

# In-memory ticket store (resets when server restarts)
tickets = []
ticket_counter = 1000


def authenticate():
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        if token in VALID_KEYS:
            return None
    return jsonify({"error": "Unauthorized", "message": "Invalid or missing Bearer token"}), 401


@app.route("/v1/tickets", methods=["GET"])
def list_tickets():
    auth_error = authenticate()
    if auth_error:
        return auth_error
    return jsonify({"data": tickets, "total": len(tickets)})


@app.route("/v1/tickets", methods=["POST"])
def create_ticket():
    global ticket_counter

    auth_error = authenticate()
    if auth_error:
        return auth_error

    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Bad request", "message": "JSON body required"}), 400

    required = ["external_id", "site", "description", "priority"]
    missing = [f for f in required if f not in body]
    if missing:
        return jsonify(
            {"error": "Bad request", "message": f"Missing fields: {', '.join(missing)}"}
        ), 400

    # Idempotency: reject duplicate external_id
    for existing in tickets:
        if existing["external_id"] == body["external_id"]:
            return jsonify(
                {
                    "error": "Conflict",
                    "message": f"Ticket already exists for external_id {body['external_id']}",
                    "existing_ticket_id": existing["id"],
                }
            ), 409

    ticket_counter += 1
    ticket = {
        "id": f"TKT-{ticket_counter}",
        "external_id": body["external_id"],
        "site": body["site"],
        "description": body["description"],
        "priority": body["priority"],
        "status": "new",
    }
    tickets.append(ticket)

    return jsonify(ticket), 201


@app.route("/v1/tickets/by-external/<external_id>", methods=["GET"])
def get_by_external(external_id):
    auth_error = authenticate()
    if auth_error:
        return auth_error

    for ticket in tickets:
        if ticket["external_id"] == external_id:
            return jsonify(ticket)

    return jsonify({"error": "Not found"}), 404


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "ticketing-api", "ticket_count": len(tickets)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
