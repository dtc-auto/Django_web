"""
WSGI config for Django_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os,sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_web.settings")
#sys.path.append('C:/Users/ziruih/Desktop/Django_dev/Django_web')
#sys.path.append('C:/Users/ziruih/Anaconda2/envsmyEnv/Lib/site-packages')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
