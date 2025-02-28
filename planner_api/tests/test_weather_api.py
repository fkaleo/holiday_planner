import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from datetime import datetime

from planner_api.models import Destination
from planner_api.weather_service import WeatherData


@pytest.fixture
def api_client() -> APIClient:
    """Return an API client for testing."""
    return APIClient()


@pytest.fixture
def destination() -> Destination:
    """Create and return a test destination."""
    return Destination.objects.create(name="Rome", latitude=41.9028, longitude=12.4964)


@pytest.mark.django_db
def test_get_weather_data(api_client: APIClient, destination: Destination) -> None:
    """Test getting weather data for a destination."""
    # Use the existing destination fixture from test_views.py

    # Mock the WeatherService.fetch_weather method to avoid actual API calls
    with patch(
        "planner_api.weather_service.WeatherService.fetch_weather"
    ) as mock_fetch:
        # Configure the mock to return a predefined response
        mock_weather_data = WeatherData(
            datetime=datetime.fromisoformat("2023-01-01T12:00:00"),
            temperature=25.0,
            conditions="Sunny",
            precipitation=0.0,
        )
        mock_fetch.return_value = mock_weather_data

        # Make the API request
        url = reverse("destination-weather", kwargs={"pk": destination.pk})
        response = api_client.get(url)

        # Assert the response
        assert response.status_code == status.HTTP_200_OK
        assert response.data["temperature"] == 25.0
        assert response.data["conditions"] == "Sunny"
        assert response.data["precipitation"] == 0.0

        # Verify that the mock was called with the correct arguments
        mock_fetch.assert_called_once_with(destination)


@pytest.mark.django_db
def test_get_weather_data_service_error(
    api_client: APIClient, destination: Destination
) -> None:
    """Test handling of weather service errors."""
    # Mock the WeatherService.fetch_weather method to raise an exception
    with patch(
        "planner_api.weather_service.WeatherService.fetch_weather"
    ) as mock_fetch:
        # Configure the mock to raise an exception
        mock_fetch.side_effect = ValueError("Could not find weather data")

        # Make the API request
        url = reverse("destination-weather", kwargs={"pk": destination.pk})
        response = api_client.get(url)

        # Assert the response
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "error" in response.data
        assert "Could not find weather data" in response.data["error"]
