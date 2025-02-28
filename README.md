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

The application will be available at http://127.0.0.1:8000/api/

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

The Holiday Planner API is built using Django REST Framework and provides the following main resources:

- **Destinations**: Manage travel locations with coordinates
- **Trips**: Create and manage complete trips with start and end dates
- **Trip Stops**: Manage individual stops within a trip, including arrival and departure times

Each resource supports standard RESTful operations (GET, POST, PUT, DELETE) and follows consistent URL patterns.


## Running with Docker

This will spin up a Docker container with the application running and a Postgres database.

```
# Build and start the containers
docker compose up --build
```

Access the application at http://127.0.0.1:8000
