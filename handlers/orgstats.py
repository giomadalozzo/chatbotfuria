from telegram import Update
from telegram.ext import ContextTypes

# Org Stats Function
async def org_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aqui estão as estatísticas da FURIA no CS2 📊: https://www.hltv.org/team/8297/furia")