import secrets

from models.house_properties.House import House
from models.house_properties.Location import Location
from models.house_properties.Room import Room
from models.rats.BigRat import BigRat
from models.rats.MediumRat import MediumRat
from models.rats.SmallRat import SmallRat


class RatFactory:

    @staticmethod
    def random_number(range):
        return secrets.randbelow(range - 1 + 1) + 1

    @staticmethod
    def create_new_rat():
        rat = ""
        option = RatFactory.random_number(3)
        match option:
            case 1:
                rat = SmallRat()
            case 2:
                rat = MediumRat()
            case 3:
                rat = BigRat()

        return rat

    @staticmethod
    def load_rats(house: House, count=0):
        rooms = house.get_rooms()
        rat_count = 0

        rooms_index = RatFactory.random_number(5)
        if rooms_index is not None:
            if count < 6:

                locations = rooms[rooms_index].get_room_locations()

                locations_index = RatFactory.random_number(5)
                if locations_index is not None:
                    if locations[locations_index].get_rat() is None:
                        rat_count += 1
                        locations[locations_index].set_rat(RatFactory.create_new_rat())

                        count += 1
                        RatFactory.load_rats(house, count)

        house.set_total_number_of_rats(rat_count)
        return house




