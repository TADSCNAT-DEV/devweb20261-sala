from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from datetime import date
class TipoAnimal(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    def clean(self):
        erros = {}
        if not self.nome:
            erros['nome'] = 'O nome do tipo de animal é obrigatório.'
        elif len(self.nome) < 5:
            erros['nome'] = 'O nome do tipo de animal deve ter pelo menos 5 caracteres.'
        elif len(self.nome) > 50:
            erros['nome'] = 'O nome do tipo de animal não pode exceder 50 caracteres.'
        else:
            self.nome = self.nome.upper()
        if erros:
            raise ValidationError(erros)

    class Meta:
        verbose_name_plural = "Tipos de Animais"
        ordering = ['nome']
        permissions=[
            ('pode_visualizar_tipoanimal','Pode Visualizar Tipo de Animal')
        ]

class Raca(models.Model):
    nome = models.CharField(max_length=50)
    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE,related_name='racas')

    def __str__(self):
        return f"{self.tipo_animal.nome} ({self.nome})"
    
    def clean(self):
        
        erros = {}
        if not self.nome:
            erros['nome'] = 'O nome da raça é obrigatório.'
        elif len(self.nome) < 3:
            erros['nome'] = 'O nome da raça deve ter pelo menos 3 caracteres.'
        else:
            self.nome = self.nome.upper()
        if self.tipo_animal is None:
            erros['tipo_animal'] = 'O tipo de animal é obrigatório.'
        #Se quiser salvar o nome em maiúsculo
        if erros:
            raise ValidationError(erros)

    class Meta:
        verbose_name_plural = "Raças"
        ordering = ['tipo_animal__nome', 'nome']

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo=models.CharField(max_length=1,choices=[('M','Masculino'),('F','Feminino')])
    cor = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE,related_name='animais')
    descricao = models.TextField(blank=True,null=True)
    disponivel = models.BooleanField(default=True,null=True)
    foto=models.ImageField(upload_to='fotos_animais/', blank=True, null=True)

    def clean(self):
        erros = {}
        if not self.nome:
            erros['nome'] = 'O nome do animal é obrigatório.'
        elif len(self.nome) < 3:
            erros['nome'] = 'O nome do animal deve ter pelo menos 3 caracteres.'
        elif len(self.nome) > 100:
            erros['nome'] = 'O nome do animal não pode exceder 100 caracteres.'
        if self.data_nascimento is None:
            erros['data_nascimento'] = 'A data de nascimento é obrigatória.'
        elif self.data_nascimento > date.today():
            erros['data_nascimento'] = 'A data de nascimento não pode ser no futuro.'
        if self.sexo not in ['M', 'F']:
            erros['sexo'] = 'O sexo deve ser "M" para masculino ou "F" para feminino.'
        if not self.cor:
            erros['cor'] = 'A cor do animal é obrigatória.'
        elif len(self.cor) < 3:
            erros['cor'] = 'A cor do animal deve ter pelo menos 3 caracteres.'
        elif len(self.cor) > 50:
            erros['cor'] = 'A cor do animal não pode exceder 50 caracteres.'
        if self.raca is None:
            erros['raca'] = 'A raça do animal é obrigatória.'
        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return self.nome
    def idade(self):
        
        hoje = date.today()
        if self.data_nascimento is None:
            return 0
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade

    class Meta:
        verbose_name_plural = "Animais"
        ordering = ['nome']



class RacaOrdenada(Raca):
    class Meta:
        proxy = True
        ordering = ['nome']
    
    def mostre(self):
        return f'Raça: {self.nome} - Tipo: {self.tipo_animal.nome}'


