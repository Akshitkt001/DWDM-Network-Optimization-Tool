from django.urls import path
from . import views

urlpatterns = [
    path('network-status/', views.network_status, name='network_status'),  # You can keep this if you want a specific path
]
