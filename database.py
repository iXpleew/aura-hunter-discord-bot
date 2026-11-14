import sqlite3
import discord


DATABASE_PATH : str = 'data/discord_data.sqlite'


def insert_users(users: list[tuple[int, str]]) -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    PRAGMA foreign_keys = ON;""")

    for member in users:
        member_id, member_name = member

        cursor.execute("""
        INSERT INTO DISCORD_USERS (user_id, user_name)
        VALUES (?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET user_name = excluded.user_name;""", (member_id, member_name))

    connection.commit()
    connection.close()


def insert_messages(messages: list[discord.Message]):
    pass