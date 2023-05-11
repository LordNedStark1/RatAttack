from abc import ABC, abstractmethod


class RoomRepositoryInterface(ABC):

    @abstractmethod
    def save(self, room):
        pass