from django.db import models

# Create your models here.

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='adocoes/documentos/')
    enviado_em = models.DateTimeField(auto_now_add=True)
    processo_adocao = models.ForeignKey('ProcessoAdocao', on_delete=models.CASCADE, related_name='documentos')
    def __str__(self):
        return self.descricao