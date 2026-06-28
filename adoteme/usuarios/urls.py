from django.urls import path

from usuarios.viewsclass.usuariosviews import AutoregistroView, EditarPerfilView

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', AutoregistroView.as_view(), name='autoregistro'),
    path('perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
]