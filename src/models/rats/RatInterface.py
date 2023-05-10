from abc import ABC, abstractmethod


class RatInterface(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def escape(self):
        pass
