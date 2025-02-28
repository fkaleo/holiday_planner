from rest_framework import serializers

from .models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Destination model.
    """

    class Meta:
        model = Destination
        fields = ["id", "name", "latitude", "longitude"]
