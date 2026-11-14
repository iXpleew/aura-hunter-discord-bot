import discord
from discord.ext import commands


class Collector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"I'm working {self.bot.user}")


    async def searching_channel_history(self, channel: discord.TextChannel):
        messages_history = [message async for message in channel.history(limit=1000)
                            if message.author != self.bot.user and
                            not message.author.bot  and
                            len(message.content) > 10]

        for message in messages_history:
            print(f"{message.author} - {message.content} - {message.channel}")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        await self.searching_channel_history(message.channel)
