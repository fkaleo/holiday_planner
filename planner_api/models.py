from django.db import models


class Destination(models.Model):
    """
    Destination model representing a travel destination with a name and coordinates.
    """

    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return self.name
