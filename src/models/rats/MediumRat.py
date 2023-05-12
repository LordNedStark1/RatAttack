from models.AttackInterface import Attacker


class MediumRat(Attacker):

    def attack(self):
        pass

    def __str__(self):
        return "Am a Medium rat"

    def __repr__(self):
        return "I will hunt you a little"
