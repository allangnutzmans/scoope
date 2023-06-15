from typing import Any
from django.db import models

class Laminas(models.Model):
    nome_lamina = models.CharField(max_length=255)
    montagem = models.CharField(max_length=255)
    corte = models.CharField(max_length=255, null=True)
    aumento = models.CharField(max_length=255)
    coloracao = models.CharField(max_length=255)
    fullimage = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f"{self.nome_lamina} {self.montagem} {self.aumento} {self.corte} {self.coloracao}" 


class Estruturas(models.Model):
    lamina = models.ForeignKey(Laminas, on_delete=models.CASCADE)
    nome_estrutura = models.CharField(max_length=255, null=True)
    source_mask = models.CharField(max_length=500, null=True)
    link = models.CharField(max_length=500, null=True)
  
    def __str__(self):
        return f"{self.nome_estrutura} {self.lamina}"
