from django.contrib import admin
from .models import Pergunta, Alternativa



class QuestionAdmin(admin.ModelAdmin):
     fieldsets= [
         (None, {'fields':['texto']}),
         ('Informações de data', {'fields':['data_pub']}),
         ]
     #list_display = ['texto']

admin.site.register(Pergunta,QuestionAdmin)
admin.site.register(Alternativa)
# Register your models here.
