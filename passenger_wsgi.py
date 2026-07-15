import os
import sys

# Ajouter le répertoire du projet au PATH
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(os.path.join(cwd, 'itss'))

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itss.settings')

# Charger l'application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()