#!/bin/bash
cd app 
gunicorn app:app --log-file -
