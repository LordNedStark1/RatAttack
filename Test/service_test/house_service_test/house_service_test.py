from unittest import TestCase

from models.house_properties.House import House
from models.house_properties.Location import Location
from models.house_properties.Room import Room
from models.player.Player import Player
from services.house_service.HouseServiceImpl import HouseServiceImpl
from services.house_service.HouseServiceInterface import HouseServiceInterface


class HouseServiceTest(TestCase):
    def setUp(self) -> None:
        self.house_service: HouseServiceInterface = HouseServiceImpl()
        self.player: Player = Player()
        self.player.set_player_name("Dapo")

    def test_create_new_house_method(self):
        house_id = self.house_service.creat_new_house(self.player)
        self.assertIsNotNone(self.house_service.find_house_by_id(house_id))


    def test_that_the_house_has_at_least_three_rat_at_most_four(self):
        house_id = self.house_service.creat_new_house(self.player)
        self.assertIsNotNone(self.house_service.find_house_by_id(house_id))
        new_house = self.house_service.find_house_by_id(house_id)
        self.check_presence_of_rats(new_house)

    def check_presence_of_rats(self, house: House):
        rooms = house.get_rooms()
        count = self.__is_three_rat_present(rooms)
        print(count)

    def __is_three_rat_present(self, rooms):
        count = 0
        for value in rooms:
            room: Room = value
            locations = room.get_room_locations()
            count += self._check_locations(locations)
        return count

    def _check_locations(self, locations):
        count = 0
        for local in locations:
            location: Location = local
            if location.get_rat() is not None:
                count += 1

        return count


