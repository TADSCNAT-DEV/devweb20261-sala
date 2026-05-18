from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(User):
    nome=models.CharField(max_length=100)
    cpf=models.CharField(max_length=11, unique=True)
    tipo_usuario=models.CharField(max_length=20,choices=[('ADOTANTE','ADOTANTE'),('ABRIGO','ABRIGO')],default='ADOTANTE')

    def __str__(self):
        return self.nome
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    comprovante_endereco = models.FileField(upload_to='usuarios/comprovantes_endereco/', blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    avatar=models.ImageField(upload_to='usuarios/avatars/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"