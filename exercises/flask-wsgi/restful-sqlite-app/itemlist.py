from flask_restful import Resource


items = []


class ItemList(Resource):
    def get(self):
        return {'items': items}
