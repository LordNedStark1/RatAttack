import unittest

from models.player.Player import Player
from repositories.player_repository_impl import Player_Repository_Implementation


class Player_Repository_Test(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.player = Player()
        cls.player_repo = Player_Repository_Implementation()

    def test_save_new_user(self):
        self.player_repo.save_player(self.player)
        self.assertEqual(1, len(self.player_repo.get_all_players()))

    def test_save_user_multiple_times_count_does_not_increment(self):
        self.player_repo.save_player(self.player)
        print("The first player is: "+self.player.get_player_id())
        self.player_repo.save_player(self.player)
        print("The second player is: "+self.player.get_player_id())
        self.assertEqual(1, len(self.player_repo.get_all_players()))

    def test_find_player_by_id(self):
        saved_player = self.player_repo.save_player(self.player)
        found_player = self.player_repo.find_player_by_id(saved_player.get_player_id())
        self.assertIsNotNone(found_player)

    def test_find_player_by_name(self):
        saved_player = self.player_repo.save_player(self.player)
        found_player = self.player_repo.get_player_by_name(saved_player.get_player_name())
        self.assertIsNotNone(found_player)

    def test_get_all_players(self):
        saved_player = self.player_repo.save_player(self.player)
        player2: Player = Player()
        saved_player2 = self.player_repo.save_player(player2)
        for players in self.player_repo.get_all_players():
            self.assertIsNotNone(players)
        self.assertEqual(2, len(self.player_repo.get_all_players()))
