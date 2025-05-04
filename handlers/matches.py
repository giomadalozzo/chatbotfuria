from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages

class MatchesHandler(BaseHandler):
    """Handler upcoming matches"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                "Aqui estão as partidas da FURIA 📅: "
                "https://www.hltv.org/team/8297/furia#tab-matchesBox"
            )
            logger.info(f"Matches sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in matches handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_matches_handler():
    return MatchesHandler()
