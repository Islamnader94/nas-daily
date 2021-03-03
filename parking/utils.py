from .models import Car, ParkingSlot
from .serializers import CarSerializer, ParkingSlotSerializer
from django.shortcuts import get_object_or_404
from django.conf import settings


LOT_SIZE = settings.LOT_SIZE
FIRST_TYPE = settings.FIRST_TYPE
SECOND_TYPE = settings.SECOND_TYPE

# don't forget to check if parking is already occupied.

def check_lot_size(size):
    if size > int(LOT_SIZE):
        return True
    else:
        return False


def park_car(data):
    response = None
    car = get_object_or_404(Car, car_number=data['car_number'])
    slot = ParkingSlot.objects.filter(car__isnull=True)
    car_parked = ParkingSlot.objects.filter(car=car)
    slot_count = ParkingSlot.objects.count()
    size = check_lot_size(slot_count)

    if not size:
        if slot and not car_parked:
            slot[0].car = car
            slot_serializer = ParkingSlotSerializer(slot[0])
            response = slot_serializer.data
        else:
            response = {
                "message": "Car already parked!"
            }
    else:
        response = {
            "message": "We are sorry, the parking lot is full"
        }

    return response


def unpark_car(data):
    response = None
    slot = get_object_or_404(ParkingSlot, slot_number=data['slot_number'])

    if slot.car:
        slot.car = None
        slot.save()
        response = {
            "message": "Parking slot is ready to serve you"
        }
    else:
        response = {
            "message": "Parking slot is already empty!"
        }
    return response


def slot_car_info(number_type, number):
    slot = None
    car = None

    response = {
        "car_number" : "",
        "slot_number" : ""
    }

    if number_type == FIRST_TYPE:
        car = Car.objects.get(car_number=number)
        slot = ParkingSlot.objects.filter(car=car)
        if slot:
            slot = slot[0]
    elif number_type == SECOND_TYPE:
        slot = ParkingSlot.objects.get(slot_number=number)
        if slot.car:
            car = Car.objects.get(car_number=slot.car.car_number) 
    else:
        return {
            "message": "Please specify a number type(car or slot)"
        }

    if car:
        response['car_number'] = car.car_number
    if slot:
        response['slot_number'] = slot.slot_number

    return response
