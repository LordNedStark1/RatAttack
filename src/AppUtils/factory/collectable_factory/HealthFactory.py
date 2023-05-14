import secrets
from typing import List

from models.collectable.Collectable import Collectable
from models.collectable.health.HighHealth import HighHealth
from models.collectable.health.LowHealth import LowHealth
from models.collectable.health.NoHealth import NoHealth

from models.collectable.money.ZeroNaira import ZeroNaira
from models.house_properties.Location import Location
from models.house_properties.Room import Room


class HealthFactory:
    @staticmethod
    def create_new_health():
        health = ""
        option = secrets.randbelow(3 - 1 + 1) + 1
        match option:
            case 1:
                health = NoHealth()
            case 2:
                health = LowHealth()
            case 3:
                health = HighHealth()

        return health

    @staticmethod
    def load_healths(room: Room, count=0):
        locations = room.get_room_locations()

        random_index = secrets.randbelow(5 - 1 + 1) + 1
        if random_index is not None:
            if count <= 2:
                collectables: List = locations[random_index].get_collectables()
                found = HealthFactory.search(collectables)
                if not found:
                    locations[random_index].set_collectaable(HealthFactory.create_new_health())

                    count += 1
                    HealthFactory.load_healths(room, count)
            return room

    @staticmethod
    def search(collectables):
        for i in range(len(collectables)):
            if collectables[i].type == Collectable.HEALTH:
                return True
        return False


high = HighHealth()
low = LowHealth()
money = ZeroNaira()
high.type = Collectable.HEALTH
low.type = Collectable.HEALTH
money.type = Collectable.MONEY
list = [ money]
# print(HealthFactory.search(list))


room = Room()
list = []

for i in range(8):
    location = Location()
    list.append(location)

room.set_room_locations(list),
