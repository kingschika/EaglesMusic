"""
deploy_wsgi_example.py

WSGI example for deploying EaglesMusic on PythonAnywhere.
This file is for convenience and documentation — edit the live WSGI file on PythonAnywhere
at /var/www/godking_pythonanywhere_com_wsgi.py instead of running this script.
"""
import os
import sys

# --- configuration for this account (change if you used different names) ---
PROJECT_HOME = '/home/godking/EaglesMusic'        # repo root on PythonAnywhere
VENV_DIR = '/home/godking/venv/eaglesmusic-venv'  # virtualenv path (adjust if different)
# ----------------------------------------

# Add project to Python path
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studio_project.settings')

# Optionally activate the virtualenv here (preferred: set virtualenv in the Web tab)
activate_this = os.path.join(VENV_DIR, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Wrap with WhiteNoise to serve static files from staticfiles
try:
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=os.path.join(PROJECT_HOME, 'staticfiles'))
except Exception:
    # If WhiteNoise isn't installed or something goes wrong, the app will still run.
    pass

if __name__ == '__main__':
    print('This file is an example WSGI snippet for PythonAnywhere. Edit the WSGI file on PA.')
