from flask_restful import Resource
from models.item import ItemModel


class ItemList(Resource):
    def get(self):
        items = ItemModel.find_all_items()
        return {'items': [item.json() for item in items]}
