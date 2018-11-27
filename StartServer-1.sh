#!/usr/bin/env bash
cd server2  ;python3 manage.py runserver ; cd ../server1 ; python3 manage.py runserver
