from django.shortcuts import render
from django.http import HttpResponse
from .models import Moeda,Pais
from .forms import MoedaForm,PaisForm
# Create your views here.

def home(request):
    msg = "mensagem da pagina"
    moedas = Moeda.objects.all()
    paises = Pais.objects.all()
    return render(request,"cotacao/index.html",{"msg":msg,"moedas":moedas,"paises":paises})

def moeda(request):
    return HttpResponse('<h1>Ola Moedas</h1>')

def criacao_moedas(request):
    form = MoedaForm()
    formpais = PaisForm()
    return render(request,"cotacao/criacao_moedas.html",{"form":form},{"formpais":formpais}) 
