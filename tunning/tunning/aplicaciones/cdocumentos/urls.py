from django.contrib import admin
from django.urls import path
from . import views

app_name ="cdocumentos_app"


urlpatterns = [
    path('',
         views.Inicio_vista.as_view(), 
         name='inicio'
         ),
       
    path('list_proyectos/<int:codjp>',
        views.Detalle_Proyecto.as_view(),
        name='proyecto_asignado'),
    
    path('ing-proyectos-asig/',
         views.RegistrarProyectoPersonaView.as_view(),
        name='ing_proyecto'),
    
    path('list_proyectos_registrados/<int:pk>/', 
         views.consulta_proyecto_registrado.as_view(),
         name='proyecto_registrados'),
    
    #path('carga_listado_entregable/', views.ListaEntregables.as_view(), name='carga_listado_entregable'),
    
    path('carga_listado_entregable/', views.show_excel_table, name='cargar_excel'),
]