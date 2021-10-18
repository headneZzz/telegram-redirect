import asyncio
import logging
import configparser
from threading import Thread
from client import Client


def worker(client):
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    new_loop.run_until_complete(client.main())

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    api_id = int(config["Telegram"]["api_id"])
    api_hash = config["Telegram"]["api_hash"]
    entity = config["Telegram"]["entity"]
    print('Starting')
    logging.basicConfig(level=logging.INFO)
    phones_file = open('phones.txt', 'r')
    phones = phones_file.readlines()
    for phone in phones:
        phone = phone.strip()
        print(phone)
        client = Client(phone, api_id, api_hash, entity)
        Thread(target=worker, args=[client]).start()


if __name__ == '__main__':
    main()
