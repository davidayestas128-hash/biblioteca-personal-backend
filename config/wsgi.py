"""
Configuración WSGI para el proyecto config.

Expone el callable de WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, ver:
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
