from django.db import models

class Molo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)