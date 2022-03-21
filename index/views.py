from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html', {} )

def plantilla(request):
    datos = {
        'lista1': ['Información Personal', 'Estudios', 'Hobbys'],
        'nombre1': 'Nicolas Orellana',
        'apellido1': 'Orellana',

        'nombre2': 'Pablo Quiroga',
        'apellido2': 'Quiroga',
        'lista2': ['Información Personal', 'Estudios', 'Hobbys'],
    }
    return render(request, 'index/plantilla.html', datos )