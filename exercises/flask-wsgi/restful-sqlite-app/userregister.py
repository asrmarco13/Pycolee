import sqlite3
from user import User
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank')

    def post(self):
        data = self.parser.parse_args()
        username = data['username']
        password = data['password']
        # verify if username exists
        user = User.find_by_username(username)
        if user:
            return {"message": "User already exists"}, 400

        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()

        try:
            insert_user_query = 'INSERT INTO users values(NULL, ?, ?)'
            cursor.execute(insert_user_query, (username, password))
            connection.commit()
            connection.close()
            return {"message": "User created successfully"}, 201
        except Exception as ex:
            return {"message":
                    "An error occured during user registration %s"
                    % ex}, 500
