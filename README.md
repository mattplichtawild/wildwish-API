The easiest way to run this app is to use Docker. Make sure you have Docker installed and properly set up.

## Startup

From the root directory:

Run `docker-compose build` to build the images locally.

Run `docker-compose up` to start up the container. The app can viewed by navigating to the port in a browser ('localhost:8000')

Use 'CTRL-C' to quit the server, or run `docker-compose down` from a different shell.

## Migrations

After running the container, you may need to make migrations. 

With the container up and running, run `docker ps` in another shell.
Copy the container ID of the Django app:
```
➜  django-wildwish git:(master) ✗ docker ps
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                    NAMES
f68fda031a4a        django-wildwish_web   "python manage.py ru…"   14 seconds ago      Up 13 seconds       0.0.0.0:8000->8000/tcp   django-wildwish_web_1
b45b6309d329        postgres:12           "docker-entrypoint.s…"   3 days ago          Up 12 minutes       5432/tcp                 django-wildwish_db_1
```

Log into the container with `docker exec -t -i f68fda031a4a bash` then run `python manage.py makemigrations && python manage.py migrate`.