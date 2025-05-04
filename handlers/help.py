from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages

class HelpHandler(BaseHandler):
    """Handler help options"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                Messages.HELP,
                parse_mode="Markdown"
            )
            logger.info(f"Help sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in help handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_help_handler():
    return HelpHandler()
