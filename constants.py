class Messages:
    """Messages used by the bot"""
    
    # Welcome message
    WELCOME = """**BEM-VINDO AO FURIOSO BOT! 🐾**

Sou seu assistente oficial da FURIA no CS!
Use os comandos abaixo para saber mais:
/molodoy - Saiba mais sobre a chegada do novo AWP da FURIA
/yekindar - Saiba mais sobre a nova adição do time
/orgstats - Veja as estatísticas do time da FURIA
/proximosjogos - Agenda dos próximos jogos
/stats [jogador] - Veja as estatísticas dos jogadores do nossa lineup
/streams - Link da Twitch dos nossos jogadores
/titulos - Histórico de títulos da FURIA
/midia - Links das nossas redes sociais
/ajuda - Ver comandos disponíveis"""

    HELP = """**📌 COMANDOS DISPONÍVEIS**

🔹 /start - Mensagem de boas-vindas
🔹 /ajuda - Mostra esta mensagem de ajuda
🔹 /titulos - Histórico de títulos da FURIA
🔹 /proximosjogos - Próximas partidas agendadas
🔹 /stats [jogador] - Estatísticas de um jogador
🔹 /molodoy - Info sobre o novo AWP
🔹 /yekindar - Info sobre o novo jogador
🔹 /midia - Links das redes sociais
🔹 /streams - Links das streams dos jogadores
🔹 /orgstats - Estatísticas da organização"""

    # Error message
    ERROR = "❌ Comando não reconhecido. Use /ajuda para ver os comandos disponíveis."
    ERROR_GENERIC = "⚠️ Ocorreu um erro inesperado. Por favor, tente novamente mais tarde."

    # Messages about players
    MOLODOY_INFO = """**🎯 Danil "Molodoy" Golubenko** 🇰🇿

📅 **Idade:** 20 anos  
🖱️ **Função:** AWP  
🌎 **Nacionalidade:** Cazaquistão  
📊 **Rating HLTV:** 1.24 

💡 **Sobre:**  
Com a saída de Marcelo \"chelo\" Cespedes, a FURIA inicia o processo de internacionalização da lineup de CS com a adição do jovem talento
Danil \"Molodoy\" Golubenko. Molodoy atuava pela equipe AMKAL Esports e é conhecido por seu estilo agressivo e mira precisa. Danil entra para a FURIA para assumir o papel de AWP do time, deixando FalleN com a função de IGL.
Com essa nova adição, a FURIA visa alcançar melhores resultados nos próximos torneios e consolidar-se como uma das principais equipes do cenário competitivo. 
\n\nPara saber mais, veja o [vídeo publicado pelo FalleN](https://x.com/FURIA/status/1915134729357054290) sobre a nova contratação.\n

🔗 **Links:**  
[HLTV](https://www.hltv.org/stats/players/24144/molodoy) | [Twitch](https://twitch.tv/molodoy1818)"""

    YEKINDAR_INFO = """**🔥 Mareks "YEKINDAR" Gaļinskis** 🇱🇻

📅 **Idade:** 25 anos  
🖱️ **Função:** Entry Fragger  
🌎 **Nacionalidade:** Letônia  
📊 **Rating HLTV:** 1.13 

💡 **Sobre:**  
Anunciado como stand-in para o restante da temporada, YEKINDAR chega na FURIA para substituir Felipe \"skullz\" Medeiros, que foi movido para o banco. 
YEKINDAR, jogador letão de 25 anos, é conhecido por seu estilo agressivo e versatilidade tática, destacando-se como entry-fragger em equipes como Virtus[.]Pro e Team Liquid. Sua chegada à FURIA representa um passo significativo na internacionalização do elenco, que agora conta com jogadores do Brasil, Cazaquistão e Letônia, e terá que adotar o inglês como idioma principal de comunicação.
O CEO da FURIA, Jaime Pádua, [comentou sobre a contratação](https://x.com/jaimepadua/status/1914794199918039232): \"A chegada do YEKINDAR traz a agressividade que precisamos, com experiência, voz ativa e a enorme possibilidade de facilitar a adaptação do nosso querido molodoy ao elenco\".\n

🔗 **Links:**  
[HLTV](https://www.hltv.org/stats/players/13915/yekindar) | [Twitch](https://twitch.tv/yekindar)"""

    # Menssages about stats and info
    SOCIAL_MEDIA = """**🌐 REDES SOCIAIS OFICIAIS**

🔹 [Twitter](https://twitter.com/FURIA)  
🔹 [Instagram](https://instagram.com/furiagg)  
🔹 [Facebook](https://facebook.com/furiagg)  
🔹 [YouTube](https://youtube.com/@FURIAgg)  
🔹 [TikTok](https://tiktok.com/@furia)  
🔹 [Site Oficial](https://furia.gg)"""

    STREAMS = """**🎥 STREAMS DOS JOGADORES**

🔴 [FalleN](https://twitch.tv/gafallen)  
🔴 [YEKINDAR](https://twitch.tv/yekindar)  
🔴 [KSCERATO](https://twitch.tv/kscerato)  
🔴 [yuurih](https://twitch.tv/yuurih)  
🔴 [Molodoy](https://twitch.tv/molodoy1818)"""


class URLs:
    """All URLs used by the bot"""
    
    HLTV_BASE = "https://www.hltv.org"
    FURIA_TEAM = f"{HLTV_BASE}/team/8297/furia"
    FURIA_MATCHES = f"{FURIA_TEAM}#tab-matchesBox"
    
    # URLs Players
    PLAYER_STATS = {
        "fallen": f"{HLTV_BASE}/stats/players/2023/fallen",
        "yekindar": f"{HLTV_BASE}/stats/players/13915/yekindar",
        "molodoy": f"{HLTV_BASE}/stats/players/24144/molodoy",
        "yuurih": f"{HLTV_BASE}/stats/players/12553/yuurih",
        "kscerato": f"{HLTV_BASE}/stats/players/15631/kscerato"
    }
    
    # URLs images
    PLAYER_IMAGES = {
        "yekindar": "https://img-cdn.hltv.org/playerbodyshot/rRclDPBXIMxFv2fv0dV0J0.png?ixlib=java-2.1.0&w=400&s=2b0f6209ca40efa081852b9d1d8e01c1",
        "molodoy": "https://img-cdn.hltv.org/playerbodyshot/qNyAd_xVHTTmbCAKPx-jPk.png?ixlib=java-2.1.0&w=400&s=b128ede878e462107c70590202b14139"
    }
