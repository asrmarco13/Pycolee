from flask import Flask, jsonify, request


app = Flask(__name__)
stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')  # '/' means home page of application http://www.example.com/
def home():
    return 'Hello world!'


# POST /store data: name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')  # http://127.0.0.1/store/some_name
def get_store(name):
    """
    Iterate over stores
    If the store name matches, return it
    If none match, return error message
    """
    for store in stores:
        store_name = store['name']
        if (store_name == name):
            return jsonify(store)

    return jsonify({'message': 'No store matches'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        store_name = store['name']
        if (store_name == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)

    return jsonify({'message': 'No store matches'})


# GET /store/<string:name>/item
def get_items_in_store(name):
    for store in stores:
        store_name = store['name']
        if store_name == name:
            return jsonify({'items': store['items']})

    return jsonify({'message': 'no store found'})


app.run(port=8080)
