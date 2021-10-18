import asyncio
import configparser
import logging

from client import Client

config = configparser.ConfigParser()
config.read("settings.ini")
api_id = int(config["Telegram"]["api_id"])
api_hash = config["Telegram"]["api_hash"]
entity = config["Telegram"]["entity"]
logging.basicConfig(level=logging.INFO)
phones_file = open('phones.txt', 'r')
phones = phones_file.readlines()
clients = []
for phone in phones:
    phone = phone.strip()
    print(phone)
    client = Client(phone, api_id, api_hash, entity)
    clients.append(client)


async def main():
    await asyncio.wait([client.client.run_until_disconnected() for client in clients])


if __name__ == '__main__':
    print("Starting")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
