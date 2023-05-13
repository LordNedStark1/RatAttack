from unittest import TestCase

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
