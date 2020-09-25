#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until psql "postgresql://postgres:postgres@$host:5432" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec ${cmd}

# this file was copy and pasted from https://docs.docker.com/compose/startup-order/