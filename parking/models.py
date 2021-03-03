from django.db import models

class Car(models.Model):
    car_number = models.CharField(max_length=300)

    def __str__(self):
        return self.car_number


class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=300)
    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.slot_number
