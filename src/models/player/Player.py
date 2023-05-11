from models.collectable.Money import Money


class Player:

    def __init__(self):
        self._name = ""
        self._age = ""
        self._health: int = 0
        self._money = Money()

    def set_player_name(self, player_name: str) -> None:
        self._name = player_name

    def get_player_name(self) -> str:
        return self._name

    def set_player_age(self, player_age: str) -> None:
        self._age = player_age

    def get_player_age(self) -> str:
        return self._age

    def set_player_health(self, player_health: int) -> None:
        self._health = player_health

    def get_player_health(self) -> int:
        return self._health

    def set_player_money(self, money: Money) -> None:
        self._money = money

    def get_player_money(self) -> Money:
        return self._money
