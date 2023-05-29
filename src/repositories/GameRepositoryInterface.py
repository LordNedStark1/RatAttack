from abc import ABC


class GameRepositoryInterface(ABC):

    def save(self, game_dict):
        pass

    def find_game_by_id(self, game_id):
        pass
