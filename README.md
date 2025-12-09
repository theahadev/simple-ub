# Simple UserBot

An easy to use Telegram UserBot built using [telethon-core](https://github.com/theahadev/telethon-core).

## TODO
- [x] make the bot run correctly
- [x] add trigger character
- [ ] add su/sudo user check
- [ ] add sqlite/mongodb/json to store config
- [ ] add the ability to see command/handler list and remove handlers when needed
- [ ] add crash/error logging
  - add a wrapper script for running the main bot
  - manage crashes and restarts
- [ ] update the docker compose
- [x] make a init script
- [ ] add new instructions for init script in readme
- [ ] update readme for the new env file
- [ ] Add installer/setup scripts
- [ ] C O M M A N D   P R O X Y
- [ ] make command proxy actually work
- [ ] add auto ota updater ([@ZG089](https://github.com/ZG089) for the idea)


# The README file is not ready yet!

## Features

Coming soon!

## Requirements

- Python 3.11 or higher
- Telegram API credentials (API ID and API Hash)
- Telethon session string
 
## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/theahadev/simple-ub.git
cd simple-ub
```

2. Create a `.env` file with your credentials:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
DATA_FOLDER=./data
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/theahadev/simple-ub.git
cd simple-ub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials (see [Configuration](#configuration))

4. Run the bot:
```bash
python3 main.py
```

## Configuration

Create a `.env` file in the root directory with the following variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) | Yes |
| `API_HASH` | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | Yes |
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/botfather) | Yes |
| `DATA_FOLDER` | Directory for storing bot session and data (default: `./data`) | Yes |
| `TRIGGER_CHAR` | Character used to trigger commands (default: `~`) | No |
| `SUDO_USERS` | Comma-separated list of admin IDs | No |
| `LOG_CHANNEL_ID` | Channel ID for logging | No |

## Project Structure

```
telethon-core/
├── main.py                 # the main bot
├── requirements.txt        # py dependencies
├── Dockerfile             # docker image building
├── docker-compose.yml     # docker compose
├── .env                   # environment vars
├── data/                  # bot session and permanent data for handlers
└── handlers/              # handlers directory
    ├── init.py           # boot logging and command registering
    ├── start.py          # /start handler
    ├── help.py           # /help handler
    └── addchat.py        # adding to chat handler
```

## Creating Custom Handlers

To add a new command handler, create a Python file in the `handlers/` directory:

```python
from telethon import events

def register(bot, trigger_char="~"):
    @bot.on(events.NewMessage(pattern=f'{trigger_char}command'))
    async def command_handler(event):
        if event.is_private:
            await event.reply("Response in private chats")
        elif event.is_group:
            await event.reply("Response in groups")
        elif event.is_channel:
            await event.reply("Response in channels")
```
The bot will automatically load and register your handler on startup.

> **Note**: Optionally you can add it to `commands.txt` too.

## Available Commands

- `~start` - Start the bot (shows different messages in PMs, groups, and channels)
- `~help` - Display help information (context-aware responses)

> **Note**: The trigger character can be customized via the `TRIGGER_CHAR` environment variable.

## Development

### Adding New Features

1. Create a new handler file in the `handlers/` directory
2. Implement the `register(bot)` function
3. Use Telethon's event system to handle messages or events
4. The handler will be automatically loaded on bot restart

### Debugging

Check Docker logs:
```bash
docker-compose logs -f
```

Or run directly to see output:
```bash
python3 main.py
```

## Docker Commands

```bash
# Start the bot
docker compose up -d

# Stop the bot
docker compose down

# View logs
docker compose logs -f
```

## Security Notes

- Keep your .env file and session string secure.
- Do NOT install untrusted/sketchy modules. For official modules that are approved by the developer, check out [@simpleub](https://t.me/simpleub).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Commit your changes (`git commit -m 'Added rate limiting'`)
3. Push to the branch (`git push`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Telethon documentation](https://docs.telethon.dev/)

---
