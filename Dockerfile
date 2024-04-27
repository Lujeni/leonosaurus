# Base build
FROM python:3.11-alpine as base
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq

COPY pyproject.toml pyproject.toml
RUN pip install -e .

# Now multistage build
FROM python:3.11-alpine
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY src /app
ENV PYTHONUNBUFFERED 1
