#!/bin/bash

python challenge/manage.py migrate
python challenge/manage.py loaddata towns_data.json
python challenge/manage.py runserver
