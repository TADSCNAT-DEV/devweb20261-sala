from usuarios.models import Usuario,Perfil
from django.core.exceptions import ValidationError

class UsuarioService:
    @staticmethod
    def criar_usuario(nome, email,username,cpf, password, tipo_usuario):
        usuario = Usuario(nome=nome, email=email, username=username, cpf=cpf, tipo_usuario=tipo_usuario,password=password)
        try:
            usuario.full_clean()  # Valida os dados do usuário
            usuario.save()  # Salva o usuário no banco de dados
            perfil = Perfil(usuario=usuario)
            perfil.save()  # Salva o perfil no banco de dados
        except ValidationError as e:
            raise e
        return usuario

    @staticmethod
    def atualizar_usuario(usuario_id, nome=None,  password=None):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")
        if nome is not None:
            usuario.nome = nome
        if password is not None:
            usuario.password = password
        try:
            usuario.full_clean()  # Valida os dados do usuário
            usuario.save()  # Salva as alterações no banco de dados
        except ValidationError as e:
            raise e
        return usuario

    @staticmethod
    def excluir_usuario(usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.delete()
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")

    @staticmethod
    def obter_usuario(usuario_id):
        try:
            return Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def consultar_tipo_usuario(username):
        try:
            usuario = Usuario.objects.get(username=username)
            return usuario.tipo_usuario
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def buscar_usuarios_por_nome(nome=None, tipo_usuario=None):
        usuarios = Usuario.objects.all()
        if nome:
            usuarios = usuarios.filter(nome__icontains=nome)
        if tipo_usuario:
            usuarios = usuarios.filter(tipo_usuario=tipo_usuario)
        return usuarios

    @staticmethod
    def atualizar_perfil(usuario_id, comprovante_endereco=None, bio=None, avatar=None):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")
        
        if Perfil.objects.filter(usuario=usuario).exists():
            perfil=usuario.perfil
        else:
            perfil=Perfil(usuario=usuario)
        if comprovante_endereco:
            perfil.comprovante_endereco = comprovante_endereco
        if bio:
            perfil.bio = bio
        if avatar:
            perfil.avatar = avatar
        perfil.save()
        return perfil