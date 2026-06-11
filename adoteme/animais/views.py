from django.contrib import messages
from django.shortcuts import render,redirect
from animais.models import Animal
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from animais.services.animaisservices import AnimalService
from django.core.exceptions import ValidationError
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

def cadastrar_animal(request):
    if request.method == 'GET':
        racas = RacaService.listar_racas()
        context = {
            'racas': racas,
        }
        return render(request, 'animais/form.html', context)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao')
        disponivel = request.POST.get('disponivel') == 'on'
        foto = request.FILES.get('foto')
        try:

            animal = AnimalService.cadastrar_animal(
                nome=nome,
                data_nascimento=data_nascimento,
                sexo=sexo,
                cor=cor,
                raca_id=raca_id,
                descricao=descricao,
                disponivel=disponivel,
                foto=foto
            )
        except ValidationError  as e:
            racas = RacaService.listar_racas()
            context = {
                'racas': racas,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/form.html', context)
        messages.success(request, 'Animal cadastrado com sucesso!')
        return redirect('animais:listar_animais')
def atualizar_animal(request, id):
    if request.method == 'GET':
        animal = AnimalService.obter_animal(id)
        racas = RacaService.listar_racas()
        context = {
            'animal': animal,
            'racas': racas,
        }
        return render(request, 'animais/form.html', context)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao')
        disponivel = request.POST.get('disponivel') == 'on'
        foto = request.FILES.get('foto')
        try:
            animal = AnimalService.atualizar_animal(
                id=id,
                nome=nome,
                data_nascimento=data_nascimento,
                sexo=sexo,
                cor=cor,
                raca_id=raca_id,
                descricao=descricao,
                disponivel=disponivel,
                foto=foto
            )
        except ValidationError  as e:
            animal = AnimalService.obter_animal(id)
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
def excluir_animal(request, id):
    if request.method == 'POST':
        animal = AnimalService.obter_animal(id)
        animal.delete()
        messages.success(request, 'Animal excluido com sucesso!')
        return redirect('animais:listar_animais')
    else:
        return redirect('animais:listar_animais')
