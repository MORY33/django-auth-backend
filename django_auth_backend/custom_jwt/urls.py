from django.urls import path
from .views import ExchangeToken, RefreshToken

urlpatterns = [
    path('exchange-token/', ExchangeToken.as_view(), name='exchange-token'),
    path('refresh-token/', RefreshToken.as_view(), name='refresh-token'),
]
