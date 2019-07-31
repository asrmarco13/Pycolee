from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from userregister import UserRegister
from item import Item
from itemlist import ItemList


app = Flask(__name__)
app.secret_key = 'marco'
api = Api(app)
# JWT creates url /auth for us
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
