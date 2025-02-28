FROM python:3.13.2-slim-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential curl

# Upgrade pip and install Poetry
RUN pip install pip --upgrade
RUN pip install poetry==2.1.1

# create app folder
RUN mkdir /app
WORKDIR /app

# install dependencies listed in poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --only main

# copy the app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Command to run when container starts
CMD ["./docker_entrypoint.sh"]
