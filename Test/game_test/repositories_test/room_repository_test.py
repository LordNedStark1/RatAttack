from unittest import TestCase

from models.house_properties.House import House
from repositories.room_repository_impl import RoomRepositoryImpl
from repositories.room_repository_interface import RoomRepositoryInterface


class RoomRepositoryTest(TestCase):
    room_repo: RoomRepositoryInterface = RoomRepositoryImpl()

    def test_save(self):
        room = House()
        saved_room: House = self.room_repo.save(room)
        self.assertEqual(saved_room, self.room_repo.find_room_by_id(saved_room.get_room_id()))
