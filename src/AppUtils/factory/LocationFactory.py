from AppUtils.factory.RatFactory import RatFactory
from models.house_properties.Location import Location


class LocationFactory:

    @staticmethod
    def populate_location_with_collectables(location: Location):
        pass

    @staticmethod
    def populate_location_with_rats():
        rat_list = []
        for i in range (3):
            rat_list.append(RatFactory.create_new_rat())
        # location.set_rats(rat_list)
        return rat_list

print (LocationFactory.populate_location_with_rats())

