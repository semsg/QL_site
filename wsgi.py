"""
WSGI config for web_project_01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
project_home = u'/home/semsg/QL_site'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QL_site.settings")

application = get_wsgi_application()
