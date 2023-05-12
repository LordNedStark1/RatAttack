from RatAttack.src.repositories.RatRepositoryIntrface import RatRepositoryInterface


class RatRepositoryImpl(RatRepositoryInterface):
    rats = {}

    def save(self, rat: RatInterface):
        self.rats[rat] = rat

    def delete(self, rat):
        self.rats.remove(rat)
