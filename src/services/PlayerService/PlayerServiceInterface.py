from abc import abstractmethod


class PlayerServiceInterface:

    @abstractmethod
    def create_new_player(self, player_name, player_age):
        pass