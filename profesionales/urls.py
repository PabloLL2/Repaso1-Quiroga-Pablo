from django.urls import path
from . import views

urlpatterns = [
    path('cerrajeros/', views.lista_cerrajeros, name='cerrajeros'),
    path('cerrajeros/crear/', views.crear_cerrajero, name='crear_cerrajero'),
    path('cerrajeros/<int:pk>', views.DetalleCerrajero.as_view(), name='detalle_cerrajero'),
    path('cerrajeros/<int:pk>/editar', views.EditarCerrajero.as_view(), name='editar_cerrajero'),
    path('cerrajeros/<int:pk>/borrar', views.BorrarCerrajero.as_view(), name='borrar_cerrajero'),



    path('futbolistas/crear/', views.crear_futbolistas, name='crear_futbolistas'),
    path('actor/crear/', views.crear_actor, name='crear_actor'),
]