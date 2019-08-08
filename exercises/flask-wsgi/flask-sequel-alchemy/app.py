from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.itemlist import ItemList
from resources.userregister import UserRegister
from resources.item import Item
from resources.store import Store
from resources.storelist import StoreList
from security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'marco'
api = Api(app)
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run('localhost', 8080, True)
