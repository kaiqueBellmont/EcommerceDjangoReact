#!/bin/bash -x

# back
cd backend/ && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt &&
python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py createsuperuser &&
python3 manage.py runserver 8000

# front
cd ./frontend && npm install --legacy-peer-deps && npm start

