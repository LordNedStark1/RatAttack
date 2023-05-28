from unittest import TestCase

from AppUtils.word_generator.WordGenerator import WordGenerator
from services.PlayerService.PlayerServiceImpl import PlayerServiceImpl
from services.PlayerService.PlayerServiceInterface import PlayerServiceInterface


class HouseServiceTest(TestCase):
    def setUp(self) -> None:
        self.player_service: PlayerServiceInterface = PlayerServiceImpl()

    def test_create_new_house_method(self):
        house_id , player_id = self.player_service.create_new_player(self._generate_name(), 20)
        # self.assertIsNotNone(self.player_service.find_house_by_id(house_id))

    def _generate_name(self):
        return WordGenerator.generate_name()