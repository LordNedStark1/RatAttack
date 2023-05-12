from flask import json


class House:
    def __init__(self):
        self._house_name = ""
        self._player_id = ""
        self._house_id = ""
        self._total_number_of_rooms = 6
        self._rooms = []

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

