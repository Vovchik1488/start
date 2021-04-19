"""
ASGI config for myfirst project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.adspath(__file__)))

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, _'apps'_))

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirst.settings')

application = get_asgi_application()
