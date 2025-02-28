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
python manage.py makemigrations
python manage.py migrate
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