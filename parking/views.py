import json
import io, csv
from django.shortcuts import render
from django.http import JsonResponse
from .utils import park_car, unpark_car, slot_car_info
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.

#park a car endpoint: car number as input and add the car to db and return where it is parked. if parking slots are full, retrun error message.

# unpark a car: takes slot number where the car is parked, clears the parking for next usage

#get car/slot information: takes slot number or car number and return car number and slot number for input usage.

#if user makes more than 10 requests in 10 sec we retrun error message

# https://github.com/simonw/ratelimitcache


class ParkCarView(APIView):

    def put(self, request):
        """
        Put request to park a car in an empty parking slot.
        """
        try:
            data = request.data
            response = park_car(data)
            return JsonResponse(
                response,
                safe=False,
                status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                safe=False,
                status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return JsonResponse(
                {'error': 'Something terrible went wrong'},
                safe=False,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UnParkCarView(APIView):

    def put(self, request):
        """
        Put request to unpark a car.
        """
        try:
            data = request.data
            response = unpark_car(data)
            return JsonResponse(
                response,
                safe=False,
                status=status.HTTP_200_OK)

        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                safe=False,
                status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return JsonResponse(
                {'error': 'Something terrible went wrong'},
                safe=False,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Information(APIView):

    def get(self, request, number_type, number):
        """
        Get Request to fetch car/parking slot information.
        """
        try:
            response = slot_car_info(number_type, number)
            return JsonResponse(
                response,
                safe=False,
                status=status.HTTP_200_OK)

        except ObjectDoesNotExist as e:
            return JsonResponse(
                {'error': str(e)},
                safe=False,
                status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return JsonResponse(
                {'error': 'Something terrible went wrong'},
                safe=False,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
