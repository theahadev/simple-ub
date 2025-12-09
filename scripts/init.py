#!/usr/bin/env python3
"""
Session String Generator for Telethon Bot
This script generates a session string for your Telethon bot.
"""

import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def generate_session_string():
    """Generate a session string for the bot"""
    
    # Get API credentials
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")
    
    if not api_id or not api_hash:
        print("❌ Error: API_ID and API_HASH must be set in your .env file")
        print("Get these from https://my.telegram.org")
        return
    
    try:
        api_id = int(api_id)
    except ValueError:
        print("❌ Error: API_ID must be a valid integer")
        return
    
    print("🚀 Starting session string generation...")
    print("📱 You will need to log in with your phone number")
    
    # Create client with StringSession
    client = TelegramClient(StringSession(), api_id, api_hash)
    
    try:
        await client.start()
        
        # Get the session string
        session_string = client.session.save()
        
        if not session_string:
            print("❌ Error: Failed to generate session string")
            return
        
        print("\n✅ Session string generated successfully!")
        print("📋 Copy this session string to your .env file as SESSION_STRING:")
        print("-" * 50)
        print(session_string)
        print("-" * 50)
        
        # Save to file as backup
        with open('session_string.txt', 'w') as f:
            f.write(session_string)
        
        print("💾 Session string also saved to 'session_string.txt'")
        print("\n⚠️  Important:")
        print("   - Keep this session string secure and private")
        print("   - Add SESSION_STRING=<your_string> to your .env file")
        print("   - Delete 'session_string.txt' after copying to .env")
        
    except Exception as e:
        print(f"❌ Error generating session: {e}")
    
    finally:
        await client.disconnect()
        # No temporary files to clean up when using StringSession

def main():
    """Main function"""
    print("=" * 60)
    print("🔑 Telethon Session String Generator")
    print("=" * 60)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ Error: .env file not found")
        print("Please create a .env file with API_ID and API_HASH")
        return
    
    # Run the async function
    asyncio.run(generate_session_string())

if __name__ == "__main__":
    main()