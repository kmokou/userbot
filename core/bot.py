from core.client import client
from core.dispatcher import load_modules

async def start_bot():
    await client.start()
    load_modules(client)
    print("Userbot is running...")
    await client.run_until_disconnected()