from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages, URLs

class MolodoyHandler(BaseHandler):
    """Handler about Molodoy"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.chat.send_photo(
                photo=URLs.PLAYER_IMAGES['molodoy'],
                caption="Jogador Molodoy, novo AWP da FURIA."
            )
            await update.message.reply_text(
                Messages.MOLODOY_INFO,
                parse_mode="Markdown"
            )
            logger.info(f"Molodoy info sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in molodoy handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_molodoy_handler():
    return MolodoyHandler()
