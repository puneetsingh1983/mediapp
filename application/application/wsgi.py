"""
WSGI config for application project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys


path_name = "/home/ec2-user/myspace/mediapp/application"
if path_name not in sys.path:
    sys.path.append(path_name)

os.environ['DJANGO_SETTINGS_MODULE'] = 'application.settings'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

application = get_wsgi_application()
