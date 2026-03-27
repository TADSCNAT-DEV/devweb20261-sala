from django.shortcuts import render
from django.http import HttpResponse
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
