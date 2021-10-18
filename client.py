import asyncio

from telethon.events import NewMessage
from telethon import TelegramClient


class Client:
    def __init__(self, phone, api_id, api_hash, entity):
        self.client = TelegramClient(phone, api_id, api_hash)
        self.entity = entity
        self.client.start(phone=lambda: phone)
        self.client.add_event_handler(self.forward, NewMessage(incoming=True))

    async def forward(self, event):
        print(event.message.message)
        await self.client.forward_messages(self.entity, event.message)
