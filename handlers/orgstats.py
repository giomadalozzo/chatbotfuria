from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger
from handlers.base_handler import BaseHandler
from constants import Messages

class OrgStatsHandler(BaseHandler):
    """Handler FURIA stats"""
    
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                "Aqui estão as estatísticas da FURIA no CS2 📊: "
                "https://www.hltv.org/team/8297/furia"
            )
            logger.info(f"Org stats sent to {update.effective_user.id}")
        except Exception as e:
            logger.error("Error in orgstats handler: %s", e)
            await update.message.reply_text(Messages.ERROR_GENERIC)

def create_org_stats_handler():
    return OrgStatsHandler()
