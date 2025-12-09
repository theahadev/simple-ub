from telethon import functions, types
from datetime import datetime

# send bot startup message to log channel
async def logstart(bot, log_channel_id):
    try:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = (
            "**#STARTED**\n"
            f"**Time:** `{now}`\n"
        )
        await bot.send_message(log_channel_id, msg)
        print("Startup message has been sent.")
    except Exception as e:
        print(f"Failed to send startup message: {e}")