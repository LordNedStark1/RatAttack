from abc import ABC, abstractmethod


class RatRepositoryInterface(ABC):

    @abstractmethod
    def save(self, rat):
        pass

    @abstractmethod
    def delete(self, rat):
        pass
