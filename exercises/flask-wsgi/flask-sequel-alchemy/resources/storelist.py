from flask_restful import Resource
from models.store import StoreModel


class StoreList(Resource):
    def get(self):
        stores = StoreModel.find_all_stores()
        return {'stores': [store.json() for store in stores]}
