import random


class Health:

    @staticmethod
    def supply():
        health = random.randint(1, 100)

        return health
