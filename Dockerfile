# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /EcommerceDjangoReact/backend
COPY ./requirements.txt /EcommerceDjangoReact/backend
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["python", "manage.py", "migrate"]
COPY ./backend/frontend /backend/frontend
RUN ["npm", "install"]
RUN ["npm", "run", "build"]
COPY . /EcommerceDjangoReact