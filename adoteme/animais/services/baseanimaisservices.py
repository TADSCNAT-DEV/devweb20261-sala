from animais.models import Raca, TipoAnimal

class RacaService:

    @staticmethod
    def obter_raca(id):
        return Raca.objects.get(id=id)

    @staticmethod
    def listar_racas():
        return Raca.objects.all()

    @staticmethod
    def buscar_racas_por_nome(nome):
        return Raca.objects.filter(nome__icontains=nome)

class TipoAnimalService:

    @staticmethod
    def obter_tipo_animal(id):
        return TipoAnimal.objects.get(id=id)

    @staticmethod
    def listar_tipos_animais():
        return TipoAnimal.objects.all()
    
    @staticmethod
    def buscar_tipos_animais_por_nome(nome):
        return TipoAnimal.objects.filter(nome__icontains=nome)