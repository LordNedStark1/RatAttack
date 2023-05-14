from abc import abstractmethod, ABC

from models.Attacker import Attacker
from models.collectable.Collectable import Collectable


class Weapon(Attacker, ABC):
    type = Collectable.WEAPON

