import antigravity
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token: str, name: str, maintainers: list[int] = None):
        """
        Initialize the Bot.

        Args:
            token (str): The token of the bot.
            name (str): The name of the bot.
            maintainers (list[int]): List of user IDs who are maintainers.
        """
        self.token = token
        self.name = name
        self.maintainers = set(maintainers) if maintainers else set()
        self.subscribers = set()

        self.application = ApplicationBuilder().token(self.token).build()
        start_handler = CommandHandler('start', self.start)
        self.application.add_handler(start_handler)

    def run(self):
        """
        Start the bot polling.
        """
        self.application.run_polling()

    async def send_message(self, chat_id: int, text: str):
        """
        Send a message to a specific user.

        Args:
            chat_id (int): The chat ID of the user.
            text (str): The message to send.
        """
        await self.application.bot.send_message(chat_id=chat_id, text=text)

    async def notify_users(self, text: str):
        """
        Send a notification argument to all subscribers.

        Args:
            text (str): The message to broadcast.
        """
        for chat_id in self.subscribers:
            try:
                await self.send_message(chat_id, text)
            except Exception as e:
                logger.error(f"Failed to send message to {chat_id}: {e}")

    def add_command(self, command: str, func, restricted: bool = False):
        """
        Add a command handler to the bot.

        Args:
            command (str): The command name (e.g. 'start').
            func (Callable): The function to call when the command is received.
                             It should accept (chat_id, text) as arguments.
            restricted (bool): If True, only maintainers can use this command.
        """
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
            chat_id = update.effective_chat.id
            text = update.message.text
            
            if restricted and chat_id not in self.maintainers:
                await context.bot.send_message(chat_id=chat_id, text="You are not authorized to use this command.")
                return

            await func(chat_id, text)

        handler = CommandHandler(command, wrapper)
        self.application.add_handler(handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        self.subscribers.add(chat_id)
        await context.bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me! You have been subscribed to notifications.")

