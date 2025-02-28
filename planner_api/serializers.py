from rest_framework import serializers

from .models import Destination


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
