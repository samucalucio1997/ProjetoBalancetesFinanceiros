# Create your views her
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
import datetime
from django.utils import timezone


from myApp.models import Pergunta


class Req(View):
     def get(self, request, *args, **kwargs):
         return HttpResponse('<h1>Aplicação da classe no elementode views rodando</h1>')


def req(request):
    return HttpResponse('<h1>Olá, minha aplicação</h1>')

def detalhes(request, pergunta_id):
    resposta = 'detalhes %s' % pergunta_id
    return HttpResponse(resposta)

def principal(request):
    output = Pergunta.objects.order_by('-data_pub')
    return render(request,'myApp/index.html',{'output':output})


def secundario(request, pergunta_id):
        alt_list = get_object_or_404(Pergunta, pk = pergunta_id)
        return render(request,'myApp/Pergunta.html',{'alt_list':alt_list})


def coletavoto(request, pergunta_id):
    Alt = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
       p=Alt.alternativa_set.get(pk = request.POST['pergunta_id'])
    except (KeyError,Pergunta.DoesNotExist):
        return render(request,'myApp/Pergunta.html',{
            'pergunta':Pergunta,
            'error_mensage':"você não selecionou uma alternativa"})
    else:
       p.qtd_votos+=1
       p.save()
       return render(request,'myApp/results.html',{'context':Alt})


def results(request, pergunta_id):
    alt = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'myApp/results.html',{'context':alt})


def Create_Objt(quest_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    if(days<=timezone.now()):
        return Pergunta.objects.create(texto=quest_text,data_pub = time)
    else:
        return Pergunta.objects.create(texto=quest_text,data_pub = timezone.now())



def index(request):
    return HttpResponse('<h1>Grandes programadores usam <a href="https://docs.oracle.com/javase/8/docs/api/overview-summary.html">Java</a> </h1>')
