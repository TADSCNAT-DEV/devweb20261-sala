from django.shortcuts import render
from animais.models import Animal
from animais.models import Raca
from animais.services.animaisservices import AnimalService
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from adocao.models import ProcessoAdocao
# Create your views here.


def index_logado(request):
    context = {
        'total_animais':AnimalService.listar_animais().count(),
        'total_racas': RacaService.listar_racas().count(),
        'total_pedidos_adocao': 0,
        'pedidos_em_analise': 0,
        'animais_disponiveis': AnimalService.listar_animais(disponivel=True).count(),
        'animais_indisponiveis': AnimalService.listar_animais(disponivel=False).count(),
    }
    return render(request, 'principal/interna/index.html', context)

def index(request):
    nome = request.GET.get('nome', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    raca = request.GET.get('raca', '').strip()
    disponibilidade = request.GET.get('disponivel', 'todos').strip() or 'todos'

    disponivel = None
    if disponibilidade == 'sim':
        disponivel = True
    elif disponibilidade == 'nao':
        disponivel = False

    animais = AnimalService.buscar(
        nome=nome or None,
        tipo=tipo or None,
        raca=raca or None,
        disponivel=disponivel,
    )

    context = {
        'animais': animais,
        'animais_disponiveis': AnimalService.listar_animais(disponivel=True),
        'tipos': TipoAnimalService.listar_tipos_animais(),
        'racas': RacaService.listar_racas(),
        'filtro_nome': nome,
        'filtro_tipo': tipo,
        'filtro_raca': raca,
        'filtro_disponivel': disponibilidade,
        'total_animais': AnimalService.listar_animais().count(),
        'total_tipos': TipoAnimalService.listar_tipos_animais().count(),
        'total_adocoes': 0,
    }
    return render(request, 'principal/landing/index.html', context)
