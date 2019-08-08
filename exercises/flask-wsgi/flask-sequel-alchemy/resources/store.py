from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()

        return {'message': 'Store {} not found'.format(name)}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store {} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception:
            return {'message': 'An error occured while creating {}'.format(name)}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_to_db()
            except Exception:
                return {'message': 'An error occured while deleting {}'.format(name)}, 500

            return {'message': 'Store {} deleted'.format(name)}

        return {'message': 'Store {} not exists'.format(name)}, 404
