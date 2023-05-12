from abc import ABC, abstractmethod

from RatAttack.src.models.Room import Room


class RoomRepositoryInterface(ABC):

    @abstractmethod
    def save(self, room: Room):
        pass

    @abstractmethod
    def find_room_by_id(self, room_id):
        pass
