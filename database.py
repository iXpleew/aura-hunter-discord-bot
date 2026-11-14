import sqlite3


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


def insert_channels(channels: list[tuple[int,str]]) -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    PRAGMA foreign_keys = ON;""")

    for channel in channels:
        channel_id, channel_name = channel
        cursor.execute("""
        INSERT INTO DISCORD_CHANNELS (channel_id, channel_name)
        VALUES(?,?)
        ON CONFLICT(channel_id)
        DO UPDATE SET channel_name = excluded.channel_name;""", (channel_id, channel_name))

    connection.commit()
    connection.close()

def insert_roles(roles: list[tuple[int, str]]) -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    PRAGMA foreign_keys = ON;""")

    for role in roles:
        role_id, role_name = role
        cursor.execute("""
        INSERT INTO DISCORD_ROLES (role_id, role_name)
        VALUES(?,?)
        ON CONFLICT(role_id)
        DO UPDATE SET role_name = excluded.role_name;""", (role_id, role_name))

    connection.commit()
    connection.close()
