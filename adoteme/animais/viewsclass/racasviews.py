
from django.views.generic import ListView,View
from animais.models import Raca
from animais.services.baseanimaisservices import RacaService,TipoAnimalService
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from principal.mixins import AbrigoMixin

class RacaListView(ListView,LoginRequiredMixin):
    template_name = 'animais/raca/lista.html'
    context_object_name = 'racas'
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
            queryset = RacaService.buscar_racas_por_nome(search_query)
        else:
            queryset = RacaService.listar_racas()
        return queryset

class RacaSalvarView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        tipo_animal_id = request.POST.get('tipo_animal_id')
        try:
            raca = RacaService.cadastrar_raca(nome, tipo_animal_id)
        except ValidationError  as e:
            tipos_animais = TipoAnimalService.listar_tipos_animais()
            context = {
                'tipos_animais': tipos_animais,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/raca/form.html', context)
        messages.success(request, 'Raça cadastrada com sucesso!')
        return redirect('animais:listar_racas')
    def get(self, request, *args, **kwargs):
        tipos_animais = TipoAnimalService.listar_tipos_animais()
        context = {
            'tipos_animais': tipos_animais,
        }
        return render(request, 'animais/raca/form.html', context)
class RacaAtualizarView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, *args, **kwargs):
        raca_id = kwargs.get('id')
        nome = request.POST.get('nome')
        tipo_animal_id = request.POST.get('tipo_animal_id')
        try:
            raca = RacaService.atualizar_raca(raca_id, nome, tipo_animal_id)
        except ValidationError as e:
            tipos_animais = TipoAnimalService.listar_tipos_animais()
            context = {
                'tipos_animais': tipos_animais,
                'erros': e.message_dict,
                'dados': request.POST,
                'raca_id': raca_id,
            }
            return render(request, 'animais/raca/form.html', context)
        messages.success(request, 'Raça atualizada com sucesso!')
        return redirect('animais:listar_racas')

    def get(self, request, *args, **kwargs):
        raca_id = kwargs.get('id')
        raca = RacaService.obter_raca(raca_id)
        tipos_animais = TipoAnimalService.listar_tipos_animais()
        context = {
            'raca': raca,
            'tipos_animais': tipos_animais,
        }
        return render(request, 'animais/raca/form.html', context)
    
class RacaExcluirView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, *args, **kwargs):
        raca_id = kwargs.get('id')
        RacaService.excluir_raca(raca_id)
        messages.success(request, 'Raça excluída com sucesso!')
        return redirect('animais:listar_racas')