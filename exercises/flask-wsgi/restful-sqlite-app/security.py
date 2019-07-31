from user import User
from werkzeug.security import safe_str_cmp
# from flask_restful import reqparse


def authenticate(username, password):
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
    data = parser.parse_args()
    user = username_mapping.get(data['username'], None)
    """
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
