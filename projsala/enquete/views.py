from django.shortcuts import render

# Create your views here.
total1=0
total2=0
total3=0
total4=0
def index(request): 
    contexto = {
        'questao': 'Qual é a sua linguagem de programação favorita?',
        'alternativa1': 'Python',
        'alternativa2': 'JavaScript',
        'alternativa3': 'Java',
        'alternativa4': 'C#',
    }
    return render(request,'enquete/index.html', contexto)
def votar(request):
    global total1, total2, total3, total4
    resposta = request.POST.get('alternativa')
    if resposta == '1':
        total1 += 1
    elif resposta == '2':
        total2 += 1
    elif resposta == '3':
        total3 += 1
    elif resposta == '4':
        total4 += 1
    total_votos= total1 + total2 + total3 + total4
    contexto = {
        'alternativa1': 'Python',
        'alternativa2': 'JavaScript',
        'alternativa3': 'Java',
        'alternativa4': 'C#',
        'total1': total1,
        'total2': total2,
        'total3': total3,
        'total4': total4,
        'total_votos': total_votos,
    }
    return render(request, 'enquete/resultado.html', contexto)
