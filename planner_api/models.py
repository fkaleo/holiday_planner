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


class TripStop(models.Model):
    """
    TripStop model representing a stop in a trip with arrival and departure times
    and destination.
    """

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    arrival_datetime = models.DateTimeField()
    departure_datetime = models.DateTimeField()
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.destination} ({self.arrival_datetime.strftime('%Y-%m-%d')})"


class Trip(models.Model):
    """
    Trip model representing a complete trip with multiple stops and overall start/end times.
    """

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f"Trip {self.id}: {self.start_datetime.strftime('%Y-%m-%d')} to {self.end_datetime.strftime('%Y-%m-%d')}"

    @property
    def trip_stops(self) -> models.QuerySet["TripStop"]:
        """
        Return all trip stops associated with this trip.
        """
        return self.tripstop_set.all().order_by("arrival_datetime")
