FROM python:3.8-slim

WORKDIR /app

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install pipenv -y \
    && apt-get clean

COPY ./Pipfile .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --skip-lock --system --dev

COPY . /app/
