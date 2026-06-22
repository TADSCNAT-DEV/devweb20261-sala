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
    
    @staticmethod
    def check_abrigo_group(user):
        return user.groups.filter(name='ABRIGO').exists()
    
def adoteme_context(request):
        context = {
            'IS_ADOTANTE': Utils.check_adotante(request.user),
            'IS_ABRIGO': Utils.check_abrigo(request.user),
        }
        return context