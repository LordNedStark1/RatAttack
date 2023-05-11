from random import random, randint

from models.rats.BigRat import BigRat
from models.rats.MediumRat import MediumRat
from models.rats.SmallRat import SmallRat


class RatFactory:

    @staticmethod
    def create_new_rat():
        rat = ""
        option = randint(1, 3)
        match option:
            case 1:
                rat = SmallRat()
            case 2:
                rat = MediumRat()
            case 3:
                rat = BigRat()

        return rat
