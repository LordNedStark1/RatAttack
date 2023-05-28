from abc import ABC
from enum import Enum

from models.Attacker import Attacker
from models.collectable.Collectable import Collectable


class Weapon(Attacker, ABC):
    GUN = 0
    KNIFE = 1
    BULLET = 2
    type = Collectable.WEAPON
