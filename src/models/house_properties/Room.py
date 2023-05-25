import json


class Room:
    def __init__(self):
        self._room_id = ""
        self._room_locations = []

    def set_room_id(self, room_id):
        self._room_id = room_id

    def get_room_id(self):
        return self._room_id

    def get_room_locations(self):
        return self._room_locations

    def set_room_locations(self, locations):
        self._room_locations = locations

    # Todo method below is to be verified
    def to_dict(self):
        location_list = []
        for location in self._room_locations:
            location_list.append(location.to_dict())
        return {
            'room_id': self._room_id,
            'room_location': location_list
        }

    def to_json(self):
        return json.dumps(self.to_dict())
