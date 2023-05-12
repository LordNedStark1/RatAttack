
class Room:
    def __init__(self):
        self._room_id = 0
        self._rats_id = []
        self._collectable = []

    def set_room_id(self, room_id):
        self._room_id = room_id

    def get_room_id(self):
        return self._room_id

    def get_rats_id(self):
        return self._room_id


