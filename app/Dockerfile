# Use Python3.8 image
FROM python:3.8

# Sets dumping log messages directly to stream instead of buffering
# I don't even know what this means or if I need to do it
# ENV PYTHONUNBUFFERED 1

# Use pipenv to manage packages
RUN pip install pipenv

# Create project directory and use
# ENV PROJECT_DIR /usr/local/src/django-wildwish

# WORKDIR ${PROJECT_DIR}

# Set working directory to code directory (alt. method to above)
WORKDIR /app

# Get dependencies
COPY Pipfile ../django-wildwish/Pipfile.lock

# What do these flags mean?
RUN pipenv install --system --deploy