from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Carro(models.Model):
    placa = models.CharField(max_length=15)
    modelo = models.CharField(max_length=50)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.modelo} ({self.placa})'
    