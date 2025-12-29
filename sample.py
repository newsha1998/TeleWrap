import os
import sys
from dotenv import load_dotenv

# Add project root to path (for telewrap import)
sys.path.insert(0, os.path.dirname(__file__))

from telewrap.bot import Bot

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    name = os.getenv("BOT_NAME", "DefaultBot")
    
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found in environment variables.")
        print("Please create a .env file with TELEGRAM_BOT_TOKEN=your_token_here")
        return

    print(f"Initializing bot '{name}' with token from environment...")
    bot = Bot(token=token, name=name)
    
    print(f"Successfully initialized bot: {bot.name}")
    print(f"Token: {bot.token}")

if __name__ == "__main__":
    main()
