from django.urls import path
from .views import ExchangeToken, RefreshToken, Test

urlpatterns = [
    path('exchange-token/', ExchangeToken.as_view(), name='exchange-token'),
    path('refresh-token/', RefreshToken.as_view(), name='refresh-token'),
    path('test-auth/', Test.as_view(), name='test'),
]
