from models.house_properties.House import House
from models.player.Player import Player
from repositories.MongoDbHouseRepository import MongoDbHouseRepository
from services.house_service.HouseServiceInterface import HouseServiceInterface
from services.room_service.RoomServiceImpl import RoomServiceImpl
from services.room_service.RoomServiceInterface import RoomServiceInterface


class HouseServiceImpl(HouseServiceInterface):

    mongo_house_repo: MongoDbHouseRepository = MongoDbHouseRepository.get_instance()
    room_service: RoomServiceInterface = RoomServiceImpl()

    def creat_new_house(self, player: Player):
        house: House = House()
        house.set_house_name(player.get_player_name())

        created_room = self.room_service.create_new_room()
        # house_dict = converting_house_to_dictionary(house)
        # self.mongo_house_repo.save(house_dict)

    def find_house_by_id(self, house_id):
        return self.mongo_house_repo.find_house_by_id(house_id)
