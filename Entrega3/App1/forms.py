from django import forms
 
class ContactosFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)    
    email= forms.EmailField()
    telefono= forms.CharField(max_length=30) 

class CalificacionFormulario(forms.Form):
    id= forms.IntegerField()
    calificacion= forms.IntegerField()  

class SugerenciaFormulario(forms.Form):
    id= forms.IntegerField()
    sugerencia= forms.CharField(max_length=30)    
             
         