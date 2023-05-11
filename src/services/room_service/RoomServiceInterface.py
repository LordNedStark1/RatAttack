from abc import ABC, abstractmethod


class RoomServiceInterface(ABC):

    @abstractmethod
    def create_new_room(self):
        pass
    @abstractmethod
    def load_collectables(self, room_id):
        pass