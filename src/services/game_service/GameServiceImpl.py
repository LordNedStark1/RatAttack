from bson import ObjectId

from AppUtils.factory.RatFactory import RatFactory
from models.house_properties.Game import Game
from models.player.Player import Player
from repositories.MongoDbGameRepository import MongoDbGameRepository
from services.game_service.GameServiceInterface import GameServiceInterface
from services.house_service.HouseServiceImpl import HouseServiceImpl
from services.house_service.HouseServiceInterface import HouseServiceInterface


def converting_house_to_dictionary(house):
    # return house.to_json()
    return house.to_dict()


class GameServiceImpl(GameServiceInterface):
    mongo_game_repo: MongoDbGameRepository = MongoDbGameRepository.get_instance()
    house_service: HouseServiceInterface = HouseServiceImpl()

    def creat_new_game(self, player: Player):
        game: Game = Game()

        game.set_game_player_name(player.get_player_name())
        game.set_player(player)

        for i in range(1, 7):
            created_house = self.house_service.create_new_house()
            created_house.set_room_id(i)

            game.add_new_house(created_house)

        self.__load_rats(game)

        game_ict = converting_house_to_dictionary(game)
        game_id = self.mongo_game_repo.save(game_ict)

        return game_id

    def __load_rats(self, game: Game):
        return RatFactory.load_rats(game)

    def find_game_by_id(self, game_id):
        converted_game_id = ObjectId(game_id)
        return self.mongo_game_repo.find_game_by_id(converted_game_id)

