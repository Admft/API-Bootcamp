# Samsara Sales Engineer Role Playbook

Use this alongside the coding lessons. The role is not simply “write Python.” The goal is to discover an operational problem, prove a useful integration, and explain it clearly enough for a customer to trust the solution.

## Capstone Customer Scenario

A regional field-services company receives safety, vehicle, equipment, and facility events in a connected-operations platform. Dispatch and maintenance teams work from a separate ticketing system. Important events are copied manually, causing delays, inconsistent priority, and occasional duplicate work.

Your proof of concept retrieves open operational events, selects critical and high-severity records, maps them to the customer's work-order schema, and creates tickets.

The mock endpoints in this repository are fictional training APIs—not official Samsara endpoints.

## Discovery Before Code

Ask these questions before proposing the integration:

1. Which operational events require action, and which create noise?
2. Who owns the response: safety, dispatch, maintenance, or an external installer?
3. What system is the team's source of truth after an event occurs?
4. What fields are required to create a usable work order?
5. How quickly must the event appear in the destination system?
6. What should happen when a record is missing data or the destination is unavailable?
7. How will we prevent duplicates and prove that no event was lost?
8. What outcome defines a successful POC: response time, fewer manual steps, or better compliance?

## Translate Requirements Into the Build

- “Only urgent events” → severity filtering
- “Use our existing workflow” → destination API and schema mapping
- “Never expose credentials” → environment variables
- “Do not create duplicate work” → external IDs and `409 Conflict` handling
- “Handle larger fleets” → pagination
- “Do not hang our process” → request timeouts
- “Help support troubleshoot it” → logs, counters, and documentation

## Five-Minute Demo

### 1. Restate the problem (30 seconds)

“Your team currently copies urgent operational events into the work-order system. We want to reduce that manual delay while preserving the system your operators already use.”

### 2. Confirm the success criteria (30 seconds)

“For this POC, success means critical and high-priority open events create correctly mapped work orders, credentials stay outside the code, and rerunning the integration creates no duplicates.”

### 3. Show the API interaction (60 seconds)

Use Postman to show:

- Bearer authentication
- `GET /v1/incidents`
- Query parameters
- JSON response and pagination metadata
- One expected error such as `401` or `404`

### 4. Run the Python integration (90 seconds)

Explain the flow without narrating every line:

1. Read configuration
2. Fetch all pages
3. Apply the customer's event criteria
4. Map source fields to destination fields
5. Create work orders
6. Count created, skipped, and failed records

Run it twice to demonstrate idempotency.

### 5. Close on value and next steps (90 seconds)

“This proves the workflow and data mapping. Before production, we would validate official endpoint contracts, rate limits, event volume, retry behavior, ownership, security review, and deployment monitoring. Next, I would test this with representative customer data and agree on measurable POC acceptance criteria.”

## Technical Questions You Must Answer Clearly

- What is an API, endpoint, HTTP method, header, query parameter, and JSON body?
- Why use `POST` rather than `GET` to create a work order?
- What do `200`, `201`, `400`, `401`, `404`, `409`, `429`, and `500` mean?
- Why keep keys in environment variables?
- What is pagination, and why does it matter for a large fleet?
- What makes the integration idempotent?
- What happens during a timeout or partial failure?
- Is this polling or event-driven? When might a webhook be preferable?
- Where would this script run, and how would you monitor it?
- Which assumptions must be verified against official customer and product API documentation?

## IoT and Deployment Context

Be ready to explain the end-to-end path at a high level:

**device or sensor → vehicle/network connectivity → cloud platform → open API → customer business system**

The API script covers the cloud-to-business-system portion. It does not replace knowledge of hardware installation, power, cellular connectivity, CAN bus, PTO, or deployment planning. For this role, connect the script to that broader system instead of presenting it as an isolated coding exercise.

## POC Handoff Checklist

- [ ] Customer problem and owner are documented
- [ ] Success criteria are measurable
- [ ] Official API documentation and authentication are confirmed
- [ ] Source and destination field mappings are reviewed
- [ ] Secrets are externalized
- [ ] Pagination, timeouts, errors, duplicates, and rate limits are addressed
- [ ] Test data includes normal and failure cases
- [ ] Deployment owner and run frequency are named
- [ ] Logs and support procedure are documented
- [ ] Limitations and production next steps are stated

## Interview Story

Use this structure:

- **Situation:** An operations team manually transferred urgent events into its work-order platform.
- **Task:** Build a repeatable POC that demonstrated technical feasibility and customer value.
- **Action:** Clarified event criteria and success measures, tested the APIs in Postman, built a Python integration with secure configuration and resilient request handling, and documented the workflow.
- **Result:** Demonstrated automated ticket creation, duplicate prevention, and a clear path from POC to production validation.

Do not claim that the mock integration uses the official Samsara API. Describe it accurately as a role-specific simulation that demonstrates transferable open-API integration skills.
