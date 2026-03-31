from django.shortcuts import render

# Create your views here.
def index(request): 
    contexto = {
        'questao': 'Qual é a sua linguagem de programação favorita?',
        'alternativa1': 'Python',
        'alternativa2': 'JavaScript',
        'alternativa3': 'Java',
        'alternativa4': 'C#',
    }
    return render(request,'index2.html', contexto)
