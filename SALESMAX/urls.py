from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SETTINGS.urls')),
    path('', include('HUMANRESOURCE.urls')),
    path('', include('PURCHASE.urls')),
    path('', include('SALES.urls')),
    path('', include('WAREHOUSE.urls')),
]
