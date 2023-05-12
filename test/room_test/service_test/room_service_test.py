from unittest import TestCase

from RatAttack.src.services.house_service.HouseServiceImpl import HouseServiceImpl
from RatAttack.src.services.house_service.HouseServiceInterface import HouseServiceInterface
from RatAttack.src.services.room_service.RoomServiceImpl import RoomServiceImpl
from RatAttack.src.services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceTest(TestCase):

    def setUp(self) -> None:
        self.room_Service: RoomServiceInterface = RoomServiceImpl()
        self.house_service: HouseServiceInterface = HouseServiceImpl()

    def test_create_new_room_method(self):
        self.room_Service.create_new_room()
