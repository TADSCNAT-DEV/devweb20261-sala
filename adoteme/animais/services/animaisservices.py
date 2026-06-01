
from animais.models import Animal

class AnimalService:

    @staticmethod
    def obter_animal(id):
        return Animal.objects.get(id=id)

    @staticmethod
    def listar_animais(disponivel=None):
        if disponivel is not None:
            return Animal.objects.filter(disponivel=disponivel)
        return Animal.objects.all()
    
    @staticmethod
    def buscar_animais_por_nome(nome):
        return Animal.objects.filter(nome__icontains=nome)
    
    @staticmethod
    def buscar(nome=None, tipo=None, raca=None, disponivel=None):
        animais = Animal.objects.select_related('raca', 'raca__tipo_animal')

        if disponivel is not None:
            animais = Animal.objects.filter(disponivel=disponivel)

        if nome:
            animais = animais.filter(nome__icontains=nome)
        
        if tipo:
            animais = animais.filter(raca__tipo_animal_id=tipo)
        
        if raca:
            animais = animais.filter(raca__id=raca)

        return animais