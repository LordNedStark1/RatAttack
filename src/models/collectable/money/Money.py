from abc import ABC, abstractmethod

from models.collectable.Collectable import Collectable


class Money(ABC):
    type = Collectable.MONEY

    @abstractmethod
    def supply(self):
        pass

