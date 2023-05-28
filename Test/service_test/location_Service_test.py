from unittest import TestCase

from models.house_properties.Location import Location
from services.location_service.LocationServiceImpl import LocationServiceImpl
from services.location_service.LocationServiceInterface import LocationServiceInterface


class LocationServiceTest(TestCase):
    def setUp(self) -> None:
        self.location_service: LocationServiceInterface = LocationServiceImpl()

    def test_create_new_room_method(self):
        created_locations = self.location_service.create_room_location()
        self.assertIsNotNone(created_locations[0])
        self.assertEqual(6, len(created_locations))
        self.assertEqual(1, created_locations[0].get_location_id())
        self.assertEqual(6, created_locations[5].get_location_id())

    # def test_properties_of_room(self):
    #     created_locations = self.location_service.create_room_location()
    #     for i in range(len(created_locations)):
    #         location = created_locations[i]
    #         self.assertEqual(3, len(location.get_rats()))

