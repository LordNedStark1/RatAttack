from unittest import TestCase

from models.Room import Room
from repositories.room_repository_impl import RoomRepositoryImpl
from repositories.room_repository_interface import RoomRepositoryInterface


class RoomRepositoryTest(TestCase):
    room_repo: RoomRepositoryInterface = RoomRepositoryImpl()

    def test_save(self):
        room = Room()
        saved_room: Room = self.room_repo.save(room)
        self.assertEqual(saved_room, self.room_repo.find_room_by_id(saved_room.get_room_id()))

