"""
Configuración ASGI para el proyecto config.

Expone el callable de ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, ver:
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
