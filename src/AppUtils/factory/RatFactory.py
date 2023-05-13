import secrets

from models.house_properties.Location import Location
from models.house_properties.Room import Room
from models.rats.BigRat import BigRat
from models.rats.MediumRat import MediumRat
from models.rats.SmallRat import SmallRat


class RatFactory:

    @staticmethod
    def create_new_rat():
        rat = ""
        option = secrets.randbelow(3 - 1 + 1) + 1
        match option:
            case 1:
                rat = SmallRat()
            case 2:
                rat = MediumRat()
            case 3:
                rat = BigRat()

        return rat

    @staticmethod
    def load_rats(room: Room, count=0):
        locations = room.get_room_locations()

        random_index = secrets.randbelow(5 - 1 + 1) + 1
        if random_index is not None:
            if count < 3:
                if locations[random_index].get_rat() is None:
                    locations[random_index].set_rat(RatFactory.create_new_rat())

                    count += 1
                    RatFactory.load_rats(room, count)
            return room


room = Room()
list = []

for i in range(8):
    location = Location()
    list.append(location)

room.set_room_locations(list)

room1 = RatFactory.load_rats(room)

locatons = room1.get_room_locations()
# for i in range(8):
#     print(locatons[i].get_rat())
