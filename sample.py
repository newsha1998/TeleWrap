import os
import sys
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

    maintainers_str = os.getenv("MAINTAINER_IDS", "")
    maintainers = [int(x.strip()) for x in maintainers_str.split(",") if x.strip().isdigit()]
    
    print(f"Initializing bot '{name}' with token from environment...")
    print(f"Maintainers: {maintainers}")
    bot = Bot(token=token, name=name, maintainers=maintainers)
    
    print(f"Successfully initialized bot: {bot.name}")
    print(f"Token: {bot.token}")

    # Define a test handler to verify send_message
    async def test_command(chat_id, text):
        print(f"Received /test command from {chat_id}")
        await bot.send_message(chat_id=chat_id, text=f"Hello! This is a test message from {bot.name}.")

    # Add the handler to the bot's application
    bot.add_command("test", test_command)
    print("Added /test command. Send /test to the bot to verify send_message functionality.")

    # Define a broadcast handler to verify notify_users
    async def broadcast_command(chat_id, text):
        # In a real app, 'text' would contain the command and args, we might want to split
        # validation logic is skipped for simplicity
        message_to_send = text.replace("/broadcast", "").strip() or "Default Broadcast Message"
        print(f"Broadcasting message: {message_to_send}")
        await bot.notify_users(f"Alert: {message_to_send}")

    bot.add_command("broadcast", broadcast_command, restricted=True)
    print("Added /broadcast command. Send /broadcast <message> to the bot to verify notification.")

    # Define a handler to get user ID
    async def get_id_command(chat_id, text):
        await bot.send_message(chat_id=chat_id, text=f"Your User ID is: {chat_id}")

    bot.add_command("id", get_id_command)
    print("Added /id command. Send /id to get your user ID.")
    
    # Start the bot
    bot.run()

if __name__ == "__main__":
    main()
