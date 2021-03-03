import pytest
from unittest import TestCase
from parking import utils
from unittest.mock import patch, Mock

@pytest.mark.django_db
class TestUtils(TestCase):

    @patch('parking.utils.park_car')
    def test_park_car(self, mock_park_car):
        """
        Test park car function.
        """
        mock_park_car.return_value.json.return_value = {"slot_number": "P1"}
        data = {"car_number": "C123"}
        resp = utils.park_car(data)
        self.assertEqual(
            resp.json(),
            mock_park_car.return_value.json.return_value
        )

    @patch('parking.utils.unpark_car')
    def test_unpark_car(self, mock_unpark_car):
        """
        Test unpark car function.
        """
        mock_unpark_car.return_value.json.return_value = {"message": "Parking slot is ready to serve you"}
        data = {"slot_number": "P1"}
        resp = utils.unpark_car(data)
        self.assertEqual(
            resp.json(),
            mock_unpark_car.return_value.json.return_value
        )

    @patch('parking.utils.slot_car_info')
    def test_slot_car_info(self, mock_slot_car_info):
        """
        Test slot_car_info function.
        """
        mock_slot_car_info.return_value.json.return_value = {
            "car_number" : "C123",
            "slot_number" : "P1"
        }
        number_type = "car"
        number = "C123"

        resp = utils.slot_car_info(number_type, number)
        self.assertEqual(
            resp.json(),
            mock_slot_car_info.return_value.json.return_value
        )
