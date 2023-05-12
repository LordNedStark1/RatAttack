from models.AttackInterface import Attacker


class BigRat(Attacker):

    def attack(self):
        pass

    def __str__(self):
        return "Am a big rat"

    def __repr__(self):
        return "I will hunt you down"
