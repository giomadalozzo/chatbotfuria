from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

from handlers.achievements import achievements
from handlers.help import help
from handlers.matches import matches
from handlers.molodoy import molodoy
from handlers.start import start
from handlers.socialmedia import social_media
from handlers.stats import stats
from handlers.streams import streams
from handlers.yekindar import yekindar
from handlers.orgstats import org_stats
from handlers.error import error

TOKEN='8034112887:AAFeaQTIda6_Oml48ripJ2YYqwaUjXBY8Gs'

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("titulos", achievements))
    app.add_handler(CommandHandler("ajuda", help))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("partidas", matches))
    app.add_handler(CommandHandler("molodoy", molodoy))
    app.add_handler(CommandHandler("midia", social_media))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("streams", streams))
    app.add_handler(CommandHandler("orgstats", org_stats))
    app.add_handler(CommandHandler("yekindar", yekindar))

    app.add_handler(MessageHandler(filters.COMMAND, error))

    print("ESTOU RODANDO")
    app.run_polling()

if __name__ == "__main__":
    main()