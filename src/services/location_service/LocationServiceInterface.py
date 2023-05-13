from abc import abstractmethod


class LocationServiceInterface:
    @abstractmethod
    def create_room_location(self):
        pass