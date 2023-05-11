from unittest import TestCase

from services.house_service.HouseServiceImpl import HouseServiceImpl
from services.house_service.HouseServiceInterface import HouseServiceInterface
from services.room_service.RoomServiceImpl import RoomServiceImpl
from services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceTest(TestCase):

    def setUp(self) -> None:
        self.room_Service: RoomServiceInterface = RoomServiceImpl()
        self.house_service: HouseServiceInterface = HouseServiceImpl()

    def test_create_new_room_method(self):
        self.room_Service.create_new_room()
