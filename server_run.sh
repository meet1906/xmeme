#!/bin/sh

python3 xmeme/manage.py makemigrations
python3 xmeme/manage.py migrate
python3 xmeme/manage.py runserver 0.0.0.0:8081