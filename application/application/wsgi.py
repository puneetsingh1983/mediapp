"""
WSGI config for application project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

sys.path.append(r'/home/kashyap41_lm/virtualenvs/mediapp/')
sys.path.append(r'/home/kashyap41_lm/mediapp/application/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

application = get_wsgi_application()
