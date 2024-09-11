from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('network_optimizer.urls')),  # This maps the root URL to network_optimizer.urls
]
