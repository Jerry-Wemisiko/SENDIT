from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

transit_status = [
    ("In Transit", "In Transit"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled")
]

load_sizes = [
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large")
]


class Location(models.Model):
    name = models.CharField(max_length=100, null=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(null=False)
    phonenumber = models.CharField(max_length=100, null=False)
    address = models.ForeignKey(Location, null=True, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='orders')
    load_size = models.CharField(choices=load_sizes, max_length=50, null=False)
    start_location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE, related_name='start_location')
    destination_location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE,
                                             related_name='destination_location')
    pickup_time = models.DateTimeField(default=timezone.now)
    price = models.DecimalField( max_digits=15, decimal_places=2, null=True)
    description = models.TextField(null=False)
    transit_status = models.CharField(choices=transit_status, default='In Transit', max_length=100)
    created_at = models.DateTimeField(default=timezone.now)



