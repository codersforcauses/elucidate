#!/bin/bash

echo "████ ${APP_NAME^^} - DJANGO CONTAINER STARTING... ████████████████████████████████████"
figlet $APP_NAME

# .Debug / Sanity check info
echo "Current Dir / Files (Debug)" | boxes -d shell -p a1l2
pwd
ls -al

printf "\n" && echo "Python Path & Version (Debug)" | boxes -d shell -p a1l2
which python
python -V


# Setup everytime it runs

# Migrate database
printf "\n" && echo "Running django database migrations" | boxes -d shell -p a1l2
python manage.py migrate --noinput

# Create Django Superuser
printf "\n" && echo "Creating Django Superuser" | boxes -d shell -p a1l2
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

printf "\n" && echo "MIGRATION & SETUP TASK COMPLETED" | boxes -d dog -a c

# Run inbuilt Django server if ENV is development
if [ "${APP_ENV^^}" = "DEVELOPMENT" ]; then

    # Install extra non-prod packages
    printf "\n" && echo "Installing dev dependencies for $APP_ENV" | boxes -d shell -p a1l2
    poetry install

    # Run developments
    printf "\n" && echo "Starting inbuilt django webserver" | boxes -d shell -p a1l2
    echo "Running: python manage.py runserver 0.0.0.0:8081"
    python manage.py runserver 0.0.0.0:8081
    exit
fi

# ===================
# Run Django/Gunicorn
# ===================
if [ "${APP_ENV^^}" = "PRODUCTION" ]; then

    # Run Gunicorn / Django
    printf "\n" && echo " Running Gunicorn / Django" | boxes -d shell -p a1l2
    echo "Running: gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --access-logfile=/var/log/accesslogs/gunicorn --capture-output --timeout 50"
    # gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --access-logfile=/var/log/accesslogs/gunicorn --capture-output --timeout 50
    gunicorn api.wsgi -b 0.0.0.0:8081
fi