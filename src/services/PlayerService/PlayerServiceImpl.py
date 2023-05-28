from AppUtils.Id_generator.id_generator import IdGenerator
from models.player.Player import Player
from services.PlayerService.PlayerServiceInterface import PlayerServiceInterface
from services.house_service.HouseServiceImpl import HouseServiceImpl
from services.house_service.HouseServiceInterface import HouseServiceInterface


class PlayerServiceImpl(PlayerServiceInterface):
    house_service: HouseServiceInterface = HouseServiceImpl()

    def create_new_player(self, player_name, player_age):
        player = Player()

        player.set_player_name(player_name)
        player.set_player_age(player_age)

        player.set_player_id(IdGenerator.generate_player_id())

        return player.get_player_id(), self.house_service.creat_new_house(player)
