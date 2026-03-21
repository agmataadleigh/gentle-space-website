#!/usr/bin/env bash
# exit on error
set -o errexit

# Add the two dots and slash here!
pip install -r ../requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate