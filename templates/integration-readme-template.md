# Connected Operations Event → Work Order POC

## Purpose

<!-- One paragraph: customer workflow, what this integration does, and the business outcome -->

## Customer Problem

<!-- Who has the problem? What manual delay, risk, or inefficiency exists today? -->

## POC Success Criteria

- <!-- A measurable technical or business result -->
- <!-- Expected behavior for duplicates and failures -->

## Scope and Assumptions

- <!-- Confirm these are the correct official endpoints and schemas -->
- <!-- State volume, frequency, ownership, and other assumptions -->

## Requirements

- Python 3.10+
- `pip install requests python-dotenv`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SOURCE_API_KEY` | |
| `DESTINATION_API_KEY` | |

## Setup

```powershell
copy .env.example .env
# Edit .env with your keys
pip install -r requirements.txt
```

## Run

```powershell
python your_script.py
```

## Flow

1. 
2. 
3. 

## Field Mapping

| Source | Destination |
|--------|-------------|
| | |

## Error Handling

- HTTP failures:
- Timeouts:
- Missing fields:
- Rate limits:

## Production Considerations

- Deployment owner and run frequency:
- Monitoring and support:
- Retry or recovery approach:
- Security review:
- Polling vs. webhook decision:

## Demo

1. Restate the customer problem
2. Confirm success criteria
3. Show the source API response
4. Run the integration
5. Show destination records and duplicate prevention
6. Close with value, limitations, and next steps

## Security

Credentials via environment variables. Never commit secrets.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| | |
