from AppUtils.factory.RatFactory import RatFactory
from models.house_properties.Room import Room
from services.location_service.LocationServiceImpl import LocationServiceImpl
from services.location_service.LocationServiceInterface import LocationServiceInterface
from services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceImpl(RoomServiceInterface):
    location_service: LocationServiceInterface = LocationServiceImpl()

    def create_new_room(self):
        room: Room = Room()
        locations = self.location_service.create_room_location()
        room.set_room_locations(locations)

        return room

    def load_collectables(self, room: Room):
        room.get_room_locations()



