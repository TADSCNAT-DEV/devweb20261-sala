from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from imc.services import IMCService
import json
from django.template.loader import render_to_string
# Create your views here.​
def index(request):
    return render(request,'index.html')
def jose(request):
    return HttpResponse("<h2> Bem-vindo José à  aplicação  IMC</h2>")
def tabuada(request,valor):
    html="<table border='1'>"
    html+="<tr><td>Multiplicação</td><td>Resultado</td></tr>"
    for i in range(10):
        html+=f'<tr><td>{valor}X{i+1}</td><td>{valor*(i+1)}</td></tr>'
    html+="</table>"
    resposta=HttpResponse(html)
    return resposta

def calcular_imc(request,altura,peso):
    altura=altura/100
    imc=peso/(altura*altura)
    response=f'Calculo do IMC: {imc}'
    return HttpResponse(response)

def calcular(request):
    if request.method == 'GET':
        return render(request,'erro.html')
    #altura = float(request.POST.get('altura'))
    #peso = float(request.POST.get('peso'))
    dados=json.loads(request.body)
    altura = float(dados.get('altura'))
    peso = float(dados.get('peso'))
    try:
        resultado = IMCService.calcular_imc(altura, peso)
    except ValueError as e:
        mensagem=str(e)
        return HttpResponse(mensagem, status=400)
    contexto={
        'altura':altura,
        'peso':peso,
        'resultado':resultado,
    }
    html=render_to_string('resultado_partial.html',contexto)
    return HttpResponse(html,status=200)

def mensagem(request):
    return JsonResponse({'texto':'Olá do Servidor','mensagem_texto':'Novo Texto'})
    
