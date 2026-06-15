from django.db import models
from usuarios.models import Usuario
from animais.models import Animal
import datetime
# Create your models here.

STATUS_CHOICES =[('EM_ANALISE', 'Em Análise'),
        ('APROVADA', 'Aprovada'),
        ('REPROVADA', 'Reprovada'),]

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='adocoes/documentos/')
    enviado_em = models.DateTimeField(auto_now_add=True)
    processo_adocao = models.ForeignKey('ProcessoAdocao', on_delete=models.CASCADE, related_name='documentos')
    def __str__(self):
        return self.descricao
 
class ProcessoAdocao(models.Model):
    criadaem=models.DateField(auto_now_add=True)
    atualizadaem=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='EM_ANALISE')
    animal=models.ForeignKey(Animal,on_delete=models.PROTECT,related_name='processos_adocao')
    adotante=models.ForeignKey(Usuario,on_delete=models.PROTECT,related_name='processos_adocao_adotante')
    avaliador=models.ForeignKey(Usuario,on_delete=models.PROTECT,related_name='processos_adocao_avaliador')
    comentarios_avaliadores=models.ManyToManyField(Usuario,through='Comentario',related_name='comentarios_avaliadores')

    def atrasada(self):
        if self.status == 'EM_ANALISE':
            dias_em_analise = (datetime.date.today() - self.criadaem).days
            return dias_em_analise > 7
        return False

    def __str__(self):
        return f'{self.id}-{self.animal.nome}-{self.adotante.nome}-{self.avaliador.nome}'

    class Meta:
        verbose_name='Processo de Adoção'
        verbose_name_plural='Processos de Adoção'

class Comentario(models.Model):
    processo_adocao=models.ForeignKey(ProcessoAdocao,on_delete=models.PROTECT,related_name='comentarios')
    avaliador=models.ForeignKey(Usuario,on_delete=models.PROTECT,related_name='comentarios')
    texto=models.TextField()
    realizado_em=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.avaliador}-{self.processo_adocao.id}-{self.texto}'
    
    class Meta:
        verbose_name='Comentário'
        verbose_name_plural='Comentários'