# Holiday Planner

A Django-based application for planning your holidays with ease.

## Technology Stack

- Python
- Django
- Django REST Framework
- Poetry for dependency management

## Getting Started

### Setup

Make sure you have all dependencies installed:
```
poetry install --no-root
```

### Database Migrations

To initialize or update your database schema:
```
python manage.py migrate
```

### Populating the Database

To populate the database with sample data:
```
python manage.py shell < planner_api/scripts/populate.py
```

### Running the Server

To start the development server:
```
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Running Tests

Run the tests:
```
pytest
```

## Adding Content via Django Admin

To access the Django admin interface, you first need to create a superuser account:

```
python manage.py createsuperuser
```

Navigate to http://127.0.0.1:8000/admin in your web browser

## API Endpoints

### Destinations API

The application provides a RESTful API for managing travel destinations.

#### Base URL

```
/api/destinations/
```

#### Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/destinations/` | GET | List all destinations |
| `/api/destinations/` | POST | Create a new destination |
| `/api/destinations/{id}/` | GET, PUT, DELETE | Standard CRUD operations for a specific destination |
| `/api/destinations/{id}/weather/` | GET | Get weather data for a specific destination |

#### Destination Object

```json
{
  "id": 1,
  "name": "Paris",
  "latitude": 48.8566,
  "longitude": 2.3522
}
```

#### Weather Data Response

```json
{
  "datetime": "2025-02-28T14:00:00Z",
  "temperature": 18.5,
  "conditions": "Partly Cloudy",
  "precipitation": 0.0
}
```
