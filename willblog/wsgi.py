"""
WSGI config for willblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/willblog')

os.environ['PYTHON_EGG_CACHE'] = '/tmp/python_eggs'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "willblog.settings")

application = get_wsgi_application()
