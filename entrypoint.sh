#!/bin/bash

docker compose down -v

docker compose up --build -d
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --no-input --clear
