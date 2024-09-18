   #!/bin/sh
   echo "Starting Celery worker..."
   celery -A reopt_api worker --loglevel=info