
import os

# from django.core.asgi import get_asgi_application
from configurations.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth_backend.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_asgi_application()
