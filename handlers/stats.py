from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages, URLs

class StatsHandler(BaseHandler):
    """Handler for player stats"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            player_name = ' '.join(context.args).lower() if context.args else ''
            
            if player_name in URLs.PLAYER_STATS:
                await update.message.reply_text(
                    f"Aqui estão as estatísticas do {player_name.capitalize()} 📊: "
                    f"{URLs.PLAYER_STATS[player_name]}"
                )
                logger.info(f"Stats sent for {player_name} to {update.effective_user.id}")
            else:
                await update.message.reply_text(
                    f"Jogador não encontrado. Jogadores disponíveis:\n"
                    f"{', '.join(URLs.PLAYER_STATS.keys())}"
                )
        except Exception as e:
            logger.error("Error in stats handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_stats_handler():
    return StatsHandler()
