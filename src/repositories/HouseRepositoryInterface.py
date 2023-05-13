from abc import ABC


class HouseRepositoryInterface(ABC):

    def save(self, house_dict):
        pass

    def find_house_by_id(self, house_id):
        pass
