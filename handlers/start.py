from telethon import events
import re

def register(bot, trigger_char="."):
    @bot.on(events.NewMessage(pattern=f'{re.escape(trigger_char)}start'))
    async def start_handler(event):
        # if in pms
        if event.is_private:
            await event.reply(
f"""
This is a placeholder text for {trigger_char}start command in pm's.
""",
parse_mode="markdown")
        # if in a group
        elif event.is_group:
            await event.reply(
f"""
This is a placeholder text for {trigger_char}start command in groups.
""",
parse_mode="markdown")
        elif event.is_channel:
            await event.reply(
f"""
This is a placeholder text for {trigger_char}start command in channels.
""",
parse_mode="markdown")