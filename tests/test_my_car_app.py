import unittest
from unittest import mock
from my_car_app import get_max_items, get_car_make, get_car_wheels, get_roll_call
from my_car_app import Car
from stubs import CarStub


class TestMyCar(unittest.TestCase):

    # Mock constant.
    @mock.patch('my_car_app.MAX_ITEMS', 7)
    def test_constant(self):
        self.assertEqual(get_max_items(), 7)

    # Mocking a method on a class
    @mock.patch('my_car_app.Car.get_make')
    def test_method(self, mock_get_make):
        mock_get_make.return_value = 'Ford'
        self.assertEqual(get_car_make(), 'Ford')
        assert get_car_make() == 'Ford'
        mock_get_make.assert_called()

    # Mock property
    @mock.patch('my_car_app.Car.wheels', new_callable=mock.PropertyMock)
    def test_property(self, mock_wheels):
        mock_wheels.return_value = 2
        self.assertEqual(get_car_wheels(), 2)

    # Mock entire class
    @mock.patch('my_car_app.Car')
    def test_class(self, mock_car):
        mock_car.return_value = CarStub()
        self.assertEqual(get_car_make(), 'Mock car')
        self.assertEqual(get_car_wheels(), 666)

    # Mock class method
    @mock.patch('my_car_app.Car.roll_call')
    def test_class_method(self, mock_get_roll_call):
        mock_get_roll_call.return_value = [Car('Mock car'), ]
        self.assertEqual(get_roll_call(), [Car('Mock car'), ])

    # Mock side effect example
    def test_car_is_made_in_germany(self):
        with mock.patch.object(Car, 'is_car_german', side_effect=car_make_side_effect):
            car = Car()
            assert car.is_car_german('BMW')
            # check that side effect is used
            assert not car.is_car_german('Audi') # Note 'Audi' is made in Germany :)
            assert not car.is_car_german('Mock car')


def car_make_side_effect(*args):
    if args[0] == 'BMW':
        return True
    else:
        return False


if __name__ == '__main__':
    unittest.main()
