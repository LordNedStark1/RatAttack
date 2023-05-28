from models.collectable.weapons.Bullet import Bullet
from models.collectable.weapons.weapon import Weapon


class Gun(Weapon):
    weapon_type = Weapon.GUN

    def __init__(self):
        self._bullet = []
        self._gun_strength = 10

    def attack(self):
        gun = 10
        if len(self._bullet) != 0:
            return gun * self._bullet.pop().attack()
        return gun

    def load_gun(self, bullets: Bullet):
        self._bullet.append(bullets)


lf = {}
lf.update({"554": 32, 94: 485})
lf.update({"557": 32, 949: 485})
print(lf)
del lf
print(lf)
