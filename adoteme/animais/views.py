from django.shortcuts import render
from animais.models import TipoAnimal,Animal
# Create your views here.

def listar_tipos_animais(request):
    criterio=request.GET.get('criterio')
    if criterio:
        tipos_animais=TipoAnimal.objects.filter(nome__icontains=criterio)
    else:
        tipos_animais=TipoAnimal.objects.all()
    contexto={'tipos_animais':tipos_animais}
    return render(request,'animais/lista_tipo_animal.html',context=contexto)

def listar_animais_por_tipo(request, tipo_id):
    tipo_animal=TipoAnimal.objects.get(id=tipo_id)
    animais=Animal.objects.filter(raca__tipo_animal=tipo_animal)
    contexto = {
        'tipo_animal': tipo_animal,
        'animais': animais,
    }
    return render(request, 'animais/lista_animais_por_tipo.html', contexto)