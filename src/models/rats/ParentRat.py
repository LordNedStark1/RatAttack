from abc import abstractmethod

from models.Attacker import Attacker


class ParentRat(Attacker):
    def __init__(self):
        self._rat_id = ""

    @abstractmethod
    def attack(self):
        pass
