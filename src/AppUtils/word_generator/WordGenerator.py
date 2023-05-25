import random


class WordGenerator:
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    @classmethod
    def generate_name(cls):
        word = ''
        word += WordGenerator.consonants[cls.random_number(20)]
        word += WordGenerator.vowels[cls.random_number(4)]
        word += WordGenerator.consonants[cls.random_number(20)]
        word += WordGenerator.vowels[cls.random_number(4)]
        word += WordGenerator.vowels[cls.random_number(4)]
        word += WordGenerator.consonants[cls.random_number(20)]

        return word

    @classmethod
    def random_number(cls, word_range):
        return random.randint(0, word_range)

