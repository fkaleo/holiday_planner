import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
import openmeteo_requests  # type: ignore
import requests

from planner_api.models import Destination
from planner_api.weather_service import WeatherService, WeatherData


@pytest.fixture
def weather_service() -> WeatherService:
    """Return a WeatherService instance for testing."""
    return WeatherService()


@pytest.fixture
def destination() -> Destination:
    """Create and return a test destination."""
    return Destination.objects.create(name="Rome", latitude=41.9028, longitude=12.4964)


@pytest.mark.django_db
def test_fetch_weather_success(
    weather_service: WeatherService, destination: Destination
) -> None:
    """Test successful weather data fetching."""
    # Mock the openmeteo_requests.Client.weather_api method to avoid actual API calls
    with patch(
        "planner_api.weather_service.openmeteo_requests.Client.weather_api"
    ) as mock_weather_api:
        # Create a mock response object with the necessary methods and attributes
        mock_hourly = MagicMock()
        mock_hourly.VariablesLength.return_value = 3
        mock_hourly.Time.return_value = (
            1672574400  # 2023-01-01T12:00:00 in Unix timestamp
        )

        # Mock the Variables method to return objects with Values method
        temp_var = MagicMock()
        temp_var.Values.return_value = 20.5

        precip_var = MagicMock()
        precip_var.Values.return_value = 0.0

        weather_code_var = MagicMock()
        weather_code_var.Values.return_value = 0

        # Configure Variables to return different mocks based on index
        mock_hourly.Variables.side_effect = lambda i: [
            temp_var,
            precip_var,
            weather_code_var,
        ][i]

        # Create the main response mock
        mock_response = MagicMock()
        mock_response.Hourly.return_value = mock_hourly

        # Configure the weather_api to return a list with our mock
        mock_weather_api.return_value = [mock_response]

        # Call the method
        result = weather_service.fetch_weather(destination)

        # Verify the result
        assert isinstance(result, WeatherData)
        assert result.datetime == datetime.fromtimestamp(1672574400)
        assert result.temperature == 20.5
        assert result.conditions == "Clear sky"
        assert result.precipitation == 0.0

        # Verify the API was called with the correct parameters
        mock_weather_api.assert_called_once()
        args, kwargs = mock_weather_api.call_args
        assert args[0] == weather_service.base_url
        assert kwargs["params"]["latitude"] == destination.latitude
        assert kwargs["params"]["longitude"] == destination.longitude
        assert kwargs["params"]["hourly"] == [
            "temperature_2m",
            "precipitation",
            "weathercode",
        ]
        assert "start_date" not in kwargs["params"]
        assert "end_date" not in kwargs["params"]
