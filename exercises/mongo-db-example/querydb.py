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

# find a person
person = people_collection.find_one()
print(person)

# find a person with apple pc
apple_person = people_collection.find_one({'computer': 'Apple'})
print(apple_person)

# find a person with surname greater then
person = people_collection.find_one({'surname': {'$gt': 'Orfei'}})
print(person)
