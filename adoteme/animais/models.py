from django.db import models

# Create your models here.

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=50)

class Raca(models.Model):
    nome = models.CharField(max_length=100)
    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.PROTECT,related_name='racas')

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    cor= models.CharField(max_length=50)
    disponivel= models.BooleanField(default=True)
    descricao= models.TextField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE,related_name='animais')
