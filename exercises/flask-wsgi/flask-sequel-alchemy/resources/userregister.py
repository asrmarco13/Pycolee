from models.user import UserModel
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
        # verify if username exists
        user = UserModel.find_by_username(username)
        if user:
            return {"message": "User already exists"}, 400

        user = UserModel(**data)

        try:
            # INSERT INTO users values(NULL, ?, ?)
            user.save_to_db()
            return {"message": "User created successfully"}, 201
        except Exception as ex:
            return {"message":
                    "An error occured during user registration %s"
                    % ex}, 500
