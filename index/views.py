from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html', {} )

def plantilla(request):
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'juancho',
        'apellido': 'fort'
    }
    return render(request, 'index/plantilla.html', datos )