# This file contains the WSGI configuration to serve up your Django project.

import os
import sys

# Add your project's directory to the sys.path
# This is the directory that contains your 'manage.py' file.
path = '/home/StacyChege1/fitgirlstracker_api'
if path not in sys.path:
    sys.path.append(path)

# Now, import the dotenv library and load the .env file from the project directory
from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

# Set the DJANGO_SETTINGS_MODULE to your project's settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'fitgirlstracker.settings'

# Load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()