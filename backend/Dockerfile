FROM python:3.9.6-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backend

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /backend/
