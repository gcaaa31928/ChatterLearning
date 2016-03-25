from chatter_learning.store_adapters import BaseStore
from pymongo import MongoClient
import json
class Mongodb(BaseStore):

    def __init__(self, **kwargs):
        self.database_url = kwargs.get('database_url', 'mongodb://localhost:/27017')
        self.database_name = kwargs.get('database_name', 'chatterLearning')
        self.client = MongoClient(self.database_url)
        self.database = self.client[self.database_name]

    def get(self, key):
        data = self.database.find_one({'key': key})
        if not data:
            return None
        values = json.loads(data)
        return values

    def put(self, key, values):
        data = json.dumps(values)
        self.database.replace_one({'key', key}, data)
