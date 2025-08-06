from config.settings import ADMIN_ID

def admin_only(func):
    async def wrapper(event):
        if not event.sender_id == ADMIN_ID:
            print(event.sender_id, ADMIN_ID)
            return
        return await func(event)
    return wrapper