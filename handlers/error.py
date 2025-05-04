from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages

class ErrorHandler(BaseHandler):
    """Handler for unknown commands"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            logger.warning(f"Unknown command from {update.effective_user.id}: {update.message.text}")
            await update.message.reply_text(Messages.ERROR)
        except Exception as e:
            logger.error("Error in error handler: %s", e)

def create_error_handler():
    return ErrorHandler()
