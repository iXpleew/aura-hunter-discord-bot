import sqlite3


def manual_aura_classifier():
    connection = sqlite3.connect("data/discord_data.sqlite")
    cursor = connection.cursor()
    messages_list = cursor.execute("""
                   SELECT * FROM DISCORD_MESSAGES
                   order by random()
                   LIMIT 5;""")
    for message in messages_list:
        print(message)

if __name__ == "__main__":
    manual_aura_classifier()