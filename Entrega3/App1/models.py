from django.db import models


class Contactos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)    
    email= models.EmailField(max_length=30)
    telefono= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - Telefono {self.telefono}"
    
class Sugerencias(models.Model):
    id=models.AutoField(primary_key=True)
    sugerencia= models.CharField(max_length=30) 
    def __str__(self):
        return f"Sugerencia: {self.sugerencia}"   

class Calificacion(models.Model):
    id=models.AutoField(primary_key=True)
    calificacion= models.CharField(max_length=30) 
    def __str__(self):
        return f"Calificaion: {self.calificacion}"    
       
