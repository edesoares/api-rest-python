from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.IntegerField(validators=[MaxValueValidator(9999999999999)])
    ano = models.IntegerField(validators=[MaxValueValidator(9999)])
    edicao = models.IntegerField(validators=[MaxValueValidator(99)])
    paginas = models.IntegerField(validators=[MaxValueValidator(9999)])