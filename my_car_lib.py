

MAX_ITEMS = 10


class Car(object):

    def __init__(self, make=None):
        self.make = make

    @classmethod
    def for_make(cls, make):
        car = cls()
        car.make = make
        return car

    def get_make(self):
        return self.make

    @property
    def wheels(self):
        return 4

    @staticmethod
    def roll_call():
        return [Car('Ford'), Car('Chevy'), Car('BMW'), Car('Audi')]

    def is_car_german(self, car):
        if car in ['Ford', 'BMW', 'Audi']:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.make == other.make
