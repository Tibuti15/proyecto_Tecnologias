from django.db import models

# Create your models here.
class Tecnologias(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    foto=models.FileField(upload_to='tecnologias',null=True,blank=True)

    def __str__(self):
        return self.nombre

class SitioWeb(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    url = models.URLField()
    creador = models.CharField(max_length=150)
    tecnologias = models.ForeignKey(Tecnologias, on_delete=models.CASCADE)
    foto = models.FileField(upload_to='logo',null=True,blank=True)


    def __str__(self):
        return self.nombre

