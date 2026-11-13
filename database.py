import _sqlite3

def insert_messages():
    connection = _sqlite3.connect("data/discord_data.sqlite")
    cursor = connection.cursor()
