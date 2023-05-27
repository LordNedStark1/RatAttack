import secrets

from models.house_properties.House import House

from models.house_properties.Room import Room
from models.rats.BigRat import BigRat
from models.rats.MediumRat import MediumRat
from models.rats.ParentRat import ParentRat
from models.rats.SmallRat import SmallRat


class RatFactory:
    __rat_id = 1
    def random_number(range):
        return secrets.randbelow(range - 1 + 1) + 1

    @staticmethod
    def create_new_rat():
        rat: ParentRat = None
        option = RatFactory.random_number(3)
        match option:
            case 1:
                rat = SmallRat()
            case 2:
                rat = MediumRat()
            case 3:
                rat = BigRat()
        rat
        return rat

    @staticmethod
    def load_rats(house: House, count=0):
        rooms = house.get_rooms()

        rooms_index = RatFactory.random_number(5)
        if RatFactory._count_rat_number_in_house(house) < 5:
            if rooms_index is not None:
                if count < 6:

                    locations = rooms[rooms_index].get_room_locations()

                    locations_index = RatFactory.random_number(5)
                    if locations_index is not None:
                        if locations[locations_index].get_rat() is None:
                            locations[locations_index].set_rat(RatFactory.create_new_rat())

                            count += 1
                            RatFactory.load_rats(house, count)

        house.set_total_number_of_rats(RatFactory._count_rat_number_in_house(house))
        return house

    def _count_rat_number_in_house(house: House):
        rooms = house.get_rooms()

        return RatFactory._check_rooms(rooms)

    def _check_rooms(rooms):
        count = 0
        for value in rooms:
            room: Room = value
            locations = room.get_room_locations()

            count += RatFactory._check_locations(locations)
        return count

    def _check_locations(locations):
        count = 0

        for location in locations:
            rat = location.get_rat()
            if rat is not None:
                count += 1

        return count
