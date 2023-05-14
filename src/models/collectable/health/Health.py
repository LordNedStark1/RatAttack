import random
from abc import ABC, abstractmethod

from models.collectable.Collectable import Collectable


class Health(ABC):
    type = Collectable.HEALTH

    @abstractmethod
    def supply(self):
        pass

