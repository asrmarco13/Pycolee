from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'marco'
api = Api(app)
# JWT creates url /auth for us
jwt = JWT(app, authenticate, identity)
items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank')

    @jwt_required()
    def get(self, name):
        """
        for item in items:
            if item['name'] == name:
                return item
        """
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is not None:
            return {'message': 'Item {} exists.'.format(name)}, 400

        request_data = Item.parser.parse_args()
        item = {
            'name': name,
            'price': request_data['price']
        }
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {'message': 'Item {} deleted.'.format(name)}

    def put(self, name):
        request_data = Item.parser.parse_args()
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is None:
            item = {
                'name': name,
                'price': request_data['price']
            }
            items.append(item)
        else:
            item.update(request_data)

        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=8080, debug=True)
