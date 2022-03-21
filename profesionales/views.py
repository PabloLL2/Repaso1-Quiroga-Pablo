from django.shortcuts import render
from .models import Cerrajero
from .forms import CerrajeroFormulario

# Create your views here.

def crear_cerrajero(request):

    if request.method == 'POST': 
        form = CerrajeroFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data['nombre'], apellido=data['apellido'], desempleado=data['desempleado'])
            cerrajero.save()
            return render(request, "index/index.html", {})

    form = CerrajeroFormulario()
    return render(request, "profesionales/crear_cerrajero.html", {'form': form})