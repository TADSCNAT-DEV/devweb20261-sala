from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from animais.services.baseanimaisservices import TipoAnimalService
from principal.mixins import AbrigoMixin
from animais.forms import TipoAnimalForm
from principal.utils import FormUtils

TIPO_ANIMAL_FORM_TEMPLATE = 'animais/tipo/form.html'
TIPO_ANIMAL_LIST_ROUTE = 'animais:listar_tipos'




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
        busca = self.request.GET.get('busca', '')
        if busca:
            queryset = TipoAnimalService.buscar_tipos_animais_por_nome(busca)
        else:
            queryset = TipoAnimalService.listar_tipos_animais()
        return queryset
    


class TipoAnimalSalvarView(LoginRequiredMixin, AbrigoMixin, View):
    def get(self, request, *args, **kwargs):
        form=TipoAnimalForm()
        return render(request, TIPO_ANIMAL_FORM_TEMPLATE, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TipoAnimalForm(request.POST)
        if not form.is_valid():
            return render(request, TIPO_ANIMAL_FORM_TEMPLATE, {'form': form})
        try:
            TipoAnimalService.cadastrar_tipo_animal(form.cleaned_data['nome'])
        except ValidationError as e:
            FormUtils.adicionar_erros_validacao_ao_formulario(form, e)
            return render(request, TIPO_ANIMAL_FORM_TEMPLATE, {'form': form})

        messages.success(request, 'Tipo de animal cadastrado com sucesso!')
        return redirect(TIPO_ANIMAL_LIST_ROUTE)


class TipoAnimalAtualizarView(LoginRequiredMixin, AbrigoMixin, View):
    def get(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        form = TipoAnimalForm(initial={'nome': tipo_animal.nome})
        context = {
            'tipo_animal': tipo_animal,
            'form': form,
        }
        return render(request, TIPO_ANIMAL_FORM_TEMPLATE, context)

    def post(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        form = TipoAnimalForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'tipo_animal': TipoAnimalService.obter_tipo_animal(tipo_animal_id),
            }
            return render(request, TIPO_ANIMAL_FORM_TEMPLATE, context)
        try:
            TipoAnimalService.atualizar_tipo_animal(tipo_animal_id, form.cleaned_data['nome'])
        except ValidationError as e:
            tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
            FormUtils.adicionar_erros_validacao_ao_formulario(form, e)
            context = {
                'tipo_animal': tipo_animal,
                'form': form,
            }
            return render(request, TIPO_ANIMAL_FORM_TEMPLATE, context)

        messages.success(request, 'Tipo de animal atualizado com sucesso!')
        return redirect(TIPO_ANIMAL_LIST_ROUTE)


class TipoAnimalExcluirView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, *args, **kwargs):
        tipo_animal_id = kwargs.get('id')
        tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        tipo_animal.delete()
        messages.success(request, 'Tipo de animal excluido com sucesso!')
        return redirect(TIPO_ANIMAL_LIST_ROUTE)

    def get(self, request, *args, **kwargs):
        return redirect(TIPO_ANIMAL_LIST_ROUTE)
