#!/usr/bin/env python

import os
import sys

# Add your project directory to sys.path
path = '/home/yourusername/travel_project'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_project.production_settings'

# Import Django and setup
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
