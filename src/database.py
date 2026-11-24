import sqlite3
from message_class import Message
from datetime import datetime

DATABASE_PATH : str = '../data/discord_data.sqlite'


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


def insert_message(m_id: int, m_content: str, m_time: str, m_user_id: int, m_channel_id: int, m_response_id: str) -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    PRAGMA foreign_keys = ON;""")
    cursor.execute("""
    INSERT INTO DISCORD_MESSAGES (message_id, content, time_sent, user_id, channel_id, response_to)
    VALUES(?,?,?,?,?,?)
    ON CONFLICT(message_id)
    DO UPDATE SET content = excluded.content, time_sent = excluded.time_sent, user_id = excluded.user_id, channel_id = excluded.channel_id, response_to = excluded.response_to;""",
                   (m_id, m_content, m_time, m_user_id, m_channel_id, m_response_id))

    connection.commit()
    connection.close()


def get_username_by_id(user_id: int) -> str:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    name = cursor.execute("""
    SELECT user_name FROM DISCORD_USERS WHERE user_id = ?""", (user_id,)).fetchone()[0]
    connection.close()
    return name




def insert_aura_messages(messages_with_aura: dict):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    PRAGMA foreign_keys = ON;""")
    for message_id, aura_classification in messages_with_aura.items():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO DISCORD_MESSAGES_AURA (message_id, aura_points, who_evaluated, date)
        VALUES(?,?,?,?); """, (message_id, aura_classification, "human", datetime.now().replace(microsecond=0, tzinfo=None)))
        connection.commit()

    connection.close()

        


def get_messages_for_manual_classification():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    message_list = list(cursor.execute("""
                    SELECT mes.* FROM DISCORD_MESSAGES mes
                    LEFT JOIN DISCORD_MESSAGES_AURA aur ON mes.message_id = aur.message_id
                    where aur.message_id is NULL
                    ORDER BY random()
                    limit 5;"""))

    connection.close()
    message_objects = []
    for message in message_list:
        mes_id, mes_content, mes_time_sent, mes_user_id, mes_channel_id, mes_response_id = message
        new_message_obj = Message(mes_id, mes_content, datetime.fromisoformat(mes_time_sent).replace(microsecond=0, tzinfo=None), mes_user_id, mes_channel_id, mes_response_id)
        message_objects.append(new_message_obj)

    return message_objects