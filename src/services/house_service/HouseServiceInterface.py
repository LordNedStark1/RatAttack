from abc import ABC, abstractmethod

from models.player.Player import Player


class HouseServiceInterface(ABC):
    @abstractmethod
    def creat_new_house(self, player: Player):
        pass

    @abstractmethod
    def find_house_by_id(self, house_id):
        pass
