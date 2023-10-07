from django.conf import settings
from oauth2_provider import settings as oauth2_settings

# Your custom settings
DRFSO2_PROPRIETARY_BACKEND_NAME = getattr(
    settings, 'DRFSO2_PROPRIETARY_BACKEND_NAME', "Django"
)

DRFSO2_URL_NAMESPACE = getattr(settings, 'DRFSO2_URL_NAMESPACE', 'drf')

if hasattr(settings, 'ACTIVATE_JWT') and getattr(settings, 'ACTIVATE_JWT'):
    oauth2_settings.DEFAULTS[
        'ACCESS_TOKEN_GENERATOR'
    ] = 'custom_jwt.generate_token'

    oauth2_settings.DEFAULTS[
        'REFRESH_TOKEN_GENERATOR'
    ] = 'custom_jwt.generate_token'
