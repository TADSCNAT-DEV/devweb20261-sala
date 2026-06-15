from django.db import models
from animais.models import Animal
from usuarios.models import Usuario
from django.core.exceptions import ValidationError
# Create your models here.
import datetime
class ProcessoAdocao(models.Model):
    STATUS_CHOICES = [
        ('EM_ANALISE', 'Em Análise'),
        ('APROVADA', 'Aprovada'),
        ('REPROVADA', 'Reprovada'),
    ]
    adotante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='processos_adocao_adotante')
    avaliador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos_adocao_avaliador')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='processos_adocao')
    criadaem= models.DateTimeField(auto_now_add=True)
    atualizadaem = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM_ANALISE')
    comentarios=models.ManyToManyField(Usuario, blank=True, through='Comentario',related_name='comentarios_usuario')

    def clean(self):
        erros = {}
        if self.adotante and self.adotante.tipo_usuario != 'ADOTANTE':
            erros['adotante'] = 'O usuário deve ser do tipo ADOTANTE.'
        if self.avaliador and self.avaliador.tipo_usuario != 'ABRIGO':
            erros['avaliador'] = 'O usuário avaliador deve ser do tipo ABRIGO.'
        if self.animal is None:
            erros['animal'] = 'O animal é obrigatório.'
        elif not self.animal.disponivel:
            erros['animal'] = 'O animal não está disponível para adoção.'
        if erros:
            raise ValidationError(erros)
    
    def atrasada(self):
        if self.status == 'EM_ANALISE':
            dias_em_analise = (datetime.date.today() - self.criadaem).days
            return dias_em_analise > 7
        return False

    def __str__(self):
        return f"Processo de Adoção: {self.adotante.nome} - {self.animal.nome} ({self.status})"

class Comentario(models.Model):
    processo_adocao = models.ForeignKey(ProcessoAdocao, on_delete=models.CASCADE, related_name='comentarios_processo')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios_autor')
    texto = models.TextField()
    realizadoem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.nome} em {self.realizadoem.strftime('%Y-%m-%d %H:%M:%S')}"

class DocumentoAdocao(models.Model):
    processo_adocao = models.ForeignKey(ProcessoAdocao, on_delete=models.CASCADE, related_name='documentos')
    descricao = models.CharField(max_length=100)
    enviadoem = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='adocao/documentos/')

    def __str__(self):
        return f"Documento: {self.descricao} para {self.processo_adocao}"