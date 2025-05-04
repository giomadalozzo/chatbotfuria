from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages

class SocialMediaHandler(BaseHandler):
    """Handler social media"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                Messages.SOCIAL_MEDIA,
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
            logger.info(f"Social media links sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in social media handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_social_media_handler():
    return SocialMediaHandler()
