import sqlite3


connection = sqlite3.connect('shop.db')
cursor = connection.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY,
               username text NOT NULL,
               password text NOT NULL)'''
cursor.execute(create_table)

username = 'marco'
password = 'asdf'

insert_user = '''INSERT INTO users
               VALUES (NULL, ?, ?)'''
cursor.execute(insert_user, (username, password))

connection.commit()
connection.close()
