from telegram.ext import CommandHandler, MessageHandler, filters
from .start import StartHandler
from .help import HelpHandler
from .stats import StatsHandler
from .achievements import AchievementsHandler
from .error import ErrorHandler
from .matches import MatchesHandler
from .molodoy import MolodoyHandler
from .orgstats import OrgStatsHandler
from .socialmedia import SocialMediaHandler
from .streams import StreamsHandler
from .yekindar import YekindarHandler

def get_handlers():
    """Factory for all handlers"""
    return [
        CommandHandler("start", StartHandler().handle),
        CommandHandler("ajuda", HelpHandler().handle),
        CommandHandler("stats", StatsHandler().handle),
        CommandHandler("titulos", AchievementsHandler().handle),
        CommandHandler("proximosjogos", MatchesHandler().handle),
        CommandHandler("molodoy", MolodoyHandler().handle),
        CommandHandler("orgstats", OrgStatsHandler().handle),
        CommandHandler("midia", SocialMediaHandler().handle),
        CommandHandler("streams", StreamsHandler().handle),
        CommandHandler("yekindar", YekindarHandler().handle),
        MessageHandler(filters.COMMAND, ErrorHandler().handle)
    ]
