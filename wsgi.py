"""
WSGI config for web_project_01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
project_home = u'/media/giv/51466dba-1d41-423c-b2d0-1c9954a05cb7/Гив/Программирование/Сайты/web_project_01/QL_site'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
