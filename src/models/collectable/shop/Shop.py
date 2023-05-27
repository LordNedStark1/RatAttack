from models.collectable.health.HighHealth import HighHealth
from models.collectable.health.LowHealth import LowHealth
from models.collectable.health.MediumHealth import MediumHealth
from models.collectable.weapons.Bullet import Bullet
from models.collectable.weapons.Gun import Gun
from models.collectable.weapons.Knife import Knife


class Shop:
    def buy_gun(self):
        return Gun()

    def buy_knife(self):
        return Knife()

    def buy_bullet(self, bullet_number):
        return Bullet(bullet_number)

    def buy_high_health(self):
        return HighHealth()

    def buy_medium_health(self):
        return MediumHealth()

    def buy_low_health(self):
        return LowHealth()
