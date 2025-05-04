from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages, URLs

class YekindarHandler(BaseHandler):
    """Handler about Yekindar"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.chat.send_photo(
                photo=URLs.PLAYER_IMAGES['yekindar'],
                caption="Jogador Yekindar, nova adição da FURIA."
            )
            await update.message.reply_text(
                Messages.YEKINDAR_INFO,
                parse_mode="Markdown"
            )
            logger.info(f"Yekindar info sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in yekindar handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_yekindar_handler():
    return YekindarHandler()
