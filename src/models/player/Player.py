from models.collectable.money.Money import Money


class Player:

    def __init__(self):
        self._name: str = ""
        self._player_id: str = ""
        self._age: int = 0
        self._health: int = 0
        self._money: Money = None

    def set_player_name(self, player_name: str) -> None:
        self._name = player_name

    def get_player_name(self) -> str:
        return self._name

    def set_player_id(self, player_id: str) -> None:
        self._player_id = player_id

    def get_player_id(self) -> str:
        return self._player_id

    def set_player_age(self, player_age: int) -> None:
        self._age = player_age

    def get_player_age(self) -> int:
        return self._age

    def set_player_health(self, player_health: int) -> None:
        self._health = player_health

    def get_player_health(self) -> int:
        return self._health

    def set_player_money(self, money: Money) -> None:
        self._money = money

    def get_player_money(self) -> Money:
        return self._money

    def to_dict(self):
        return {
            'name': self._name,
            'player_id': self._player_id,
            'age': self._age,
            'health': self._health,
            'money': self._money
        }
