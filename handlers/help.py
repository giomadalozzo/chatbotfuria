from telegram import Update
from telegram.ext import ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            "Os comandos disponíveis são esses:\n"
            "/molodoy - Saiba mais sobre a chegada do novo AWP da FURIA\n"
            "/yekindar - Saiba mais sobre a nova adição do time\n"
            "/proximosjogos - Agenda dos próximos jogos\n"
            "/stats - Veja as estatísticas dos jogadores do nossa lineup (digite o comando e o nome do jogador da FURIA Ex: /stats FalleN)\n"
            "/streams - Link da Twitch dos nossos jogadores\n"
            "/midia - Links das nossas redes sociais\n",
        parse_mode="Markdown"
    )