from django.shortcuts import render
from animais.models import Animal
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from animais.services.animaisservices import AnimalService
# Create your views here.

def listar_animais(request):
    busca = request.GET.get('busca')
    if busca:
        animais = AnimalService.buscar_animais_por_nome(busca)
    else:
        animais = AnimalService.listar_animais()

    context = {
        'animais': animais,
        'busca': busca,
    }
    return render(request, 'animais/lista.html', context)

def listar_tipos(request):
    busca = request.GET.get('busca')
    if busca:
        tipos = TipoAnimalService.buscar_tipos_animais_por_nome(busca)
    else:
        tipos = TipoAnimalService.listar_tipos_animais()

    context = {
        'tipos': tipos,
        'busca': busca,
    }
    return render(request, 'animais/tipo/lista.html', context)
