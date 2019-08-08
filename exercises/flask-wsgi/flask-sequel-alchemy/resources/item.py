from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item {} not exists'.format(name)}, 404

    def post(self, name):
        request_data = self.parser.parse_args()
        print(ItemModel.find_item_by_name(name))
        if ItemModel.find_item_by_name(name):
            return {'message': 'Item {} exists.'.format(name)}, 400

        item = ItemModel(name, **request_data)

        try:
            item.save_to_db()
        except Exception:
            return {'message': 'An error occured inserting the item'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_to_db()

            return {'message': 'Item {} deleted.'.format(name)}

        return {'message': 'Item {} not exists'.format(name)}, 404

    def put(self, name):
        request_data = self.parser.parse_args()
        item = ItemModel.find_item_by_name(name)

        if item:
            try:
                item.price = request_data['price']
            except Exception:
                return {'message': 'An error occured updating the item'}, 500
        else:
            try:
                item = ItemModel(name, **request_data)
            except Exception:
                return {'message': 'An error occured inserting the item'}, 500

        item.save_to_db()
        return item.json(), 201
