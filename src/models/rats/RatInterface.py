from abc import ABC, abstractmethod


class RatInterface(ABC):
    def __init__(self):
        self._rat_id = ''

    def set_id(self, rat_id):
        self._rat_id = rat_id

    def get_id(self):
        return self._rat_id

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def escape(self):
        pass
