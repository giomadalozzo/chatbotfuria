from telegram import Update
from telegram.ext import ContextTypes

async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            "**Siga a FURIA nas redes sociais! 🐾**\n\n"
            "X: [x.com/FURIA](https://x.com/FURIA)\n"
            "Facebook: [facebook.com/furiagg](https://www.facebook.com/furiagg)\n"
            "Instagram: [instagram.com/furiagg](https://www.instagram.com/furiagg)\n"
            "TikTok: [tiktok.com/@furia](https://www.tiktok.com/@furia)\n"
            "YouTube: [youtube.com/@FURIAgg](https://www.youtube.com/@FURIAgg)\n"
            "Website: [furia.gg](https://www.furia.gg/)\n",
        parse_mode="Markdown"
    )