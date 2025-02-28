import openmeteo_requests  # type: ignore
from datetime import datetime
from typing import Dict, Any, List
from dataclasses import dataclass

from .models import Destination


@dataclass
class WeatherData:
    """Weather data for a specific location and time."""

    datetime: datetime
    temperature: float
    conditions: str  # e.g., "Sunny", "Rainy"
    precipitation: float


class WeatherService:
    """Service for fetching weather data for destinations using the Open-Meteo API."""

    def __init__(self) -> None:
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        # Map WMO weather codes to human-readable conditions
        # Source: https://open-meteo.com/en/docs
        self.wmo_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }

    def fetch_weather(
        self, destination: Destination
    ) -> WeatherData:
        """
        Fetch weather data for a destination using the Open-Meteo API.

        Args:
            destination: The destination to fetch weather for.

        Returns:
            WeatherData: Weather data for the destination (first hour of forecast).
        """
        # Setup the Open-Meteo API client
        openmeteo = openmeteo_requests.Client()

        # Open-Meteo API parameters
        params: Dict[str, Any] = {
            "latitude": destination.latitude,
            "longitude": destination.longitude,
            "hourly": ["temperature_2m", "precipitation", "weathercode"],
            "timezone": "auto",
        }

        # Make the API request
        responses = openmeteo.weather_api(self.base_url, params=params)
        
        # Process the response (first location)
        response = responses[0]
        
        # Process hourly data
        hourly = response.Hourly()
        
        # Check if we have any data
        if hourly.VariablesLength() == 0:
            raise ValueError("No forecast data available")
        
        # Get the timestamp for the first hour
        timestamp = hourly.Time()
        datetime_obj = datetime.fromtimestamp(timestamp)
        
        # Get all variables
        hourly_variables = [hourly.Variables(i) for i in range(hourly.VariablesLength())]
        
        # Find the specific variables we need
        # The order is the same as in the request: temperature_2m, precipitation, weathercode
        temperature_var = hourly_variables[0]
        precipitation_var = hourly_variables[1]
        weathercode_var = hourly_variables[2]
        
        # Get the values for the first hour (index 0)
        temperature = float(temperature_var.Values(0))
        precipitation = float(precipitation_var.Values(0))
        weather_code = int(weathercode_var.Values(0))
        
        # Convert weather code to human-readable condition
        conditions = self.wmo_codes.get(weather_code, "Unknown")
        
        return WeatherData(
            datetime=datetime_obj,
            temperature=temperature,
            conditions=conditions,
            precipitation=precipitation,
        )
