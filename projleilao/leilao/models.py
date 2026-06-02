from django.db import models

# Create your models here.

class Participante(models.Model):
    nome=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    endereco=models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Leilao(models.Model):
    dataInicio=models.DateField()
    horaInicio=models.TimeField()
    dataTermino=models.DateField()
    horaTermino=models.TimeField()

    def __str__(self):
        return f'Leilão: {self.dataInicio}-{self.horaInicio}/{self.dataTermino}-{self.horaTermino}'

class ItemLeilao(models.Model):
    titulo=models.CharField(max_length=100)
    descricao=models.TextField()
    lanceMinimo=models.DecimalField(max_digits=10,decimal_places=2)
    arrematado=models.BooleanField(default=False)
    leilao=models.ForeignKey(Leilao,on_delete=models.CASCADE,related_name='itens')
    
    def __str__(self):
        return f'{self.titulo}-{self.lanceMinimo}'
    
    @property
    def total_lances(self):
        valor_total=0
        for lance in self.lances.all():
            valor_total+=lance.valorLance
        return valor_total

class Lance(models.Model):
    valorLance=models.DecimalField(max_digits=10,decimal_places=2)
    horaLance=models.TimeField(auto_now_add=True)
    participante=models.ForeignKey(Participante,on_delete=models.SET_NULL,null=True,related_name="lances")
    itemLeilao=models.ForeignKey(ItemLeilao,on_delete=models.SET_NULL,null=True,related_name='lances')

    def __str__(self):
        return f'{self.itemLeilao}-{self.participante}-{self.valorLance}'

