from django.urls import path
from .views import index, plantilla, mi_login,registrarse
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', index, name='index'),
    path('login/', mi_login, name='login'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='index/logout.html') , name='logout'),
    path('plantilla/', plantilla, name='plantilla')
]