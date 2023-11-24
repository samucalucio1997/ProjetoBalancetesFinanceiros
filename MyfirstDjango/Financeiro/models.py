from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    login = models.ForeignKey(User,on_delete=models.CASCADE)

class Balancete(models.Model):
     nome = models.CharField(max_length = 180, blank=False)
     ft_boleto = models.ImageField(upload_to='Balancete_imgs/', null=True, blank=True)
     data = models.DateTimeField('Data de publicação' , null=True)
     user = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Receitas(models.Model):
      nome = models.CharField(max_length = 80, blank=False)
      valor = models.FloatField(blank=False,default = 0.0)
      balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)


class Despesas(models.Model):
      nome = models.CharField(max_length = 80, blank=False)
      valor = models.FloatField(blank=False,default = 0.0)
      balancete = models.ForeignKey(Balancete, on_delete = models.CASCADE)


