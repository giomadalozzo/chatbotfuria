from telegram import Update
from telegram.ext import CallbackContext

async def error(update: Update, context: CallbackContext):
    await update.message.reply_text("Desculpe, esse comando não existe. Digite /ajuda para ver os comandos disponíveis.")