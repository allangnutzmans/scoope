from typing import Any
from django.db import models

class Laminas(models.Model): #Descrição da lâmina
    nome_lamina = models.CharField(max_length=255)
    montagem = models.CharField(max_length=255)
    corte = models.CharField(max_length=255, null=True)
    aumento = models.CharField(max_length=255)
    coloracao = models.CharField(max_length=255)
    imagem_completa = models.ImageField(upload_to='imagens_laminas', null=True)

    def __str__(self):
        return f"{self.nome_lamina} {self.montagem} {self.aumento} {self.corte} {self.coloracao}" #Nome na tabela para o ADM


class Estruturas(models.Model): #Estruturas
    lamina = models.ForeignKey(Laminas, on_delete=models.CASCADE)
    nome_estrutura = models.CharField(max_length=255, null=True)
    mascara = models.ImageField(upload_to='imagens_laminas', null=True)
    #link = models.CharField(max_length=500, null=True)
  
    def __str__(self):
        return f"{self.nome_estrutura} {self.lamina}" ##Nome na tabela para o ADM
