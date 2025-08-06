from telethon import events
from utils.decorators import admin_only

def register(client):
    @client.on(events.NewMessage(pattern="^.ping"))
    @admin_only
    async def handler(event):
        await event.edit("Pong")
