# Pull base image
FROM python:3.11-alpine

# Set environment variables:
# PIP_DISABLE_PIP_VERSION_CHECK disables an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
# PYTHONDONTWRITEBYTECODE means Python will not try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED ensures our console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY ./requirements.txt .

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

# Copy project
COPY . .