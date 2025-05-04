from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from services.hltv_service import HLTVAchievementsService
from constants import Messages

class AchievementsHandler(BaseHandler):
    """Handler for FURIA Achievements"""
    
    def __init__(self):
        self.service = HLTVAchievementsService()
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            achievements = self.service.get_furia_achievements()
            formatted_achievements = "\n".join([f"🏆 {a}" for a in achievements["achievements"]])
            
            await update.message.reply_text(
                f"*🏆 Histórico de Títulos da FURIA (CS:GO/CS2)*\n\n{formatted_achievements}",
                parse_mode="Markdown"
            )
            logger.info(f"Achievements sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in achievements handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_achievements_handler():
    return AchievementsHandler()
