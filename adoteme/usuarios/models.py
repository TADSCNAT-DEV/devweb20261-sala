from django.db import models
from django.contrib.auth.models import User
from principal.cloudinary import get_image_field,get_file_field

# Create your models here.

class Usuario(User):
    nome=models.CharField(max_length=100)
    cpf=models.CharField(max_length=11, unique=True)
    tipo_usuario=models.CharField(max_length=20,choices=[('ADOTANTE','ADOTANTE'),('ABRIGO','ABRIGO')],default='ADOTANTE')

    def cpf_formatado(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
    
    def clean(self):
        erros = {}
        if self.tipo_usuario not in ['ADOTANTE', 'ABRIGO']:
            erros['tipo_usuario'] = 'O tipo de usuário deve ser "ADOTANTE" ou "ABRIGO".'
        if not self.email:
            erros['email'] = 'O email é obrigatório.'
        elif len(self.email) > 254:
            erros['email'] = 'O email não pode exceder 254 caracteres.'
        if not self.username:
            erros['username'] = 'O nome de usuário é obrigatório.'
        elif len(self.username) < 3:
            erros['username'] = 'O nome de usuário deve ter pelo menos 3 caracteres.'
        if not self.nome:
            erros['nome'] = 'O nome é obrigatório.'
        elif len(self.nome) < 3:
            erros['nome'] = 'O nome deve ter pelo menos 3 caracteres.'
        elif len(self.nome) > 100:
            erros['nome'] = 'O nome não pode exceder 100 caracteres.'
        if not self.cpf:
            erros['cpf'] = 'O CPF é obrigatório.'
        elif len(self.cpf) != 11 or not self.cpf.isdigit():
            erros['cpf'] = 'O CPF deve conter exatamente 11 dígitos numéricos.'
        if Usuario.objects.filter(cpf=self.cpf).exclude(id=self.id).exists():
            erros['cpf'] = 'O CPF já está em uso por outro usuário.'
        if Usuario.objects.filter(email=self.email).exclude(id=self.id).exists():
            erros['email'] = 'O email já está em uso por outro usuário.'
        if Usuario.objects.filter(username=self.username).exclude(id=self.id).exists():
            erros['username'] = 'O nome de usuário já está em uso por outro usuário.'
        if self.password:
            if len(self.password) < 8:
                erros['password'] = 'A senha deve ter pelo menos 8 caracteres.'
            elif not self.password.startswith(('pbkdf2_', 'argon2$', 'bcrypt$', 'scrypt$')):
                self.set_password(self.password)  # Hash da senha
        return erros

    def __str__(self):
        return self.nome
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    comprovante_endereco = get_file_field(upload_to='usuarios/comprovantes_endereco/', blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    avatar=get_image_field(upload_to='usuarios/avatars/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"
