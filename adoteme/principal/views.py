from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from animais.models import Animal
from animais.models import Raca
from animais.services.animaisservices import AnimalService
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from adocao.models import ProcessoAdocao
from django.core.paginator import Paginator
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return index_logado(request)
    else:
        if request.method == 'GET':
            return render(request, 'principal/interna/login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return index_logado(request)
            else:
                return render(request, 'principal/interna/login.html', {'error': 'Usuário ou senha inválidos.'})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return index(request)

@login_required
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

    lista_animais = AnimalService.buscar(
        nome=nome or None,
        tipo=tipo or None,
        raca=raca or None,
        disponivel=disponivel,
    )

    paginador=Paginator(lista_animais,3)
    pagina = request.GET.get('page')
    animais = paginador.get_page(pagina)

    query_params = request.GET.copy()
    query_params.pop('page', None)
    query_string = query_params.urlencode()


    context = {
        'animais': animais,
        'animais_disponiveis': AnimalService.listar_animais(disponivel=True),
        'tipos': TipoAnimalService.listar_tipos_animais(),
        'racas': RacaService.listar_racas(),
        'filtro_nome': nome,
        'filtro_tipo': tipo,
        'filtro_raca': raca,
        'query_string':query_string,
        'filtro_disponivel': disponibilidade,
        'total_animais': AnimalService.listar_animais().count(),
        'total_tipos': TipoAnimalService.listar_tipos_animais().count(),
        'total_adocoes': 0,
    }
    return render(request, 'principal/landing/index.html', context)
