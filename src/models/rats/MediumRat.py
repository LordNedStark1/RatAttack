from RatAttack.src.models.rats.RatInterface import RatInterface


class MediumRat(RatInterface):
    def attack(self):
        pass

    def escape(self):
        pass

    def __str__(self):
        return "Am a Medium rat"

    def __repr__(self):
        return "I will hunt you a little"
