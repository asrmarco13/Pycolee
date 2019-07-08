import pymongo
from pymongo import MongoClient

# connect to mongodb
print('Connect to Database, insert credentials...')
username = input('Insert username: ')
password = input('Insert password: ')
host = input('Insert host: ')
port = input('Insert host port: ')
port = int(port)
client = MongoClient(
       host=host, port=port,
       username=username, password=password)
print('...successful connection')

# getting database
db = client.people_database

# getting a collection
people_collection = db.people

# create index
people_collection.create_index([('name', pymongo.ASCENDING)])
people_collection.create_index([('surname', pymongo.ASCENDING)])
people_collection.create_index([('computer', pymongo.ASCENDING)])

# insert a document
people1 = {
    'name': 'Marco',
    'surname': 'Orfei',
    'age': 31,
    'computer': [
        'Apple',
        'Lenovo'
    ]
}

people_collection.insert_one(people1)

# insert another document
people2 = {
    'name': 'Mario',
    'surname': 'Rossi',
    'age': 50,
    'computer': [
        'Lenovo'
    ]
}

people_collection.insert_one(people2)
