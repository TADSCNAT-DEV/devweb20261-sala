from usuarios.services import UsuarioService
class Utils:
    @staticmethod
    def check_adotante(user):
        tipo=UsuarioService.consultar_tipo_usuario(user.username)
        if tipo == 'ADOTANTE':
            return True
        return False
    @staticmethod
    def check_abrigo(user):
        tipo=UsuarioService.consultar_tipo_usuario(user.username)
        if tipo == 'ABRIGO':
            return True
        return False