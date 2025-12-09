from telethon import TelegramClient
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv
import asyncio
import importlib

# Load environment variables
load_dotenv()

# Telethon stuff
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
session_string = os.getenv("SESSION_STRING")

# If the bot has admin specific behaivour, set sudo users
# sudo_env = os.getenv('SUDO_USERS')

# Bot log channel id, better to have
log_channel_id = int(os.getenv("LOG_CHANNEL_ID"))

# If bot needs to store data permanently somewhere
data_folder = os.getenv("DATA_FOLDER")

# Trigger character for commands (default to '.' if not set)
trigger_char = os.getenv("TRIGGER_CHAR", ".")

# convert sudo users env value into a python list
# sudo_users = [int(x.strip()) for x in sudo_env.split(',')]

# Test if sudo users are parsed correctly
# print(sudo_users[])

# for i in range(len(sudo_users)):
#    print(sudo_users[i])

# Ensure data folder exists
if data_folder and not os.path.exists(data_folder):
    os.makedirs(data_folder, exist_ok=True)

# init bot with session string
bot = TelegramClient(StringSession(session_string), api_id, api_hash)
bot.start()

# import setup utils
from handlers.init import logstart

# auto registerer for commands
for filename in os.listdir("handlers"):
    if filename.endswith(".py") and filename not in ["init.py"]:
        module_name = filename[:-3]  # removes the .py
        module = importlib.import_module(f"handlers.{module_name}")
        if hasattr(module, "register"):
            module.register(bot, trigger_char)
            print(f"Loaded handler: {module_name}")

if __name__ == '__main__':
    print("Starting bot...")

    async def main():
        # for logging bot startup
        await logstart(bot, log_channel_id)
        await bot.run_until_disconnected()
    with bot:
        bot.loop.run_until_complete(main())
