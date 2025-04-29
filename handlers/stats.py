from telegram import Update
from telegram.ext import ContextTypes

# Player List and HLTV Links
player_links = {
    "fallen": "https://www.hltv.org/stats/players/2023/fallen",
    "yekindar": "https://www.hltv.org/stats/players/24145/yekindar",
    "molodoy": "https://www.hltv.org/stats/players/24146/molodoy",
    "yuurih": "https://www.hltv.org/stats/players/24147/yuurih",
    "kscerato": "https://www.hltv.org/stats/players/24148/kscerato"
}

# Player Stats Function
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player_name = ' '.join(context.args).lower()

    # Check if the player is in the list
    if player_name in player_links:
        link = player_links[player_name]
        await update.message.reply_text(f"Aqui estão as estatísticas do {player_name.capitalize()} 📊: {link}")
    else:
        await update.message.reply_text("Jogador da FURIA não encontrado, tente novamente.")