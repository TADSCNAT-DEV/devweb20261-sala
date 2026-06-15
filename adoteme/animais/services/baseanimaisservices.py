from animais.models import Raca, TipoAnimal
from django.core.exceptions import ValidationError
class RacaService:

    @staticmethod
    def obter_raca(id):
        try:
            return Raca.objects.get(id=id)
        except Raca.DoesNotExist:
            return None

    @staticmethod
    def listar_racas():
        return Raca.objects.all()

    @staticmethod
    def buscar_racas_por_nome(nome):
        return Raca.objects.filter(nome__icontains=nome)
    @staticmethod
    def cadastrar_raca(nome, tipo_animal_id):
        tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        raca = Raca(nome=nome, tipo_animal=tipo_animal)
        try:
            raca.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e 
        raca.save()
        return raca
    @staticmethod
    def atualizar_raca(id, nome=None, tipo_animal_id=None):
        raca = Raca.objects.get(id=id)
        if nome is not None:
            raca.nome = nome
        raca.tipo_animal = TipoAnimalService.obter_tipo_animal(tipo_animal_id)
        try:
            raca.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e 
        raca.save()
        return raca

class TipoAnimalService:

    @staticmethod
    def obter_tipo_animal(id):
        try:
            return TipoAnimal.objects.get(id=id)
        except TipoAnimal.DoesNotExist:
            return None

    @staticmethod
    def listar_tipos_animais():
        return TipoAnimal.objects.all()
    
    @staticmethod
    def buscar_tipos_animais_por_nome(nome):
        return TipoAnimal.objects.filter(nome__icontains=nome)
    
    @staticmethod
    def cadastrar_tipo_animal(nome):
        tipo_animal = TipoAnimal(nome=nome)
        try:
            tipo_animal.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e 
        tipo_animal.save()
        return tipo_animal
    @staticmethod
    def atualizar_tipo_animal(id, nome):
        tipo_animal = TipoAnimal.objects.get(id=id)
        if nome is not None:
            tipo_animal.nome = nome
        try:
            tipo_animal.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e 
        tipo_animal.save()
        return tipo_animal
    
    @staticmethod
    def excluir_tipo_animal(id):
        tipo_animal = TipoAnimal.objects.get(id=id)
        return tipo_animal.delete()