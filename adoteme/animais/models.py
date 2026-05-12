from django.db import models

# Create your models here.

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'TipoAnimal: {self.nome}'

class Raca(models.Model):
    nome = models.CharField(max_length=100)
    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.PROTECT,related_name='racas')

    def __str__(self):
        return f'{self.nome} ({self.tipo_animal.nome})'

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    cor= models.CharField(max_length=50)
    disponivel= models.BooleanField(default=True)
    descricao= models.TextField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE,related_name='animais')

    def __str__(self):
        return f'Animal: {self.nome} ({self.raca})'
    @property
    def idade(self):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.dataNascimento.year - ((hoje.month, hoje.day) < (self.dataNascimento.month, self.dataNascimento.day))
        return idade