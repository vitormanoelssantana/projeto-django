from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} ({self.estado.sigla})'

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    dataDeNascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'
