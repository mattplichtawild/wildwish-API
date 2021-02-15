# Use Python3.8 image
FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Listen on port 8000
EXPOSE 8000

# Create directory for image build and set as working directory
RUN mkdir /django-wildwish
WORKDIR /django-wildwish

# Get list of required packages
RUN pip install --upgrade pip
COPY requirements.txt /django-wildwish/

# Install packages listed in requirements.txt
RUN pip install -r requirements.txt

# copy project dir
COPY . /django-wildwish/

# Run migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

CMD gunicorn app.wsgi:application --bind 0.0.0.0:8000

# copy entrypoint.sh
# Isn't this redundant since 'entrypoint.sh' is copied with the next COPY command?
# COPY ./entrypoint.sh /django-wildwish/

# run entrypoint.sh
# So many problems with trying to use these entrypoints omg
# ENTRYPOINT ["/django-wildwish/entrypoint.sh"]
# ENTRYPOINT [ "/django-wildwish/wait-for-postgres.sh" ]

# Per Django docs, don't use django server in production
# CMD python manage.py runserver 0.0.0.0:8000

# Skip using pipenv, just use pip
# RUN pip install pipenv
# COPY Pipfile Pipfile.lock

# What do these flags mean?
# --system flag will install packages into system python instead of into a virtual env (use is not recommended by pipenv)
# --deploy flag will make the build fail if Pipfile.lock is out of date
# RUN pipenv install --deploy --ignore-pipfile