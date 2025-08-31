import os
import sys

# Add your project directory to the sys.path
path = 'https://www.pythonanywhere.com/user/StacyChege1/files/home/StacyChege1/fitgirlstracker_api'
if path not in sys.path:
    sys.path.insert(0, path)

# Set up the Django project environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fitgirlstracker_api.settings'

# Activate your virtual environment
activate_this = '/home/StacyChege1/fitgirlstracker_api/venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()