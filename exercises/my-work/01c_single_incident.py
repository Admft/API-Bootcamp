import os
import requests
from dotenv import load_dotenv 

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")

SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

incident_id = "INC-38201"

response = requests.get(
    f"{SOURCE_API_URL}/v1/incidents/{incident_id}",
    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},
    timeout=30,
)

response.raise_for_status()

incident = response.json()

print(incident["facility"])

print(incident["message"])

