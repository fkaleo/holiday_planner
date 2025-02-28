from rest_framework import serializers

from .models import Destination, Trip, TripStop


class DestinationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Destination model.
    """

    class Meta:
        model = Destination
        fields = ["id", "name", "latitude", "longitude"]


class WeatherDataSerializer(serializers.Serializer):
    """Serializer for weather data."""

    datetime = serializers.DateTimeField()
    temperature = serializers.FloatField()
    conditions = serializers.CharField()
    precipitation = serializers.FloatField()


class TripStopSerializer(serializers.ModelSerializer):
    """
    Serializer for the TripStop model.
    """

    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Destination.objects.all(), write_only=True, source="destination"
    )

    class Meta:
        model = TripStop
        fields = [
            "id",
            "destination",
            "destination_id",
            "arrival_datetime",
            "departure_datetime",
            "trip",
        ]


class TripSerializer(serializers.ModelSerializer):
    """
    Serializer for the Trip model.
    """

    trip_stops = TripStopSerializer(many=True, read_only=True, source="tripstop_set")

    class Meta:
        model = Trip
        fields = ["id", "start_datetime", "end_datetime", "trip_stops"]
