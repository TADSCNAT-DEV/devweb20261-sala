from adoteme.adocao.models import ProcessoAdocao, Comentario, DocumentoAdocao
from django.core.exceptions import ValidationError
class AdocacaoService:
    @staticmethod
    def criar_processo_adocao(adotante, animal):
        processo = ProcessoAdocao(adotante=adotante, animal=animal)
        try:
            processo.full_clean()  # Valida os dados do processo de adoção
            processo.save()  # Salva o processo no banco de dados
        except ValidationError as e:
            raise e
        return processo
    @staticmethod
    def adicionar_comentario(processo_adocao, autor, texto):
        comentario = Comentario(processo_adocao=processo_adocao, autor=autor, texto=texto)
        try:
            comentario.full_clean()  # Valida os dados do comentário
            comentario.save()  # Salva o comentário no banco de dados
        except ValidationError as e:
            raise e
        return comentario
    @staticmethod
    def adicionar_documento(processo_adocao, descricao, arquivo):
        documento = DocumentoAdocao(processo_adocao=processo_adocao, descricao=descricao, arquivo=arquivo)
        try:
            documento.full_clean()  # Valida os dados do documento
            documento.save()  # Salva o documento no banco de dados
        except ValidationError as e:
            raise e
        return documento
    @staticmethod
    def atualizar_status(processo_adocao, status):
        processo_adocao.status = status
        try:
            processo_adocao.full_clean()  # Valida os dados do processo de adoção
            processo_adocao.save()  # Salva as alterações no banco de dados
        except ValidationError as e:
            raise e
        return processo_adocao