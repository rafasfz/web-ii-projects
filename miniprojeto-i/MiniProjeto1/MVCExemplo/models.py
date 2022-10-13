from django.db import models

class SistemaOperacional(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self):
    return self.nome
  
class Curso(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self):
    return self.nome

class Linguagem(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self):
    return self.nome

class Estudante(models.Model):
  primeiroNome = models.CharField(max_length=50)
  ultimoNome = models.CharField(max_length=50)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
  linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE, null=True, blank=True)
  email = models.EmailField(max_length=100)
  sistemasOperacionais = models.ManyToManyField(SistemaOperacional)
