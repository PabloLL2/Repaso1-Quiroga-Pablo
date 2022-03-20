from django.urls import path
from . import views

urlpatterns = [
    path('cerrajero/crear/', views.crear_cerrajero, name='crear_cerrajero'),
    # path('',, name='buscar_cerrajero'),
]