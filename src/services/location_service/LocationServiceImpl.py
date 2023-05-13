from models.house_properties.Location import Location
from services.location_service.LocationServiceInterface import LocationServiceInterface


class LocationServiceImpl(LocationServiceInterface):
    def create_room_location(self):
        location_list = []
        for i in range(1, 7):
            location: Location = Location()
            location.set_location_id(i)
            location_list.append(location)

        return location_list

