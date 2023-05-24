from unittest import TestCase

from models.house_properties.Location import Location
from models.house_properties.Room import Room
from services.room_service.RoomServiceImpl import RoomServiceImpl
from services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceTest(TestCase):

    def setUp(self) -> None:
        self.room_Service: RoomServiceInterface = RoomServiceImpl()

    def test_create_new_room_method(self):
        created_room: Room = self.room_Service.create_new_room()
        self.assertIsNotNone(created_room)

    def test_room_has_three_rats(self):
        created_room: Room = self.room_Service.create_new_room()
        locations: Location = created_room.get_room_locations()
        is_present = self.__is_three_rat_prestent(locations)
        self.assertTrue(is_present)

    def __is_three_rat_prestent(self, locations):
        count = 0
        for i in range(len(locations)):
            location: Location = locations[i]
            if location.get_rat() is not None:
                count += 1
        if count > 3: return False
        if 0 < count <= 3: return True


    def test_health_in_room(self):
        created_room: Room = self.room_Service.create_new_room()
        locations: Location = created_room.get_room_locations()


