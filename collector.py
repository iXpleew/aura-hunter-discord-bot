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


    def insert_messages(self, messages_list: list):
        for m_id, m_content, m_datetime, m_author_id, m_channel_id, m_ref_message_id in messages_list:
            database.insert_message(m_id, m_content, m_datetime, m_author_id, m_channel_id, m_ref_message_id)


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"I'm working {self.bot.user}")


    async def create_channel_history_list(self, channel: discord.TextChannel, list_limit:int) -> list:
        messages_history = [(message.id, message.content, message.created_at, message.author.id, message.channel.id, message.reference.message_id)
                            async for message in channel.history(limit=list_limit)
                            if message.author != self.bot.user and
                            not message.author.bot]
        return messages_history



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        main_channel = message.channel

        await self.inserting_channel_history(message.channel)
