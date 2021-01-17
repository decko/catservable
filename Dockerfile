FROM bitnami/python:3.9-debian-10 AS python-builder

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install poetry
RUN apt update && apt install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    netcat

WORKDIR /app
COPY . /app
RUN poetry config virtualenvs.in-project true && poetry install --no-dev
