import discord
import database
from discord.ext import commands


class Collector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_members = []

    def import_members(self):
        self.server_members = self.server_members = [(member.id, member.name) for member in self.bot.get_all_members()]


    def insert_users_to_database(self):
        database.insert_users(self.server_members)


    @commands.Cog.listener()
    async def on_ready(self):
        self.import_members()
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
        # await self.searching_channel_history(message.channel)
