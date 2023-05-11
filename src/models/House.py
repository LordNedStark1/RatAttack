from models.rats.RatInterface import RatInterface


class House:
    def __init__(self):
        self._house_name = ""
        self._playerId = ""
        self._houseId = ""
        self._total_number_of_rooms = 6
        self._roomsId = []
