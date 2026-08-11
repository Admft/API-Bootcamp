# Integration Vocabulary — One Sentence Each

| Term | Definition |
|------|------------|
| **Authentication** | Proving who you are (API key, Bearer token, OAuth). |
| **Authorization** | What you're allowed to do after you're authenticated. |
| **REST** | Style of API using HTTP methods and URLs to operate on resources. |
| **Endpoint** | A specific URL + method combination, e.g. `GET /v1/incidents`. |
| **Payload** | The data you send in a request body (usually JSON). |
| **Request** | What you send to an API: method, URL, headers, body. |
| **Response** | What the API returns: status code, headers, body. |
| **JSON** | Text format for structured data — the lingua franca of APIs. |
| **Schema** | The expected shape/fields of request or response data. |
| **Mapping** | Translating fields from source schema to destination schema. |
| **Pagination** | Fetching large datasets in chunks (pages) instead of all at once. |
| **Rate limiting** | API throttling — too many requests returns 429. |
| **Timeout** | Max seconds to wait before giving up on a request. |
| **Retry** | Attempting a failed request again (often with backoff). |
| **Logging** | Recording what happened for debugging and audit trails. |
| **Idempotency** | Running the same operation twice doesn't create duplicates. |
| **Webhook** | Destination calls *you* when something happens (push). |
| **Polling** | You repeatedly call the source API to check for changes (pull). |
| **Environment variable** | Secret/config stored outside code, loaded at runtime. |
| **HTTP status code** | 3-digit number telling you if the request succeeded or failed. |
| **Bearer token** | Token sent in `Authorization: Bearer <token>` header. |
| **Query parameter** | Key-value pairs in URL after `?`, e.g. `?status=open`. |
| **OpenAPI** | Machine-readable API specification (Swagger docs). |

## Sales Engineer Pitch Template

> "I built a lightweight integration that retrieves operational incidents from a monitoring API, filters critical events, maps the source schema into the destination ticketing schema, and creates actionable work orders. Authentication is handled through environment variables, requests have error handling and timeouts, and the implementation is documented for other Sales Engineers."
