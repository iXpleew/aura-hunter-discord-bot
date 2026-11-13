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

@bot.event
async def on_ready():
    print('Jestem łowcą aury jakby co')
    print(bot.user.name)
    print(bot.user.id)


def mention_ssjmonster(msg: discord.Message, ssj_nick: str = "monster133") -> str:
    return f"<@{msg.guild.get_member_named(ssj_nick).id}>"


async def searching_channel_history(channel: discord.TextChannel):
    async for message in channel.history(limit=10):
        await channel.send(f"{message.author.name} wysłał wiadomość {message.content} -> XD")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "Kogo kochamy najbardziej?":
        await message.channel.send("Igoreka <333")
    # await searching_channel_history(message.channel)
    await bot.process_commands(message)



bot.run(token, log_handler=handler, log_level=logging.DEBUG)