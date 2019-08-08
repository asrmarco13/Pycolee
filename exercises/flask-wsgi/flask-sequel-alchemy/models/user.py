from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # SELECT * FROM users WHERE username=username LIMIT 1
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # SELECT * FROM users WHERE id=_id LIMIT 1
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
