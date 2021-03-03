from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

LOT_SIZE = settings.LOT_SIZE

class Car(models.Model):
    car_number = models.CharField(max_length=300)

    def __str__(self):
        return self.car_number


class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=300)
    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.slot_number

    def save(self, *args, **kwargs):
        if ParkingSlot.objects.count() < int(LOT_SIZE):
            return super(ParkingSlot,self).save(*args,**kwargs)

        raise ValidationError("Too many records for parking slots")
