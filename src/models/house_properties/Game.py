from flask import json


class Game:
    def __init__(self):
        self._total_number_of_rats = 0
        self._game_id = ""
        self._game_player_name = ""
        self._player = None
        self._total_number_of_houses = 0
        self._houses = []

    def set_total_number_of_houses(self, total):
        self._total_number_of_houses = total

    def get_total_number_of_houses(self):
        return self._total_number_of_houses
    def add_new_house(self, house):
        self._houses.append(house)

    def get_houses(self):
        return self._houses

    def set_game_id(self, house_id):
        self._game_id = house_id

    def get_house_id(self):
        return self._game_id

    def set_game_player_name(self, game_name):
        self._game_player_name = game_name

    def get_game_player_name(self):
        return self._game_player_name

    def set_player(self, player):
        self._player = player

    def get_player(self):
        return self._player

    def to_dict(self):
        houses_list = []
        for room in self._houses:
            houses_list.append(room.to_dict())

        return {
            'game_player_name': self._game_player_name,
            'game_id': self._game_id,
            'total_number_of_rats': self._total_number_of_rats,
            "number_of_houses": self._total_number_of_houses,
            'player': self._player.to_dict(),
            'houses': houses_list
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def set_total_number_of_rats(self, rat_count):
        self._total_number_of_rats = rat_count
