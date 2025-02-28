import requests
import pytest
from pytest_docker.plugin import Services
from typing import List

import os

# Mark all tests in this file with the 'docker' marker
pytestmark = pytest.mark.docker


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: pytest.Config) -> str:
    """Path to the docker-compose file for testing the Dockerfile."""
    return os.path.join(
        str(pytestconfig.rootpath), "tests", "docker", "docker-compose.yml"
    )


@pytest.fixture(scope="session")
def docker_cleanup() -> List[str]:
    """
    Override the default docker_cleanup fixture to add the --rmi flag.
    This will remove images when cleaning up after tests.
    """
    return ["down -v --rmi local"]


def is_responsive(url: str) -> bool:
    """Check if the service is responsive."""
    try:
        response = requests.get(f"{url}/admin/", timeout=1)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


@pytest.fixture(scope="session")
def django_service(docker_ip: str, docker_services: Services) -> str:
    """Ensure that Django service is up and responsive."""
    port = docker_services.port_for("django_test", 8000)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


def test_container_running(django_service: str) -> None:
    """Test that the container is running."""
    # If django_service is available, the container is running
    assert django_service


def test_django_admin_page(django_service: str) -> None:
    """Test that the Django admin page is accessible."""
    response = requests.get(f"{django_service}/admin/")
    assert response.status_code == 200
    assert "Django administration" in response.text


def test_health_endpoint(django_service: str) -> None:
    """Test a basic health endpoint."""
    try:
        response = requests.get(django_service)
        assert response.status_code in (
            200,
            302,
            404,
        )  # Allow various responses for homepage
    except requests.RequestException as e:
        pytest.fail(f"Request to homepage failed: {e}")
