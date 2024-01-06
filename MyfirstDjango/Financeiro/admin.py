from django.contrib import admin
from .models import Usuario,Balancete,Receita,Despesa

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Receita)
admin.site.register(Despesa)
