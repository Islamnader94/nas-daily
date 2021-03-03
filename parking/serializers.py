from rest_framework import serializers
from .models import Car, ParkingSlot
from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ['slot_number']
