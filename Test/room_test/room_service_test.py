from unittest import TestCase

from services.room_service.RoomServiceImpl import RoomServiceImpl
from services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceTest(TestCase):

    def setUp(self) -> None:
        self.room_Service: RoomServiceInterface = RoomServiceImpl()


    def test_create_new_room_method(self):
        self.room_Service.create_new_room()
