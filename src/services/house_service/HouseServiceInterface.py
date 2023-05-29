from abc import ABC, abstractmethod


class HouseServiceInterface(ABC):

    @abstractmethod
    def create_new_house(self):
        pass

    @abstractmethod
    def load_collectables(self, room_id):
        pass
