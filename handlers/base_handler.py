from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes

class BaseHandler(ABC):
    """Abstract class for all handlers"""
    
    @abstractmethod
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Método principal que processa a atualização"""
        pass
