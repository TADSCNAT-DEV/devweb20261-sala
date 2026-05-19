from django.shortcuts import render

from leilao.models import Leilao
# Create your views here.

def index(request):
    leiloes = Leilao.objects.all()
    return render(request, 'index.html', {'leiloes': leiloes})

def listar_itens_leilao(request, leilao_id):
    leilao = Leilao.objects.get(id=leilao_id)
    busca=request.GET.get('busca')
    if busca:
        itens = leilao.itens.filter(titulo__icontains=busca)
    else:
        itens = leilao.itens.all()
    return render(request, 'itens_leilao.html', {'leilao': leilao, 'itens': itens})