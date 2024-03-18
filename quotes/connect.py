import configparser
from bson import ObjectId
from pymongo import MongoClient
from pathlib import Path
from django.conf import settings
import json
import psycopg2

filename = Path(settings.BASE_DIR, 'config.ini')
config = configparser.ConfigParser()
config.read(filename)

user = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')

def get_mongodb():
    client = MongoClient(f'mongodb+srv://{user}:{password}@cluster0.j1fuex0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client.hw
    return db




# with open("quotes.json", 'r', encoding='utf-8') as fd:
#     quotes = json.load(fd)
#
# for quote in quotes:
#     author = db.authors.find_one({'fullname': quote['author']})
#     if author:
#         db.quotes.insert_one({
#             'quote': quote['quote'],
#             'tags': quote['tags'],
#             'author': ObjectId(author['_id'])
#         })

