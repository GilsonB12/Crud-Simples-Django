from django.db import models

class Pessoas(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao_nome = models.TextField(max_length=255)
