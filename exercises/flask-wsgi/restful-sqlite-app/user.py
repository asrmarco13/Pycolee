import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()

        find_user_by_username = '''SELECT *
                                FROM users
                                WHERE username=?'''

        result = cursor.execute(find_user_by_username,
                                (username,))
        row = result.fetchone()
        connection.close()
        user = None
        if row:
            user = cls(*row)

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()

        find_user_by_id = '''SELECT *
                                FROM users
                                WHERE id=?'''

        result = cursor.execute(find_user_by_id,
                                (_id,))
        row = result.fetchone()
        connection.close()
        user = None
        if row:
            user = cls(*row)

        return user
