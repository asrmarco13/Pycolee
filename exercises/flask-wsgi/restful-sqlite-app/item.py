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
            return item

        return {'message': 'Item {} not exists'.format(name)}, 404

    def post(self, name):
        request_data = self.parser.parse_args()
        if self.find_item_by_name(name):
            return {'message': 'Item {} exists.'.format(name)}, 400

        item = {
            'name': name,
            'price': request_data['price']
        }

        try:
            self.insert_item(item)
        except Exception:
            return {'message': 'An error occured inserting the item'}, 500

        return item, 201

    @classmethod
    def insert_item(cls, item):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()
        query_insert = '''INSERT INTO items
                        VALUES (?, ?)'''
        cursor.execute(query_insert, (item['name'],
                                      item['price']))
        connection.commit()
        connection.close()

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
        item = self.find_item_by_name(name)
        if item:
            connection = sqlite3.connect('shop.db')
            cursor = connection.cursor()

            query_delete_item = '''DELETE FROM items where name=?'''
            cursor.execute(query_delete_item, (item['name'],))
            connection.commit()
            connection.close()

            return {'message': 'Item {} deleted.'.format(name)}

        return {'message': 'Item {} not exists'.format(name)}, 404

    def put(self, name):
        request_data = self.parser.parse_args()
        item = self.find_item_by_name(name)
        updated_item = {
            'name': name,
            'price': request_data['price']
        }

        if item:
            try:
                self.update_item(updated_item)
            except Exception:
                return {'message': 'An error occured inserting the item'}, 500

            return updated_item

        try:
            self.insert_item(updated_item)
        except Exception:
            return {'message': 'An error occured inserting the item'}, 500

        return updated_item, 201

    @classmethod
    def update_item(cls, item):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()
        query_update = '''UPDATE items
                        SET price = ?
                        WHERE name = ?'''
        cursor.execute(query_update, (item['price'], item['name']))
        connection.commit()
        connection.close()
