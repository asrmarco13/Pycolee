import sqlite3
from flask_restful import Resource


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        result = cursor.execute(query)
        rows = result.fetchall()
        connection.close()

        items = []
        for row in rows:
            item = {
                'name': row[0],
                'price': row[1]
            }
            items.append(item)

        return {'items': items}
