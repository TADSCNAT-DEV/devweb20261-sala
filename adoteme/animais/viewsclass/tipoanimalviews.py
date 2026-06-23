from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from animais.services.baseanimaisservices import TipoAnimalService
from principal.utils import Utils
from principal.mixins import AbrigoMixin


class TipoAnimalListView(LoginRequiredMixin,ListView):
    template_name = 'animais/tipo/lista.html'
    context_object_name = 'tipos'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busca'] = self.request.GET.get('busca', '')
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_string'] = query_params.urlencode()
        return context
    def get_queryset(self):
        search_query = self.request.GET.get('busca', '')
        if search_query:
            queryset = TipoAnimalService.buscar_tipos_animais_por_nome(search_query)
        else:
            queryset = TipoAnimalService.listar_tipos_animais()
        return queryset
    


class TipoAnimalSalvarView(LoginRequiredMixin, AbrigoMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'animais/tipo/form.html')

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        try:
            TipoAnimalService.cadastrar_tipo_animal(nome)
        except ValidationError as e:
            context = {
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/tipo/form.html', context)

        messages.success(request, 'Tipo de animal cadastrado com sucesso!')
        return redirect('animais:listar_tipos')


class TipoAnimalAtualizarView(LoginRequiredMixin, AbrigoMixin, View):
    def get(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        context = {
            'tipo_animal': tipo_animal,
        }
        return render(request, 'animais/tipo/form.html', context)

    def post(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        nome = request.POST.get('nome')
        try:
            TipoAnimalService.atualizar_tipo_animal(tipo_animal_id, nome)
        except ValidationError as e:
            tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
            context = {
                'tipo_animal': tipo_animal,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/tipo/form.html', context)

        messages.success(request, 'Tipo de animal atualizado com sucesso!')
        return redirect('animais:listar_tipos')


class TipoAnimalExcluirView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        tipo_animal.delete()
        messages.success(request, 'Tipo de animal excluido com sucesso!')
        return redirect('animais:listar_tipos')

    def get(self, request, *args, **kwargs):
        return redirect('animais:listar_tipos')
