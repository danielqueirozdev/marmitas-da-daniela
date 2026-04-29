from django.db import models
from django.contrib.auth.models import User

""" # Create your models here.
class ADMcontrol(models.Model):
    nome = models.CharField(max_length=160, null=False)
    ingredientes = models.CharField(max_length=260, null=False)
    descricao = models.CharField(max_length=260, null=False)
    peso = models.IntegerField(null=False)
    preco = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        )
    # imagem = models.ImageField(null=False)

    def __str__(self):
        return self.nome """