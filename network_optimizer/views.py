from django.shortcuts import render
from .models import Path

def network_status(request):
    paths = Path.objects.all().prefetch_related('links', 'wavelength')
    return render(request, 'network_optimizer/network_status.html', {'paths': paths})
