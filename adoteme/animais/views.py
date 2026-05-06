from django.shortcuts import render
from animais.models import TipoAnimal
# Create your views here.

def listar_tipos_animais(request):
    busca=request.GET.get('busca')
    if busca:
        tipos = TipoAnimal.objects.filter(nome__icontains=busca)
    else:
        tipos = TipoAnimal.objects.all()
    return render(request, 'animais/tipo/lista.html', {'tipos': tipos,'busca':busca})
