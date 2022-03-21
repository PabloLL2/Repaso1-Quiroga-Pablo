from django.urls import path
from . import views

urlpatterns = [
    path('cerrajero/crear/', views.crear_cerrajero, name='crear_cerrajero'),
    path('cerrajeros/', views.lista_cerrajeros, name='lista_cerrajeros'),
    path('futbolistas/crear/', views.crear_futbolistas, name='crear_futbolistas'),
    path('actor/crear/', views.crear_actor, name='crear_actor'),
]