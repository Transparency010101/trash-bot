import os
import logging

from dotenv import load_dotenv

from config import log_mod
from events import client

load_dotenv()

try:
    handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
except FileNotFoundError:
    os.mkdir("logs")

if __name__ == "__main__":
    token = os.getenv("ID_TOKEN")
    client.run(token, log_handler=handler if log_mod else None)
