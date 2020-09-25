# Use Python3.8 image
FROM python:3.8

# Sets dumping log messages directly to stream instead of buffering
# I don't even know what this means or if I need to do it
# ENV PYTHONUNBUFFERED 1

# Use pipenv to manage packages
RUN pip install pipenv

# Create environment variables
# These lines copied from tutorial before I knew what I was doing
# ENV PROJECT_DIR /usr/local/src/django-wildwish
# WORKDIR ${PROJECT_DIR}

# Set DEBUG to 0 so pipenv install doesn't return a non zero?
ENV DEBUG 0

# Set working directory to code directory (alt. method to above)
WORKDIR /app

# Get dependencies
COPY Pipfile Pipfile.lock

# What do these flags mean?
RUN pipenv install --system --deploy