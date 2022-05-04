from django.db import models

# Create your models here.

class message(models.Model):
    mensagem = models.CharField('mensagem',max_length=500)
    hora = models.DateTimeField(auto_now_add=True)
    is_human = models.BooleanField('humano',default=False)
    token = models.CharField('token',max_length=90)

    class Meta:
        verbose_name = 'mensagem'
        verbose_name_plural = 'mensagens'
        ordering =['id']
       
    def __str__(self):
        return self.mensagem