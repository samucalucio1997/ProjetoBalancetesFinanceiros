from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    data_nasc = models.DateTimeField('Data de nascimento',null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, pk=True)
    def __str__(self):
        return self.user.username

class Balancete(models.Model):
     nome = models.CharField(max_length = 180, blank=False)
     data = models.DateTimeField('Data do balanço mensal' , null=True)
     user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     def __str__(self):
         return self.nome


class Receita(models.Model):
      nome = models.CharField(max_length = 80, blank=False)
      valor = models.FloatField(blank=False,null=False,default = 0.0)
      ft_boleto = models.ImageField(upload_to='Receitas_img/', null=True, blank=True)
      data = models.DateTimeField('Data referente a receita' , null=True)
      balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
      def __str__(self):
           return self.nome

class Despesa(models.Model):
      nome = models.CharField(max_length = 80, blank=False)
      valor = models.FloatField(blank=False,null=False,default = 0.0)
      ft_boleto = models.ImageField(upload_to='Despesas_img/', null=True, blank=True)
      data = models.DateTimeField('Data referente a despesa' , null=True)
      balancete = models.ForeignKey(Balancete, on_delete = models.CASCADE)
      def __str__(self):
            return self.nome

