#!/bin/bash
set -e

echo "Starting Django setup..."
python --version
pip list
echo "Running migrations..."
python manage.py migrate
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
echo "Django server started, sleeping..."
sleep infinity