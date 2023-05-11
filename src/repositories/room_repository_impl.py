from models.Room import Room
from repositories.room_repository_interface import RoomRepositoryInterface


class RoomRepositoryImpl(RoomRepositoryInterface):
    rooms = {}

    def save(self, room : Room):


