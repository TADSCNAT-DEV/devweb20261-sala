from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(User):
    nome=models.CharField(max_length=100)
    cpf=models.CharField(max_length=11)
    tipo=models.CharField(max_length=1,choices=[('1','ADOTANTE'),('2','AVALIADOR')])

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    usuario=models.OneToOneField(Usuario,on_delete=models.CASCADE,related_name='perfil')
    avatar=models.ImageField(upload_to='usuarios/avatares/',null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    comprovanteEndereco=models.FileField(upload_to='usuarios/comprovantes/',null=True,blank=True)  
    def __str__(self):
        return self.usuario.nome