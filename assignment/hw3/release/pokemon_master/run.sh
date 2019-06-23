#!/usr/bin/env bash
cd /home/pokemon_coin && gunicorn --bind 0.0.0.0:5000 --workers 8 --access-logfile - --error-logfile - server:app
