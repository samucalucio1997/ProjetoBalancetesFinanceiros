from django.urls import path
from . import views
# Create your views her

app_name = 'myApp'
urlpatterns = [
    path('views/', views.req, name='req'),
    path('map/', views.index, name='index'),
    path('map/<int:pergunta_id>/', views.detalhes, name='detalhes'),
    path('perguntas/', views.principal, name = 'principal'),
    path('perguntas/<int:pergunta_id>/', views.secundario, name='secundario'),
    path('coletavoto/<int:pergunta_id>',views.coletavoto,name='coletavoto'),
    path('results/<int:pergunta_id>',views.results,name='results')
    ]
