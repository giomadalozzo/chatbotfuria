from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from constants import Messages

class StartHandler:
    """Handler start command"""

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command"""
        try:
            await update.message.reply_text(
                Messages.WELCOME,
                parse_mode="Markdown"
            )
            logger.info(f"Start command executed by {update.effective_user.id}")
            
        except Exception as e:
            logger.error("Start error for {user.id}: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)
