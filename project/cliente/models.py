from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.celular})"
