#!/bin/sh
set -e

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

# Start server
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000