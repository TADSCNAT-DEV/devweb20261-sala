from django.shortcuts import render,redirect
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

def listar_racas(request):
    busca=request.GET.get('busca')
    if busca:
        racas = RacaService.buscar_racas_por_nome(busca)
    else:
        racas = RacaService.listar_racas()

    context = {
        'racas': racas,
        'busca': busca,
    }
    return render(request, 'animais/raca/lista.html', context)


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
        return redirect('animais:listar_animais')
def excluir_animal(request, id):
    if request.method == 'POST':
        animal = AnimalService.obter_animal(id)
        animal.delete()
        return redirect('animais:listar_animais')
    else:
        return redirect('animais:listar_animais')
