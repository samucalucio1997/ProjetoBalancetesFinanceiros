from django.contrib import admin
from .models import Usuario,Balancete,Receitas,Despesas

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Receitas)
admin.site.register(Despesas)
