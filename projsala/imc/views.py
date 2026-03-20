from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.​
def index(request):
    return HttpResponse("<h1> Bem-vindo(a) à  aplicação  IMC</h1>")
def jose(request):
    return HttpResponse("<h2> Bem-vindo José à  aplicação  IMC</h2>")