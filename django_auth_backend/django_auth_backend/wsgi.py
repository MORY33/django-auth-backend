import os

# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth_backend.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
