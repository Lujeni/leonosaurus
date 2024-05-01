FROM python:3.11-buster

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=True \
    POETRY_VIRTUALENVS_IN_PROJECT=False \
    POETRY_VIRTUALENVS_CREATE=False \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md
RUN poetry install --without test --no-root && rm -rf $POETRY_CACHE_DIR
