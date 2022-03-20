from django.shortcuts import render
from .forms import CerrajeroFormulario

# Create your views here.

def crear_cerrajero(request):
    form = CerrajeroFormulario()
    return render(request, "profesionales/crear_cerrajero.html", {'form': form})