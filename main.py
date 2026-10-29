from email import message

import discord
from discord.ext import commands
from discord.abc import User
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Jestem łowcą aury jakby co')
    print(bot.user.name)
    print(bot.user.id)


def mention_ssjmonster(msg: message, ssj_nick: str = "monster133") -> str:
    return f"<@{msg.guild.get_member_named(ssj_nick).id}>"


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await message.channel.send(message.content)
        return
    if "stas" in message.content.lower():
        await message.channel.send(f"{mention_ssjmonster(message)} +10 aury za popularność")
    await bot.process_commands(message)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)