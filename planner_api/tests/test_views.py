import pytest
import json
from django.urls import reverse
from rest_framework import status
from planner_api.models import Destination
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    """Return an API client for testing."""
    return APIClient()


@pytest.fixture
def destination() -> Destination:
    """Create and return a test destination."""
    return Destination.objects.create(name="Rome", latitude=41.9028, longitude=12.4964)


@pytest.mark.django_db
def test_get_destination_list(
    api_client: APIClient,
    destination: Destination,
) -> None:
    """Test getting a list of destinations."""
    response = api_client.get(reverse("destination-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == destination.name
    assert response.data[0]["latitude"] == destination.latitude
    assert response.data[0]["longitude"] == destination.longitude


@pytest.mark.django_db
def test_get_destination_detail(
    api_client: APIClient,
    destination: Destination,
) -> None:
    """Test getting a single destination."""
    url = reverse("destination-detail", kwargs={"pk": destination.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == destination.name
    assert response.data["latitude"] == destination.latitude
    assert response.data["longitude"] == destination.longitude


@pytest.mark.django_db
def test_create_destination(
    api_client: APIClient,
) -> None:
    """Test creating a new destination."""
    data = {"name": "Sydney", "latitude": -33.8688, "longitude": 151.2093}
    response = api_client.post(
        reverse("destination-list"),
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Destination.objects.count() == 1
    assert response.data["name"] == data["name"]
    assert response.data["latitude"] == data["latitude"]
    assert response.data["longitude"] == data["longitude"]
