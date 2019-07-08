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
       host=host,
       port=port,
       username=username,
       password=password)
print('...successful connection')

# getting database
db = client.people_database

# getting a collection
people_collection = db.people

# find Mario
person = people_collection.find_one({'name': 'Mario'})

# update Mario age
people_collection.update_one({'name': 'Mario'},
                             {'$set': {'age': 70}})
# print new Mario age
person = people_collection.find_one({'name': 'Mario'})
print(person)
