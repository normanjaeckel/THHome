# -*- coding: utf-8 -*-

"""
WSGI config.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

# import site

DJANGO_SETTINGS_MODULE = ''

# BASE_DIR = '/path/to/base_dir'
# site.addsitedir(BASE_DIR)
# site.addsitedir(os.path.join(
#     BASE_DIR, '.virtualenv', 'lib', 'python3.4', 'site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

from django.core.wsgi import get_wsgi_application  # flake8:noqa isort:skip

application = get_wsgi_application()
