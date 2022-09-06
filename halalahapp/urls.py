
from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Halalah API",
        default_version='v1',
        description="Test api",
        terms_of_service="https://www.halalahapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@halalah.local"),
        license=openapi.License(name="Testing License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('discount/', include('discount.urls')),
    path('transactions/', include('transactions.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
