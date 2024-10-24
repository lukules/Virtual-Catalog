from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/account/', include('account.urls')),
    path('api/vehicles/', include('vehicles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
