
import string
import random
import datetime

class Randomize:

    @staticmethod
    def generate_random_bool():
        return bool(random.getrandbits(1))

    @staticmethod
    def generate_random_string(min: int, max: int):
        s = string.ascii_letters
        return ''.join(random.sample(s, random.randint(min, max)))

    @staticmethod
    def generate_random_int(min: int, max: int):
        return random.randint(min, max)

    @staticmethod
    def generate_random_date():
        year = random.randint(1950, 2018)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(00, 59)
        second = random.randint(00, 59)
        return datetime.datetime(year, month, day)