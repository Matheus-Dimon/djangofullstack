from django.db import models

class cadastro(models.Model):
    descrição = models.CharField(max_length=255 , primary_key=True)
    marca = models.TextField(max_length=255)
    modelo = models.TextField(max_length=255)
    preço = models.IntegerField()