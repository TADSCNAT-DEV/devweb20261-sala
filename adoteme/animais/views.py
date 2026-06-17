from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from animais.models import Animal
from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from animais.services.animaisservices import AnimalService
from django.core.exceptions import ValidationError
# Create your views here.

@login_required
def listar_animais(request):
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

    context = {
        'animais': animais,
        'busca': busca,
        'query_string': query_string,
    }
    return render(request, 'animais/lista.html', context)

@login_required
def listar_tipos(request):
    busca = request.GET.get('busca')
    if busca:
        tipos_lista = TipoAnimalService.buscar_tipos_animais_por_nome(busca)
    else:
        tipos_lista = TipoAnimalService.listar_tipos_animais()

    paginador = Paginator(tipos_lista, 3)
    pagina = request.GET.get('page')
    tipos = paginador.get_page(pagina)

    query_params = request.GET.copy()
    query_params.pop('page', None)
    query_string = query_params.urlencode()

    context = {
        'tipos': tipos,
        'busca': busca,
        'query_string': query_string,
    }
    return render(request, 'animais/tipo/lista.html', context)

@login_required
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

@login_required
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
@login_required
def excluir_animal(request, id):
    if request.method == 'POST':
        animal = AnimalService.obter_animal(id)
        animal.delete()
        messages.success(request, 'Animal excluido com sucesso!')
        return redirect('animais:listar_animais')
    else:
        return redirect('animais:listar_animais')
@login_required
def cadastrar_tipo_animal(request):
    if request.method == 'GET':
        return render(request, 'animais/tipo/form.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        try:
            tipo_animal = TipoAnimalService.cadastrar_tipo_animal(nome)
        except ValidationError  as e:
            context = {
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/tipo/form.html', context)
        messages.success(request, 'Tipo de animal cadastrado com sucesso!')
        return redirect('animais:listar_tipos')

@login_required
def atualizar_tipo_animal(request, id):
    if request.method == 'GET':
        tipo_animal = TipoAnimalService.obter_tipo_animal(id)
        context = {
            'tipo_animal': tipo_animal,
        }
        return render(request, 'animais/tipo/form.html', context)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        try:
            tipo_animal = TipoAnimalService.atualizar_tipo_animal(id, nome)
        except ValidationError  as e:
            tipo_animal = TipoAnimalService.obter_tipo_animal(id)
            context = {
                'tipo_animal': tipo_animal,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/tipo/form.html', context)
        messages.success(request, 'Tipo de animal atualizado com sucesso!')
        return redirect('animais:listar_tipos')

def excluir_tipo_animal(request, id):
    if request.method == 'POST':
        tipo_animal = TipoAnimalService.obter_tipo_animal(id)
        tipo_animal.delete()
        messages.success(request, 'Tipo de animal excluido com sucesso!')
        return redirect('animais:listar_tipos')
    else:
        return redirect('animais:listar_tipos')

@login_required
def listar_racas(request):
    busca = request.GET.get('busca')
    if busca:
        racas_lista = RacaService.buscar_racas_por_nome(busca)
    else:
        racas_lista = RacaService.listar_racas()

    paginador = Paginator(racas_lista, 3)
    pagina = request.GET.get('page')
    racas = paginador.get_page(pagina)

    query_params = request.GET.copy()
    query_params.pop('page', None)
    query_string = query_params.urlencode()

    context = {
        'racas': racas,
        'busca': busca,
        'query_string': query_string,
    }
    return render(request, 'animais/raca/lista.html', context)

@login_required
def cadastrar_raca(request):
    if request.method == 'GET':
        tipos_animais = TipoAnimalService.listar_tipos_animais()
        context = {
            'tipos_animais': tipos_animais,
        }
        return render(request, 'animais/raca/form.html', context)
    elif request.method == 'POST':
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
@login_required
def atualizar_raca(request, id):
    if request.method == 'GET':
        raca = RacaService.obter_raca(id)
        tipos_animais = TipoAnimalService.listar_tipos_animais()
        context = {
            'raca': raca,
            'tipos_animais': tipos_animais,
        }
        return render(request, 'animais/raca/form.html', context)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        tipo_animal_id = request.POST.get('tipo_animal_id')
        try:
            raca = RacaService.atualizar_raca(id, nome, tipo_animal_id)
        except ValidationError  as e:
            raca = RacaService.obter_raca(id)
            tipos_animais = TipoAnimalService.listar_tipos_animais()
            context = {
                'raca': raca,
                'tipos_animais': tipos_animais,
                'erros': e.message_dict,
                'dados': request.POST,
            }
            return render(request, 'animais/raca/form.html', context)
        messages.success(request, 'Raça atualizada com sucesso!')
        return redirect('animais:listar_racas')
@login_required
def excluir_raca(request, id):
    if request.method == 'POST':
        raca = RacaService.obter_raca(id)
        raca.delete()
        messages.success(request, 'Raça excluida com sucesso!')
        return redirect('animais:listar_racas')
    else:
        return redirect('animais:listar_racas')