#!/bin/bash -x


cd ./backend && python3 -m venv venv && pip install -r requirements.txt && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py createsuperuser && python3 manage.py runserver 8000

