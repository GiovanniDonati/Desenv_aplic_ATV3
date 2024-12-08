from django.db import models

# Create your models here.
from django.db import models
class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)
