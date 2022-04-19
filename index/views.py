from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from forms import NuestroUserForm

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

def mi_login(request):
    msj = ''
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msj = 'El Usuario no es valido.'
                #return render(request, 'index/login.html', {'login_form': login_form, 'msj': 'El Usuario no es valido.'})    
        else:
            #return render(request, 'index/login.html', {'login_form': login_form, 'msj': 'El formulario no es valido.'})
            msj= 'El Formulario no es valido.'
    
    login_form = AuthenticationForm()
    return render(request, 'index/login.html', {'login_form': login_form, 'msj': msj})

def registrarse(request):

    if request.method == 'POST':
        form = NuestroUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save
            return render(request, 'index/index.html', {'msj': f'Se creo con exito el usuario. {username}'})
            

    form = NuestroUserForm
    return render(request, 'index/registrarse.html', {'form': form})