   #!/bin/bash
   set -e

   exec > /opt/reopt/django_startup.log 2>&1

   echo "Starting Django setup..."
   python --version
   pip list
   echo "Running migrations..."
   python manage.py migrate
   echo "Starting Django server..."
   python manage.py runserver 0.0.0.0:8050