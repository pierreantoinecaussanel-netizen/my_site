import os

from django.core.wsgi import get_wsgi_application

# On dit à Django d'utiliser les réglages de ton dossier my_site
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")

application = get_wsgi_application()
