import threading

from flask import jsonify
from pymongo import MongoClient

from repositories.GameRepositoryInterface import GameRepositoryInterface


def db_factory():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['RatGame']
    return db


class MongoDbGameRepository(GameRepositoryInterface):
    __instance = None
    __instance_lock = threading.Lock()
    __data_lock = threading.Lock()
    __house_id_counter = 1
    def __init__(self):
        if MongoDbGameRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.db = db_factory()
            self.collection = self.db['Games']
            MongoDbGameRepository.__instance = self

    @staticmethod
    def get_instance():
        with MongoDbGameRepository.__instance_lock:
            if MongoDbGameRepository.__instance is None:
                MongoDbGameRepository()
            return MongoDbGameRepository.__instance

    def save(self, game_dict):

        game_dict["game_id"] = MongoDbGameRepository.__house_id_counter
        MongoDbGameRepository.__house_id_counter += 1

        result = self.collection.insert_one(game_dict)

        return result.inserted_id

    def find_game_by_id(self, game_id):
        data = self.collection.find_one({'_id': game_id})
        if data is not None:
            return self._destructured(data)
        else:
            return 'Game not found', 404

    def _destructured(self, data):
        house_dict = {}
        i, *keys_list = data.keys()
        j, *values_list = data.values()
        house_dict[i] = str(j)
        for i in range(len(keys_list)):
            house_dict[keys_list[i]] = values_list[i]


        return house_dict

