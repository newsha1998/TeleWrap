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
    def __init__(self, token: str, name: str):
        """
        Initialize the Bot.

        Args:
            token (str): The token of the bot.
            name (str): The name of the bot.
        """
        self.token = token
        self.name = name

        application = ApplicationBuilder().token(self.token).build()
        start_handler = CommandHandler('start', self.start)
        application.add_handler(start_handler)
        application.run_polling()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

