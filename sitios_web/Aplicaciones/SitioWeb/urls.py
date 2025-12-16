from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listado_sitios, name='index'),

    path('nuevo_sitio/', views.nuevo_sitio, name='nuevo_sitio'),
    path('guardar_sitio/', views.guardar_sitio, name='guardar_sitio'),
    path('editar_sitio/<int:id>/', views.editar_sitio, name='editar_sitio'),
    path('edicion_sitio/', views.edicion_sitio, name='edicion_sitio'),
    path('eliminar_sitio/<int:id>/', views.eliminar_sitio, name='eliminar_sitio'),

    path('tecnologias/', views.listado_tecnologias, name='listado_tecnologias'),
    path('nueva_tecnologia/', views.nueva_tecnologia, name='nueva_tecnologia'),
    path('guardar_tecnologia/', views.guardar_tecnologia, name='guardar_tecnologia'),
    path('editar_tecnologia/<int:id>/', views.editar_tecnologia, name='editar_tecnologia'),
    path('edicion_tecnologia/', views.edicion_tecnologia, name='edicion_tecnologia'),
    path('eliminar_tecnologia/<int:id>/', views.eliminar_tecnologia, name='eliminar_tecnologia'),
]

