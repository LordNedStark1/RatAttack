from unittest import TestCase

from AppUtils.word_generator.WordGenerator import WordGenerator

from models.house_properties.House import House
from models.player.Player import Player
from services.game_service.GameServiceImpl import GameServiceImpl
from services.game_service.GameServiceInterface import GameServiceInterface


class GameServiceTest(TestCase):

    def setUp(self) -> None:
        self.game_service: GameServiceInterface = GameServiceImpl()
        self.player: Player = Player()
        self.player.set_player_name(self._generate_name())

    def test_create_new_house_method(self):
        house_id = self.game_service.creat_new_game(self.player)
        self.assertIsNotNone(self.game_service.find_game_by_id(house_id))

    def test_that_the_house_has_at_least_three_rat_at_most_five(self):
        rat_house = []
        for i in range(30):
            count = self.house_creation_method()
            rat_house.append(count)

        is_rat_up_to_three = False
        is_rat_up_to_four = False
        is_rat_up_to_five = False
        is_rat_within_one_and_five = False
        is_rat_up_to_six = False

        for value in rat_house:
            if value == 6:
                is_rat_up_to_six = True

        for value in rat_house:
            if value == 5:
                is_rat_up_to_five = True

        for value in rat_house:
            if value == 4:
                is_rat_up_to_four = True

        for value in rat_house:
            if value == 3:
                is_rat_up_to_three = True

        for value in rat_house:
            if value >= 1:
                if value <= 5:
                    is_rat_within_one_and_five = True

        self.assertTrue(is_rat_within_one_and_five)
        self.assertTrue(is_rat_up_to_three)
        self.assertTrue(is_rat_up_to_four)
        self.assertTrue(is_rat_up_to_five)
        self.assertFalse(is_rat_up_to_six)

    def house_creation_method(self):
        self.player.set_player_name(self._generate_name())
        house_id = self.game_service.creat_new_game(self.player)
        self.assertIsNotNone(self.game_service.find_game_by_id(house_id))
        new_house_dict = self.game_service.find_game_by_id(house_id)
        count = self.check_presence_of_rats(new_house_dict)
        return count

    def check_presence_of_rats(self, game_dict):
        houses = game_dict.get('rooms')

        return self.__is_three_rat_present(houses)

    def __is_three_rat_present(self, houses):
        count = 0
        for value in houses:
            room: House = value
            locations = room['room_locations']

            count += self._check_locations(locations)
        return count

    def _check_locations(self, locations):
        count = 0

        for local in locations:
            rat = local['rat']
            if rat is not None:
                count += 1

        return count

    def _generate_name(self):
        return WordGenerator.generate_name()
