
from django.views import View
from django.shortcuts import render
from animais.services.animaisservices import AnimalService
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from adocao.models import ProcessoAdocao
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from principal.forms import ContatoForm
class PrincipalView(View):
    def get(self, request):
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

class PrincipalLogadoView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        context = {
        'total_animais':AnimalService.listar_animais().count(),
        'total_racas': RacaService.listar_racas().count(),
        'total_pedidos_adocao': 0,
        'pedidos_em_analise': 0,
        'animais_disponiveis': AnimalService.listar_animais(disponivel=True).count(),
        'animais_indisponiveis': AnimalService.listar_animais(disponivel=False).count(),
    }
        return render(request, 'principal/interna/index.html', context)

class ContatoView(View):
    def get(self, request):
        form = ContatoForm()
        return render(request, 'principal/landing/contato.html', {'form': form})

    def post(self, request):
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você pode processar os dados do formulário, como enviar um e-mail ou salvar no banco de dados
            return render(request, 'principal/landing/contato_sucesso.html', {'form': form})
        else:
            return render(request, 'principal/landing/contato.html', {'form': form})