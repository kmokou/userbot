from telethon import TelegramClient, events
from config.settings import API_ID, API_HASH, SESSION_NAME

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)