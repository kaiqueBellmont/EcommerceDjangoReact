# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /EcommerceDjangoReact/backend
COPY ./requirements.txt /EcommerceDjangoReact/backend
RUN ["pip", "install", "-r", "requirements.txt"]
COPY . /EcommerceDjangoReact