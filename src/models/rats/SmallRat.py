from src.models.rats.RatInterface import RatInterface


class SmallRat(RatInterface):

    def attack(self):
        pass

    def escape(self):
        pass

    def __str__(self):
        return "Am a small rat"

    def __repr__(self):
        return "I will hunt you but run maybe"
