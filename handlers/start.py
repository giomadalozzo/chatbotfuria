from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            "**BEM-VINDO AO FURIOSO BOT! 🐾**\n\n"
            "Sou seu assistente oficial da FURIA no CS!\n"
            "Use os comandos abaixo para saber mais:\n"
            "/molodoy - Saiba mais sobre a chegada do novo AWP da FURIA\n"
            "/yekindar - Saiba mais sobre a nova adição do time\n"
            "/proximosjogos - Agenda dos próximos jogos\n"
            "/stats - Veja as estatísticas dos jogadores do nossa lineup\n"
            "/streams - Link da Twitch dos nossos jogadores\n"
            "/midia - Links das nossas redes sociais\n"
            "/ajuda - Ver comandos disponíveis",
        parse_mode="Markdown"
    )