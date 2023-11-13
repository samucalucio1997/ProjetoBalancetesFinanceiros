import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length = 150)
    data_pub = models.DateTimeField('Data de publicação')
    ativo = models.BooleanField(default = True)
    def rece_pub(self):
        return self.data_pub >= (timezone.now() - datetime.timedelta(days=1)) and (timezone.now())




class Alternativa(models.Model):
     texto=models.CharField(max_length=80)
     qtd_votos=models.IntegerField(default=0)
     pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
     ativo = models.BooleanField(default = True)