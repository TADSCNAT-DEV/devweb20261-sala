from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index_lista.html')
def buscar(request):
    q = request.GET.get('q', '')
    alunos = [
        {'nome': 'Ana', 'curso': 'ADS'},
        {'nome': 'João', 'curso': 'SI'},
        {"nome": "Ana Lima",
         "curso": "Computação"},
        {"nome": "Bruno Costa",
         "curso": "Engenharia"},
        {"nome": "Carla Souza",
         "curso": "Sistemas"},
    ]
    if q:
        alunos = [a for a in alunos if q.lower() in a['nome'].lower() or q.lower() in a['curso'].lower()]
    return render(request, 'lista.html', {'alunos': alunos, 'q': q})