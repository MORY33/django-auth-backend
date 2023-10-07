from oauth2_provider.models import AccessToken
from oauth2_provider.settings import oauth2_settings
from django.db import models
# from django.conf import settings
from oauth2_provider.models import AbstractAccessToken
from django_auth_backend import settings


#
# class CustomAccessToken(AbstractAccessToken):
#
#     def generate_token(self):
#         # Generate the token as usual
#         token = super().generate_token()
#
#         # Add custom claims to the token payload
#         token['user_id'] = self.user.id
#         # Add more custom claims as needed
#
#         return token