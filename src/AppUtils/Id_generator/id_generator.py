import uuid

database = {}
database.update({"string_id1": 89})
database.update({"string_id2": 34})
database.update({"string_id3": 78})
database.update({"string_id4": 45})

class IdGenerator:

    @staticmethod
    def generate_id(obj):
        return id(obj)

    @staticmethod
    def generate_player_id() -> str:
        empty_string = ""
        for i in range(0, len(IdGenerator.generate_random_uuid_values())):
            if i % 4 == 0:
                empty_string += " "
            if IdGenerator.generate_random_uuid_values()[i] == "-":
                continue
            if len(empty_string) > 10:
                break
            empty_string += IdGenerator.generate_random_uuid_values()[i]
        return empty_string.upper().strip()

    @staticmethod
    def generate_random_uuid_values() -> str:
        return str(uuid.uuid4())


if __name__ == '__main__':
    Ids = IdGenerator()
    print(Ids.generate_player_id())
    print(Ids.generate_random_uuid_values())
