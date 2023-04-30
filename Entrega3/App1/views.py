from django.shortcuts import render
from App1.models import Contactos,Sugerencias,Calificacion
from django.http import HttpResponse
from App1.forms import ContactosFormulario,CalificacionFormulario,SugerenciaFormulario

def inicio(request):
    return render(request,'App1/inicio.html')

def contactos(request):
    return render(request,'App1/contacto.html')

def sugerencias(request):
    return render(request,'App1/sugerencias.html')

def calificacion(request):
    return render(request,'App1/calificacion.html')
	
def contactosFormulario(request):
     if request.method == "POST":
        miFormulario = ContactosFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            contac = Contactos(nombre=informacion['nombre'],email=informacion['email'],telefono=informacion['telefono'])
            contac.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ContactosFormulario()
             
     return render(request, "App1/contacto.html", {"miFormulario": miFormulario})

def calificacionFormulario(request):
     if request.method == "POST":
        miFormulario = CalificacionFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            contac = Calificacion(calificacion=miFormulario.cleaned_data['calificacion'])
            contac.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = CalificacionFormulario()
             
     return render(request, "App1/calificacion.html", {"miFormulario": miFormulario})

def sugerenciaFormulario(request):
     if request.method == "POST":
        miFormulario = SugerenciaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            contac = Sugerencias(sugerencia=miFormulario.cleaned_data['sugerencia'])
            contac.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = SugerenciaFormulario()
             
     return render(request, "App1/sugerencias.html", {"miFormulario": miFormulario})
    
def getCalificaciones(request):
    calificacion = request.GET.get('calificacion')
    puntos = Calificacion.objects.filter(calificacion__icontains=calificacion)
    return render(request, 'App1/getcalificacion.html', {'puntos': puntos})
    