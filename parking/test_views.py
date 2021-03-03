import pytest
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from rest_framework.reverse import reverse
from unittest import TestCase
from parking import views
from unittest.mock import patch, Mock

class TestParkCarView(APITestCase):

    factory = APIRequestFactory()
    url = 'api/park-car'


    def setUp(self):
        self.view = views.ParkCarView().as_view()


    @patch('parking.views.park_car')
    def test__put__(self, mock_park_car):
        mock_park_car.return_value = {
            "slot_number": "P1"
        }

        data = {
            "car_number": "C123"
        }

        request = self.factory.put(
            self.url,
            data,
            format='json'
        )

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
class TestUnParkCarView(APITestCase):

    factory = APIRequestFactory()
    url = 'api/unpark-car'


    def setUp(self):
        self.view = views.UnParkCarView().as_view()


    @patch('parking.views.unpark_car')
    def test__put__(self, mock_unpark_car):
        mock_unpark_car.return_value = {
            "message": "Parking slot is ready to serve you"
        }

        data = {
            "slot_number": "P1"
        }

        request = self.factory.put(
            self.url,
            data,
            format='json'
        )

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
