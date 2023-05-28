from models.collectable.health.Health import Health


class LowHealth(Health):

    def supply(self):
        return 10

