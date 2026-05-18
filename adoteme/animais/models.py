from django.db import models

# Create your models here.

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Tipos de Animais"
        ordering = ['nome']

class Raca(models.Model):
    nome = models.CharField(max_length=50)
    tipo_animal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE,related_name='racas')

    def __str__(self):
        return f"{self.tipo_animal.nome} ({self.nome})"
    
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
    def __str__(self):
        return self.nome
    def idade(self):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade

    class Meta:
        verbose_name_plural = "Animais"
        ordering = ['nome']