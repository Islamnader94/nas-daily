from django.http import JsonResponse
from .utils import park_car, unpark_car, slot_car_info
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


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
