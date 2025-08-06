import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "secrets.json"

with open(CONFIG_PATH, "r") as f:
    CONFIG = json.load(f)

API_ID = CONFIG["api_id"]
API_HASH = CONFIG["api_hash"]
SESSION_NAME = CONFIG["session_name"]
ADMIN_ID = int(CONFIG["admin_id"])