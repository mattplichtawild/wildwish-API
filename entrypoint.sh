#!/bin/sh

# Make sure Postgres is up and healthy

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Start with a fresh db
# python manage.py flush --no-input
# python manage.py migrate

exec "$@"