import threading

from flask import jsonify
from pymongo import MongoClient

from repositories.HouseRepositoryInterface import HouseRepositoryInterface


def db_factory():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['House']
    return db


class MongoDbHouseRepository(HouseRepositoryInterface):
    __instance = None
    __instance_lock = threading.Lock()
    __data_lock = threading.Lock()

    def __init__(self):
        if MongoDbHouseRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.db = db_factory()
            self.collection = self.db['houses']
            MongoDbHouseRepository.__instance = self

    @staticmethod
    def get_instance():
        with MongoDbHouseRepository.__instance_lock:
            if MongoDbHouseRepository.__instance is None:
                MongoDbHouseRepository()
            return MongoDbHouseRepository.__instance

    def save(self, house_dict):
        result = self.collection.insert_one(house_dict)
        print(result.inserted_id)
        return result.inserted_id

    def find_house_by_id(self, house_id):
        data = self.collection.find_one({'_id': house_id})
        if data is not None:
            return self._destructured(data)
        else:
            return 'Game not found', 404

    def _destructured(self, data):
        pass
