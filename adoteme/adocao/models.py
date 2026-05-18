from django.db import models
from animais.models import Animal
from usuarios.models import Usuario
# Create your models here.

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