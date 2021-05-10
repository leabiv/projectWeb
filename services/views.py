from django.shortcuts import render
from services.models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "services/servicios.html", {"servicios": servicios})