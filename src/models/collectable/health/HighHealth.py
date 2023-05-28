from models.collectable.health.Health import Health


class HighHealth(Health):

    def supply(self):
        return 50
