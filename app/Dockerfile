# Use Python3.8 image
FROM python:3.8

# Sets dumping log messages directly to stream instead of buffering
ENV PYTHONUNBUFFERED 1

# Use pipenv to manage packages
RUN pip install pipenv

# Create project directory and use
ENV PROJECT_DIR /usr/local/src/django-wildwish

WORKDIR ${PROJECT_DIR}

# Get dependencies
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/


RUN pipenv install --system --deploy