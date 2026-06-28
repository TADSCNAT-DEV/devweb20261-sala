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

class FormUtils:
    @staticmethod
    def adicionar_erros_validacao_ao_formulario(form, erro_validacao):
        if hasattr(erro_validacao, 'message_dict'):
            for campo, mensagens in erro_validacao.message_dict.items():
                destino = campo if campo in form.fields else None
                for mensagem in mensagens:
                    form.add_error(destino, mensagem)
            return

        for mensagem in erro_validacao.messages:
            form.add_error(None, mensagem)
    
def adoteme_context(request):
        context = {
            'IS_ADOTANTE': Utils.check_adotante(request.user),
            'IS_ABRIGO': Utils.check_abrigo(request.user),
            'USUARIO': UsuarioService.obter_usuario(request.user.id) if request.user.is_authenticated else None,
        }
        return context