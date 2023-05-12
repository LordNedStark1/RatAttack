
class Room:
    def __init__(self):
        self._room_id = 0
        self._rats = []
        self._collectable = []

    def set_room_id(self, room_id):
        self._room_id = room_id

    def get_room_id(self):
        return self._room_id

    def get_rats_id(self):
        return self._room_id

    # Todo method below is to be verified
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

