from AppUtils.Id_generator.id_generator import IdGenerator
from models.Room import Room
from repositories.room_repository_interface import RoomRepositoryInterface


class RoomRepositoryImpl(RoomRepositoryInterface):
    rooms = {}

    def save(self, room : Room):
        room.set_room_id(IdGenerator.generate_id(room))
        self.rooms[room.get_room_id()] = room

    def find_room_by_id(self, room_id):
        return self.rooms.get(room_id)

