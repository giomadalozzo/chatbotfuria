from telegram import Update
from telegram.ext import ContextTypes

async def streams(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            "**Siga nosso jogadores na roxinha 👾**\n\n"
            "[FalleN](https://www.twitch.tv/gafallen)\n"
            "[KSCERATO](https://www.twitch.tv/kscerato)\n"
            "[molodoy](https://www.twitch.tv/molodoy1818)\n"
            "[yekindar](https://www.twitch.tv/yekindar)\n"
            "[yuurih](https://www.twitch.tv/yuurih)\n",
        parse_mode="Markdown"
    )
