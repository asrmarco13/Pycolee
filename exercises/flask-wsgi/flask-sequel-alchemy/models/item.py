from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        item = {
            'name': self.name,
            'price': self.price
        }
        return item

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_item_by_name(cls, name):
        # SELECT * FROM items where name=name LIMIT 1
        return cls.query.filter_by(name=name).first()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all_items(cls):
        # SELECT * FROM items
        return cls.query.all()
