from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .models import Destination
from .serializers import (
    DestinationSerializer,
    WeatherDataSerializer,
)
from .weather_service import WeatherService


class DestinationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows destinations to be viewed or edited.
    """

    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=True, methods=["get"])
    def weather(self, request: Request, pk: int) -> Response:
        """Get weather data for a destination."""
        destination = self.get_object()

        # Fetch the weather data
        weather_service = WeatherService()
        try:
            weather_data = weather_service.fetch_weather(destination)

            # Serialize and return the weather data
            serializer = WeatherDataSerializer(weather_data)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"error": "Failed to fetch weather data", "detail": str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
