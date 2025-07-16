#!/bin/bash

# Install dependencies (optional if Render already does this)
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput
