from models.Room import Room
from services.room_service.RoomServiceInterface import RoomServiceInterface


class RoomServiceImpl(RoomServiceInterface):

    def create_new_room(self, house_id):
        room = Room()

    def load_collectables(self, room_id):
        pass