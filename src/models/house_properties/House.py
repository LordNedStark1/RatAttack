from flask import json


class House:
    def __init__(self):
        self._house_id = ""
        self._house_name = ""
        self._player = None
        self._total_number_of_rooms = 6
        self._rooms = []

    def set_house_id(self, house_id):
        self._house_id = house_id

    def get_house_id(self):
        return self._house_id

    def set_house_name(self, house_name):
        self._house_name = house_name

    def get_house_name(self):
        return self._house_name

    def set_player(self, player):
        self._player = player

    def get_player(self):
        return self._player

    def to_dict(self):
        return {
            'house_name': self._house_name,
            'house_id': self._house_id,
            "player_id": self._player_id,
            "number_of_rooms": self._total_number_of_rooms,
            'rooms': [room.__dict__ for room in self._rooms]
        }

    def to_json(self):
        return json.dumps(self.to_dict())
