from bson import ObjectId

from AppUtils.factory.RatFactory import RatFactory
from models.house_properties.House import House
from models.player.Player import Player
from repositories.MongoDbHouseRepository import MongoDbHouseRepository
from services.house_service.HouseServiceInterface import HouseServiceInterface
from services.room_service.RoomServiceImpl import RoomServiceImpl
from services.room_service.RoomServiceInterface import RoomServiceInterface


def converting_house_to_dictionary(house):
    # return house.to_json()
    return house.to_dict()


class HouseServiceImpl(HouseServiceInterface):
    mongo_house_repo: MongoDbHouseRepository = MongoDbHouseRepository.get_instance()
    room_service: RoomServiceInterface = RoomServiceImpl()

    def creat_new_house(self, player: Player):
        house: House = House()

        house.set_house_name(player.get_player_name())
        house.set_player(player)

        for i in range(1, 7):
            created_room = self.room_service.create_new_room()
            created_room.set_room_id(i)

            house.set_rooms(created_room)

        self.__load_rats(house)

        house_dict = converting_house_to_dictionary(house)
        house_id = self.mongo_house_repo.save(house_dict)

        return house_id

    def __load_rats(self, house: House):
        return RatFactory.load_rats(house)

    def find_house_by_id(self, house_id):
        house_dict = self.mongo_house_repo.find_house_by_id(house_id)
        return house_dict
