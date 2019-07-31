import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank')

    @jwt_required()
    def get(self, name):
        item = self.find_item_by_name(name)
        if item:
            return {'item': item}, 200

        return {'message': 'Item {} not exists'.format(name)}, 404

    def post(self, name):
        item = self.find_item_by_name(name)
        if item:
            return {'message': 'Item {} exists.'.format(name)}, 400

        request_data = self.parser.parse_args()
        item = {
            'name': name,
            'price': request_data['price']
        }
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()
        query_insert = '''INSERT INTO items
                        VALUES (?, ?)'''
        cursor.execute(query_insert, (item['name'],
                                      item['price']))
        connection.commit()
        connection.close()
        return item, 201

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items where name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            item = {
                'name': row[0],
                'price': row[1]
            }
            return item

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
