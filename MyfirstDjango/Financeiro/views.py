# import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from .models import Usuario,Balancete
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView, LogoutView
from .service import Dash_datas
# from django.utils import timezone
from django import forms
# Create your views here.

    # class Meta:
    #     model = User
    #     fields=['username','email','password']

class CadastroUser(forms.Form):
    username = forms.CharField(label='nome',max_length=150)
    password = forms.CharField(label='senha',max_length=150)
    email = forms.EmailField(label='emai',max_length=150)

class CadastroBalanco(forms.Form):
    nome = forms.CharField(label='nome',max_length=150)
    data = forms.DateTimeField(label='data_nasc')

#################################################################################################

class Principal(View):
    def get(self, request, *args, **kwargs):
        return render(request,'Financeiro/TelaLogin.html')

class FormCad(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Financeiro/Cadastrousuario.html')

class Red(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        usuario = user.usuario
        Bal = []
        if usuario != None:
           Bal = Balancete.objects.filter(user = usuario)   
        return Dash_datas().ret(request,Balancete,usuario)

class FormCadBala(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Financeiro/CadastrarBalancete.html')

class CadastrarUsuario(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':  # A verificação do método POST deve estar fora do bloco if
            data_nasc = request.POST.get['data_nasc']
            form = CadastroUser(request.POST)
            if form.is_valid(): # Verifique se o formulário é válido
                nome = form.cleaned_data['username']
                senha = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user = User.objects.create_user(nome,email,senha)
                user.save()
                usuario = Usuario()
                usuario.user = user
                usuario.data_nasc=data_nasc
                usuario.save()
                USSR = request.user
                return redirect(request,'Financeiro/Dashboard.html',{'user':USSR})
        else:
            messages.error(request,'Dados não válidados')
            return render(request,'Financeiro/Cadastrousuario.html')


class LoginFace(View):
    def post(self,request):
        # nome = request.GET.get('nome','')
        # senha =
        user = authenticate(username=request.POST.get('nome',''), password=request.POST.get('senha',''))
        if user is not None:
            login(request, user)
            user = request.user
            usuario = user.usuario
            Balete = Balancete.objects.filter(user = usuario)
            return Dash_datas().ret(request,Balete,usuario)
        else:
            messages.error(request,'Não autenticado')
            return render(request,'Financeiro/TelaLogin.html')

class CadastraBalanco(View):
    def post(self,request):
        form = CadastroBalanco(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            data = form.cleaned_data['data']
            Balanco = Balancete()
            Balanco.nome = nome
            Balanco.data = data
            user = request.user
            Balanco.user = user.usuario
            Balanco.save()
            return render(request,'Financeiro/CadastrarReceita.html',{'balanco':Balanco})
        else:
            messages.error(request,'Não cadastrado')
            return redirect('Financeiro:balancoCad')  

class AdicionarRec(View):
    def post(self,request,pk):
        return None 
       



        
        


