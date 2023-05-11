from src.models.rats.RatInterface import RatInterface


class BigRat(RatInterface):

    def attack(self):
        pass

    def escape(self):
        pass

    def __str__(self):
        return "Am a big rat"

    def __repr__(self):
        return "I will hunt you down"
