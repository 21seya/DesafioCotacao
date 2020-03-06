from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Moeda(models.Model):
    codigo = models.IntegerField()
    tipo = models.CharField(max_length=5)
    nome = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=3)
    compra = models.DecimalField(max_digits=5,decimal_places=2)
    venda = models.DecimalField(max_digits=5,decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.nome

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)   

    def __str__(self):
        return self.nome
