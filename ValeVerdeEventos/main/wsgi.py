"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import signal
import sys
import traceback
import time

from django.core.wsgi import get_wsgi_application

from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
