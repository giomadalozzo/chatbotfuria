from telegram import Update
from telegram.ext import ContextTypes

async def yekindar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_photo(photo='https://img-cdn.hltv.org/playerbodyshot/rRclDPBXIMxFv2fv0dV0J0.png?ixlib=java-2.1.0&w=400&s=2b0f6209ca40efa081852b9d1d8e01c1', caption="Novo reforço da FURIA, YEKINDAR.")
    await update.message.reply_text(
            "**Mareks \"YEKINDAR\" Gaļinskis**  🇱🇻\n\n"
            "Anunciado como stand-in para o restante da temporada, YEKINDAR chega na FURIA para substituir Felipe \"skullz\" Medeiros, que foi movido para o banco. "
            "YEKINDAR, jogador letão de 25 anos, é conhecido por seu estilo agressivo e versatilidade tática, destacando-se como entry-fragger em equipes como Virtus[.]Pro e Team Liquid. Sua chegada à FURIA representa um passo significativo na internacionalização do elenco, que agora conta com jogadores do Brasil, Cazaquistão e Letônia, e terá que adotar o inglês como idioma principal de comunicação. "
            "O CEO da FURIA, Jaime Pádua, [comentou sobre a contratação](https://x.com/jaimepadua/status/1914794199918039232): \"A chegada do YEKINDAR traz a agressividade que precisamos, com experiência, voz ativa e a enorme possibilidade de facilitar a adaptação do nosso querido molodoy ao elenco\".\n\n",
        parse_mode="Markdown"
    )