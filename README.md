# README

## Django-drf-docker-project

This is a template project built with Django, Django Rest Framework, and Docker. It provides a starting point for developing web applications using these technologies

## Stack

- Django: A high-level Python web framework that follows the model-view-controller (MVC) architectural pattern.
- Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs based on Django.
- Docker: A platform that allows developers to build, package, and distribute applications as lightweight containers.

### Prerequisites

Make sure you have the following software installed before running the project:

- Python 3.x
- Docker Desktop

## Features

This project its not just a django with docker implementation, it has some other implemented features like:

1. CustomPagination,
2. Authentication with rest-framework and JWT (in progress),
3. Bitbucket Pipeline (in progress),

## How do I get set up?

You can start the project running this easy commands:

```bash
$ docker build .
$ docker compose up
```

### Useful commands:

- Migrations:

  ```bash
  docker-compose run --rm app python manage.py makemigrations
  ```

  ```bash
  docker-compose run --rm app python manage.py migrate
  ```

  ```bash
  docker-compose run --rm app python manage.py migrate app-name migration-to-reverse
  ```

- Super user:

  ```bash
  docker-compose run --rm app python manage.py createsuperuser
  ```

- New app:

  ```bash
  docker-compose run --rm app python manage.py startapp <app_name> project_apps
  ```
