from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.routers import SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Scurve django backend API",
        default_version='v1',
        description="First version of scurve django backend",
        # terms_of_service="{'terms': 'Respect everyone'}",
        contact=openapi.Contact(email="rafa.karwot@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # Oauth
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    re_path(r'^auth/', include('social_django.urls', namespace='social')),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('', include('custom_jwt.urls')),

    # Project urls

    # Management
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('health_check/', include('health_check.urls')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]