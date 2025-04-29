from telegram import Update
from telegram.ext import ContextTypes

# Org Matches Function
async def matches(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aqui estão as partidas da FURIA 📅: https://www.hltv.org/team/8297/furia#tab-matchesBox")