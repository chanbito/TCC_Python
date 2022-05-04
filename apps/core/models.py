from django.db import models

# Create your models here.
class message(models.Model):
    mensagem = models.fields.TextField()
    hora = models.DateField()