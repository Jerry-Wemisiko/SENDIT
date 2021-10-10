from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name