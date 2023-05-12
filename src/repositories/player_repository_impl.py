from RatAttack.src.AppUtils.Id_generator.id_generator import IdGenerator
from RatAttack.src.models.player.Player import Player
from RatAttack.src.repositories.player_repository_interface import Player_Repository_Interface


class Player_Repository_Implementation(Player_Repository_Interface):
    database_of_players = {}

    def save_player(self, player: Player) -> Player:
        if self.player_does_not_exist(player):
            self._save_new_player(player)
        return self._existing_player(player)

    def find_player_by_id(self, player_id) -> Player | None:
        if player_id in self.database_of_players:
            found_object = self.database_of_players[player_id]
            return found_object
        return None

    def delete_player_by_id(self, player_id) -> bool:
        player_to_be_deleted = self.find_player_by_id(player_id)
        if player_to_be_deleted is not None or player_to_be_deleted in self.database_of_players:
            del self.database_of_players[player_id]
            return True
        return False

    def get_player_by_name(self, player_name) -> Player | None:
        for each_id in self.database_of_players:
            if self.database_of_players[each_id].get_player_name() == player_name:
                return self.database_of_players[each_id]
        return None

    def get_all_players(self) -> dict[str, Player]:
        return self.database_of_players

    def player_does_not_exist(self, player: Player):
        if player not in self.database_of_players:
            return True
        return False

    def _save_new_player(self, player: Player):
        player.set_player_id(IdGenerator.generate_player_id())
        self.database_of_players.update({player.get_player_id(): player})

    def _existing_player(self, player: Player) -> Player | None:
        found_player: Player = self.find_player_by_id(player.get_player_id())
        if found_player is not None:
            return player
        return None
