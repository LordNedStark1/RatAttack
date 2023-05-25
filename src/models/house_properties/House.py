from flask import json


class House:
    def __init__(self):
        self._house_id = ""
        self._house_name = ""
        self._player = None
        self._total_number_of_rooms = 0
        self._rooms = []

    def set_total_number_of_rooms(self, total):
        self._total_number_of_rooms = total

    def get_total_number_of_rooms(self):
        return self._total_number_of_rooms
    def set_rooms(self, rooms):
        self._rooms.append( rooms)

    def get_rooms(self):
        return self._rooms

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
        rooms_list = []
        for room in self._rooms:
            rooms_list.append(room.to_dict())

        return {
            'house_name': self._house_name,
            'house_id': self._house_id,
            'player': self._player.to_dict(),
            "number_of_rooms": self._total_number_of_rooms,
            'rooms': rooms_list
        }

    def to_json(self):
        return json.dumps(self.to_dict())
