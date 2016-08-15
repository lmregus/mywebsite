#!/bin/bash
cd flask
gunicorn app:app --log-file -
