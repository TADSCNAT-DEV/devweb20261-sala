from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View

from animais.services.animaisservices import AnimalService
from animais.services.baseanimaisservices import RacaService
from principal.utils import Utils
from principal.mixins import AbrigoMixin,AdotanteMixin
from usuarios.services import UsuarioService


class AnimalListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        busca = request.GET.get('busca')
        if busca:
            animais_lista = AnimalService.buscar_animais_por_nome(busca)
        else:
            animais_lista = AnimalService.listar_animais()

        paginador = Paginator(animais_lista, 3)
        pagina = request.GET.get('page')
        animais = paginador.get_page(pagina)

        query_params = request.GET.copy()
        query_params.pop('page', None)
        query_string = query_params.urlencode()

        tipo_usuario = UsuarioService.consultar_tipo_usuario(request.user.username)

        context = {
            'animais': animais,
            'busca': busca,
            'query_string': query_string,
            'tipo_usuario': tipo_usuario,
        }
        return render(request, 'animais/lista.html', context)


class AnimalSalvarView(LoginRequiredMixin, AbrigoMixin, View):
  
    def get(self, request, *args, **kwargs):
        racas = RacaService.listar_racas()
        context = {
            'racas': racas,
        }
        return render(request, 'animais/form.html', context)

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao')
        disponivel = request.POST.get('disponivel') == 'on'
        foto = request.FILES.get('foto')

        try:
            AnimalService.cadastrar_animal(
                nome=nome,
                data_nascimento=data_nascimento,
                sexo=sexo,
                cor=cor,
                raca_id=raca_id,
                descricao=descricao,
                disponivel=disponivel,
                foto=foto,
            )
        except ValidationError as e:
            racas = RacaService.listar_racas()
            context = {
                'racas': racas,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/form.html', context)

        messages.success(request, 'Animal cadastrado com sucesso!')
        return redirect('animais:listar_animais')


class AnimalAtualizarView(LoginRequiredMixin, AbrigoMixin, View):

    def get(self, request, *args, **kwargs):
        animal_id = kwargs.get('id')
        animal = AnimalService.obter_animal(animal_id)
        racas = RacaService.listar_racas()
        context = {
            'animal': animal,
            'racas': racas,
        }
        return render(request, 'animais/form.html', context)

    def post(self, request, *args, **kwargs):
        animal_id = kwargs.get('id')
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao')
        disponivel = request.POST.get('disponivel') == 'on'
        foto = request.FILES.get('foto')

        try:
            AnimalService.atualizar_animal(
                id=animal_id,
                nome=nome,
                data_nascimento=data_nascimento,
                sexo=sexo,
                cor=cor,
                raca_id=raca_id,
                descricao=descricao,
                disponivel=disponivel,
                foto=foto,
            )
        except ValidationError as e:
            animal = AnimalService.obter_animal(animal_id)
            racas = RacaService.listar_racas()
            context = {
                'animal': animal,
                'racas': racas,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/form.html', context)

        messages.success(request, 'Animal atualizado com sucesso!')
        return redirect('animais:listar_animais')


class AnimalExcluirView(LoginRequiredMixin, AbrigoMixin, View):

    def post(self, request, *args, **kwargs):
        animal_id = kwargs.get('id')
        animal = AnimalService.obter_animal(animal_id)
        animal.delete()
        messages.success(request, 'Animal excluido com sucesso!')
        return redirect('animais:listar_animais')

    def get(self, request, *args, **kwargs):
        return redirect('animais:listar_animais')
