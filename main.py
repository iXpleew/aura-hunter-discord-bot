import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import collector

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class AuraBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.add_cog(collector.Collector(self))


bot = AuraBot(command_prefix="!", intents=intents)
bot.run(token, log_handler=handler, log_level=logging.INFO)