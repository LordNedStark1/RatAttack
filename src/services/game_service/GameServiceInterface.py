from abc import ABC, abstractmethod

from models.player.Player import Player


class GameServiceInterface(ABC):
    @abstractmethod
    def creat_new_game(self, player: Player):
        pass

    @abstractmethod
    def find_game_by_id(self, game_id):
        pass
