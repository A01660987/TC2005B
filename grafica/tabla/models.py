from django.db import models

# Create your models here.
class Alumnos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    horas = models.IntegerField()
