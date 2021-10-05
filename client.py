from telethon.events import NewMessage
from telethon import TelegramClient


class Client:
    def __init__(self, phone, api_id, api_hash, entity):
        self.client = TelegramClient(phone, api_id, api_hash)
        self.entity = entity
        self.client.start(phone=lambda: phone)

    async def main(self):
        self.client.add_event_handler(self.handler, NewMessage(incoming=True))
        await self.client.run_until_disconnected()

    async def handler(self, event):
        await self.client.forward_messages(self.entity, event.message)
        print(event.message.message)
