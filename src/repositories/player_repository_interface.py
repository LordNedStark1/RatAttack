from abc import ABC, abstractmethod
from typing import List

from models.player.Player import Player


class Player_Repository_Interface(ABC):

    @abstractmethod
    def save_player(self, player: Player) -> Player:
        pass

    @abstractmethod
    def find_player_by_id(self, player_id: str) -> Player | None:
        pass

    @abstractmethod
    def get_all_players(self) -> List[Player]:
        pass

    @abstractmethod
    def delete_player_by_id(self, player_id: str) -> bool:
        pass

    @abstractmethod
    def get_player_by_name(self, player_name: str) -> Player | None:
        pass
