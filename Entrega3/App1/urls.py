from django.urls import path 
from App1 import views 

urlpatterns = [
     path('', views.inicio, name="Inicio"),
     path('Contactos', views.contactosFormulario, name="Contactos"),
     path('Sugerencias', views.sugerenciaFormulario, name="Sugernecias"),
     path('Calificacion', views.calificacionFormulario, name="Calificacion"),
     path('getCalificacion', views.getCalificaciones, name="getCalificacion"),
]