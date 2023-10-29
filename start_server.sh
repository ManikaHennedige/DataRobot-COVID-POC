#!/bin/bash
# change to port 5000 when running with docker-compose
gunicorn --bind 0.0.0.0:8080 app:app