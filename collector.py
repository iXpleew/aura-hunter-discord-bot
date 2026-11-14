import discord
import database
from discord.ext import commands


class Collector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_members = []

    def import_members(self):
        self.server_members = [(member.id, member.name) for member in self.bot.get_all_members()]
        database.insert_users(self.server_members)


    def insert_channels(self):
        server_channels = [(channel.id, channel.name) for channel in self.bot.get_all_channels()]
        database.insert_channels(server_channels)


    def insert_roles(self):
        print("adding roles")
        current_server = self.bot.get_guild(900807035971592194)
        server_roles = [(role.id, role.name) for role in current_server.roles]
        print("added roles")
        database.insert_roles(server_roles)


    @commands.Cog.listener()
    async def on_ready(self):
        #client = discord.Client()
        channel = discord.utils.get(self.bot.get_all_channels(), id=900807036466507789)
        self.import_members()
        self.insert_channels()
        self.insert_roles()
        print(f"I'm working {self.bot.user}")


    async def searching_channel_history(self, channel: discord.TextChannel):
        messages_history = [message async for message in channel.history(limit=10000)
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
