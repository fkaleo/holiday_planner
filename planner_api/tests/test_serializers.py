import pytest
from planner_api.models import Destination
from planner_api.serializers import DestinationSerializer


@pytest.fixture
def destination_berlin() -> Destination:
    """Create and return a Berlin destination for serializer tests."""
    return Destination.objects.create(
        name="Berlin", latitude=52.5200, longitude=13.4050
    )


@pytest.mark.django_db
def test_contains_expected_fields(destination_berlin: Destination) -> None:
    """Test that serializer contains expected fields."""
    serializer = DestinationSerializer(instance=destination_berlin)
    data = serializer.data
    assert set(data.keys()) == {"id", "name", "latitude", "longitude"}


@pytest.mark.django_db
def test_create_destination() -> None:
    """Test creating a destination with the serializer."""
    destination_data = {"name": "Berlin", "latitude": 52.5200, "longitude": 13.4050}
    serializer = DestinationSerializer(data=destination_data)
    assert serializer.is_valid()
    destination = serializer.save()
    assert destination.name == destination_data["name"]
    assert destination.latitude == destination_data["latitude"]
    assert destination.longitude == destination_data["longitude"]


@pytest.mark.django_db
def test_update_destination(destination_berlin: Destination) -> None:
    """Test updating a destination with the serializer."""
    update_data = {"name": "Updated Berlin", "latitude": 52.5201, "longitude": 13.4051}
    serializer = DestinationSerializer(instance=destination_berlin, data=update_data)
    assert serializer.is_valid()
    destination = serializer.save()
    assert destination.name == update_data["name"]
    assert destination.latitude == update_data["latitude"]
    assert destination.longitude == update_data["longitude"]
