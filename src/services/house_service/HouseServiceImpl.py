from models.House import House
from models.player.Player import Player
from repositories.MongoDbHouseRepository import MongoDbHouseRepository
from services.house_service.HouseServiceInterface import HouseServiceInterface


class HouseServiceImpl(HouseServiceInterface):
    mongo_house_repo: MongoDbHouseRepository = MongoDbHouseRepository.get_instance()
    def creat_new_house(self, player: Player):
        house: House = House()
        house.set_house_name(player.get_player_name())
        house.set_player(player)

        house_dict = converting_house_to_dictionary(house)
        self.mongo_house_repo.save(house_dict)
