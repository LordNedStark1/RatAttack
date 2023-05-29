from AppUtils.factory.RatFactory import RatFactory
from models.house_properties.House import House
from services.location_service.LocationServiceImpl import LocationServiceImpl
from services.location_service.LocationServiceInterface import LocationServiceInterface
from services.house_service.HouseServiceInterface import HouseServiceInterface


class HouseServiceImpl(HouseServiceInterface):
    location_service: LocationServiceInterface = LocationServiceImpl()

    def create_new_house(self):
        room: House = House()
        locations = self.location_service.create_room_location()
        room.set_room_locations(locations)

        return room

    def load_collectables(self, room: House):
        room.get_room_locations()



