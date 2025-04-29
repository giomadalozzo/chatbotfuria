from telegram import Update
from telegram.ext import ContextTypes

async def molodoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_photo(photo='https://img-cdn.hltv.org/playerbodyshot/qNyAd_xVHTTmbCAKPx-jPk.png?ixlib=java-2.1.0&w=400&s=b128ede878e462107c70590202b14139', caption="Jogador Molodoy, novo AWP da FURIA.")
    await update.message.reply_text(
            "**Danil \"Molodoy\" Golubenko** 🇰🇿\n\n"
            "Com a saída de Marcelo \"chelo\" Cespedes, a FURIA inicia o processo de internacionalização da lineup de CS com a adição do jovem talento "
            "Danil \"Molodoy\" Golubenko. Molodoy atuava pela equipe AMKAL Esports e é conhecido por seu estilo agressivo e mira precisa. Danil entra para a FURIA para assumir o papel de AWP do time, deixando FalleN com a função de IGL. "
            "Com essa nova adição, a FURIA visa alcançar melhores resultados nos próximos torneios e consolidar-se como uma das principais equipes do cenário competitivo. "
            "\n\nPara saber mais, veja o [vídeo publicado pelo FalleN](https://x.com/FURIA/status/1915134729357054290) sobre a nova contratação.\n\n",
        parse_mode="Markdown"
    )