   #!/bin/bash
   set -e

   echo "Starting Django setup..." >&2
   python --version >&2
   pip list >&2
   echo "Running migrations..." >&2
   python manage.py migrate >&2
   echo "Starting Django server..." >&2
   python manage.py runserver 0.0.0.0:8000