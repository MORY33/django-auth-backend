from pathlib import Path
from configurations import Configuration, values
from decouple import config
import os
from oauth2_provider import settings as oauth2_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)


class BaseConfig(Configuration):
    DOTENV = os.path.join(BASE_DIR, '.env')
    SECRET_KEY = config('DJANGO_SECRET_KEY')

    CORS_ALLOW_METHODS = [
        "DELETE",
        "GET",
        "OPTIONS",
        "PATCH",
        "POST",
        "PUT",
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        },
    }

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # external modules
        'rest_framework',
        'debug_toolbar',
        'corsheaders',
        'rest_framework_swagger',
        'drf_yasg',

        # oauth
        'oauth2_provider',
        'social_django',
        'drf_social_oauth2',

        # app modules
        "custom_jwt",

        # health check
        'health_check',  # required
        'health_check.db',  # stock Django health checkers
        'health_check.cache',
        'health_check.storage',
        'health_check.contrib.migrations',
        'health_check.contrib.psutil',  # disk and memory utilization; requires psutil
    ]
    MIDDLEWARE = [
        'django_auth_backend.middleware.UnicodeEncodeErrorMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'django_auth_backend.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]


    WSGI_APPLICATION = 'django_auth_backend.wsgi.application'

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = config('TIMEZONE')

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = 'static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


class Local(BaseConfig):
    BaseConfig.MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:3000',
    ]
    SECURE_CROSS_ORIGIN_OPENER_POLICY = None

    INTERNAL_IPS = [
        '127.0.0.1',
        '192.168.0.100',
        'localhost',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
            'drf_social_oauth2.authentication.SocialAuthentication',
        ),

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 50,
    }

    AUTHENTICATION_BACKENDS = (
        # Google OAuth2
        'social_core.backends.google.GoogleOAuth2',
        'drf_social_oauth2.backends.DjangoOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    )
    # Google configuration
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

    # Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
    ]

    ACTIVATE_JWT = True

    OAUTH2_PROVIDER = {
        "ACCESS_TOKEN_GENERATOR": "custom_jwt.backends.CustomTokenGenerator",
        "REFRESH_TOKEN_GENERATOR": "custom_jwt.backends.CustomTokenGenerator",
    }

    oauth2_settings.DEFAULTS['ACCESS_TOKEN_EXPIRE_SECONDS'] = 1.577e7

    # OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = "custom_jwt.backends.CustomTokenGenerator"
    # OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL = "custom_jwt.backends.CustomTokenGenerator"





class Dev(BaseConfig):
    DEBUG = False
    ALLOWED_HOSTS = ['localhost']

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 50,
    }





