from user import User
from werkzeug.security import safe_str_cmp
# from flask_restful import reqparse


users = [User(1, 'marco', 'asdf')]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


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
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
