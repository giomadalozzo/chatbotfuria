import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from utils.logger import logger
from config import Config
from handlers import get_handlers

async def post_init(application):
    """Post-initialization tasks"""
    logger.info("Bot initialized successfully")

def setup_application() -> ApplicationBuilder:
    """Configure the application with proper dependency injection"""
    return ApplicationBuilder() \
        .token(Config.TOKEN) \
        .post_init(post_init) \
        .concurrent_updates(True) \
        .build()

def main() -> None:
    """Entry point for the bot application"""
    try:
        app = setup_application()
        
        # Registering all handlers
        for handler in get_handlers():
            app.add_handler(handler)

        logger.info("Starting bot in polling mode")
        app.run_polling()

    except Exception as e:
        logger.critical("Failed to start bot: %s", e, exc_info=True)
        raise

if __name__ == "__main__":
    main()
