#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Django in the background
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000 &

# Start Celery worker
echo "Starting Celery worker..."
exec celery -A reopt_api worker --loglevel=info

# Create superuser
# python manage.py createsuperuser --noinput --username admin --email a@a.com || true
