from models.AttackInterface import Attacker


class SmallRat(Attacker):

    def attack(self):
        pass

    def __str__(self):
        return "Am a small rat"

    def __repr__(self):
        return "I will hunt you but run maybe"
