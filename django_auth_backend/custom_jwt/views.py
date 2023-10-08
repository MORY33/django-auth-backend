from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from decouple import config

class ExchangeToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        print(code)
        token_endpoint = "http://localhost:8000/auth/convert-token/"
        payload = {
            "grant_type": "convert_token",
            "client_id": config('DJANGO_CLIENT_ID'),
            "client_secret": config('DJANGO_CLIENT_SECRET'),
            "token": code,
            "backend": "google-oauth2"

        }

        response = requests.post(token_endpoint, data=payload)
        data = response.json()
        # print(data)

        if "error" in data:
            return Response({"error": data["error"]})

        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        return Response({
            "access_token": access_token,
            "refresh_token": refresh_token
        })

class RefreshToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        print(refresh_token)
        token_endpoint = "http://localhost:8000/auth/token"
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": config('DJANGO_CLIENT_ID'),
            "client_secret": config('DJANGO_CLIENT_SECRET'),
        }

        response = requests.post(token_endpoint, data=payload)
        data = response.json()
        print(data)

        if "error" in data:
            return Response({"error": data["error"]})

        return Response(data)


class Test(APIView):
    def get(self, request, *args, **kwargs):
        # print(request.META)
        print(request.user)
        return Response({"in": "get"})

