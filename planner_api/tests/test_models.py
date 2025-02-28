import pytest
from planner_api.models import Destination
from typing import Dict, Any


@pytest.fixture
def paris_data() -> Dict[str, Any]:
    """Return data for a Paris destination."""
    return {
        "name": "Paris",
        "latitude": 48.8566,
        "longitude": 2.3522
    }


@pytest.mark.django_db
def test_destination_creation(paris_data: Dict[str, Any]) -> None:
    """Test creating a destination instance."""
    destination = Destination.objects.create(**paris_data)
    assert destination.name == "Paris"
    assert destination.latitude == 48.8566
    assert destination.longitude == 2.3522
    assert str(destination) == "Paris"
