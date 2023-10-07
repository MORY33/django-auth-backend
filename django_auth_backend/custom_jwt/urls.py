from django.urls import path
from .views import ExchangeToken

urlpatterns = [
    path('exchange-token/', ExchangeToken.as_view(), name='exchange-token'),
]
