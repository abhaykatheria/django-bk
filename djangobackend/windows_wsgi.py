"""
WSGI config for djangobackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir("C:/Users/abhay/AppData/Local/Programs/Python/Python37-32/Lib/site-packages")

sys.path.append('C:/Users/abhay/Desktop/oneML/new/OneML/djangobackend') 
sys.path.append('C:/Users/abhay/Desktop/oneML/new/OneML/djangobackend/djangobackend')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobackend.settings')

application = get_wsgi_application()
