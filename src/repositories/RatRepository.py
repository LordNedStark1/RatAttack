from abc import ABC


class RatRepositoryInterface(ABC):
    rats = []
    
    def save(self, rat):
        self.rats.append(rat)
    
    def delete(self, rat):
        self.rats.remove(rat)
