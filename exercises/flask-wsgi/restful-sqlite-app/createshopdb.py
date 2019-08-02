import sqlite3


connection = sqlite3.connect('shop.db')
cursor = connection.cursor()

create_users_table = '''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY,
                      username text NOT NULL,
                      password text NOT NULL)'''

cursor.execute(create_users_table)

create_items_table = ''' CREATE TABLE IF NOT EXISTS items
                     (name text NOT NULL,
                      price real NOT NULL)'''

cursor.execute(create_items_table)

connection.commit()
connection.close()
