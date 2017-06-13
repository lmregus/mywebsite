#!/bin/bash
cd app
python migration.py db upgrade
gunicorn app:app --log-file -
