import asyncio
import logging
import configparser
from threading import Thread

from client import Client

loop = asyncio.new_event_loop()


def side_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


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
        asyncio.run_coroutine_threadsafe(client.main(), loop)


thread = Thread(target=side_thread, args=(loop,), daemon=True)
thread.start()

if __name__ == '__main__':
    main()
