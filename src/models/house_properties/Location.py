from typing import List


class Location:
    def __init__(self):
        self.__location_id = ""
        self.__rat = None
        self.__collectable = []

    def set_location_id(self, location_id):
        self.__location_id = location_id

    def get_location_id(self):
        return self.__location_id

    def set_rat(self, rat):
        self.__rat = rat

    def get_rat(self) :
        return self.__rat

    def set_collectables(self, collectable):
        self.__collectable.append(collectable)

    def get_collectables(self):
        return self.__collectable

    def to_dict(self):
        rat = None
        if self.__rat is not None:
            rat = self.__rat.to_dict()
        return {
            'location_id': self.__location_id,
            'rat': rat,
            'collectable': self.__collectable
        }

    def __repr__(self):
        return f"Location(location_id={self.__location_id}, rat={self.__rat}," \
               f" collectable={self.__collectable})"
