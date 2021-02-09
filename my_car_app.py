from my_car_lib import MAX_ITEMS, Car


def get_max_items():
    return MAX_ITEMS


def get_car_make(make=None):
    car = Car()
    if make:
        car = Car.for_make(make)
    return car.get_make()


def get_car_wheels():
    return Car().wheels


def get_roll_call():
    return Car.roll_call()


def is_car_made_in_germany():
    car = Car()
    return car.is_car_german(car.make)
