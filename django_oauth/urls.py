from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]
