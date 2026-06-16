
from animais.models import Animal
from django.core.exceptions import ValidationError
class AnimalService:

    @staticmethod
    def obter_animal(id):
        try:
            return Animal.objects.get(id=id)
        except Animal.DoesNotExist:
            return None

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
        animais = Animal.objects.all()

        if disponivel is not None:
            animais = animais.objects.filter(disponivel=disponivel)

        if nome:
            animais = animais.filter(nome__icontains=nome)
        
        if tipo:
            animais = animais.filter(raca__tipo_animal_id=tipo)
        
        if raca:
            animais = animais.filter(raca__id=raca)

        return animais
    
    @staticmethod
    def cadastrar_animal(nome, data_nascimento, sexo, cor, raca_id, descricao=None, disponivel=True, foto=None):
        animal = Animal(
            nome=nome,
            data_nascimento=data_nascimento,
            sexo=sexo,
            cor=cor,
            raca_id=raca_id,
            descricao=descricao,
            disponivel=disponivel,
            foto=foto
        )
        try:
            animal.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e 
        animal.save()
        return animal
    
    @staticmethod
    def atualizar_animal(id, nome=None, data_nascimento=None, sexo=None, cor=None, raca_id=None, descricao=None, disponivel=None, foto=None):
        animal = Animal.objects.get(id=id)

        if nome is not None:
            animal.nome = nome
        if data_nascimento is not None:
            animal.data_nascimento = data_nascimento
        if sexo is not None:
            animal.sexo = sexo
        if cor is not None:
            animal.cor = cor
        if raca_id is not None:
            animal.raca_id = raca_id
        if descricao is not None:
            animal.descricao = descricao
        if disponivel is not None:
            animal.disponivel = disponivel
        if foto is not None:
            animal.foto = foto
        try:
            animal.full_clean()  # Valida os dados do modelo
        except ValidationError as e:
            raise e
        animal.save()
        return animal
    @staticmethod
    def excluir_animal(id):
        animal=AnimalService.obter_animal(id)
        if animal:
            return animal.delete()
        else:
            raise ValidationError("Animal com o id não existe")