from telegram import Update
from telegram.ext import ContextTypes

async def achievements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            """*🏆 Histórico de Títulos da FURIA (CS:GO/CS2)*

                1st - Elisa Masters Espoo 2023  
                1st - BGS Esports 2023  
                1st - BLAST\u200B.tv Paris Major 2023: American RMR  
                1st - PGL Major Antwerp 2022: American RMR  
                1st - Intel Extreme Masters XVI - Fall: North America  
                1st - Regional Major Rankings 2021: North America  
                1st - Elisa Invitational Summer 2021  
                1st - Intel Extreme Masters XV - New York Online: North America  
                1st - ESL Pro League Season 12: North America  
                1st - DreamHack Open Summer 2020: North America  
                1st - DreamHack Masters Spring 2020: North America  
                1st - ESL Pro League Season 12: North American Qualifier  
                1st - Arctic Invitational 2019  
                1st - EMG CS:GO World Invitational 2019  
                1st - ESEA Season 31: Global Challenge  
                1st - ESEA Season 31: Premier Division - North America Final  
                1st - ESL One: Cologne 2019 - North American Qualifier  
                1st - Esports Championship Series Season 7 - North America: Series 3  
                1st - ESEA Season 30: Premier Division - North America  
                1st - DreamHack Masters Dallas 2019: North American Qualifier  
                1st - EPICENTER 2018 - Wild Card Americas Qualifier - Open Qualifier #1  
                1st - ESL Brasil Premier League Season 6  
                1st - Gamers Club Liga Profissional: May 2018  
                1st - Americas Minor Championship - London 2018: SA Open Qualifier #2  
                1st - Aorus League - Invitational  
                1st - GG\u200B.BET Ascensão  
                1st - Gamers Club Liga Profissional: April 2018  
                1st - Aorus League - Brazil: Finals 2021  
                1st - PGL Major Copenhagen 2024: American RMR  
                1st - BLAST Premier: Fall 2020 Showdown  
                1st - DreamHack Masters Spring 2020: North America  
                1st - ESEA Season 31: Premier Division - North America  
                1st - ESL One: Cologne 2019: North American Open Qualifier #2  
                1st - ESEA Season 29: Premier Relegation - North America  
                1st - Americas Minor Championship - Katowice 2019: North American Open Qualifier #2  
                1st - ZOTAC Cup Masters 2018 - Americas: South America  
                1st - ESL LA League Season 1  
                1st - ESL Brasil Premier League Season 5 - Qualifier #2  
                1st - Americas Minor Championship - Rio 2020: North American Closed Qualifier  
                1st - Americas Minor Championship - Katowice 2019: North American Closed Qualifier  
                1st - DreamHack Open Atlanta 2018: North American Open Qualifier  
                1st - ESL LA League Season 1: Closed Qualifier
            """,
        parse_mode="Markdown"
    )