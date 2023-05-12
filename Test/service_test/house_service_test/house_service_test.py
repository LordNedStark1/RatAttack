from unittest import TestCase

from repositories.MongoDbHouseRepository import MongoDbHouseRepository


class HouseServiceTest(TestCase):
    def setUp(self) -> None:
        self.mongo_house_repo = MongoDbHouseRepository.get_instance()
