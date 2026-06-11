from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('listar/', views.listar_animais, name='listar_animais'),
    path('tipos/listar/', views.listar_tipos, name='listar_tipos'),
    path('racas/listar/',views.listar_racas,name='listar_racas'),
    path('cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('atualizar/<int:id>/', views.atualizar_animal, name='atualizar_animal'),
    path('excluir/<int:id>/', views.excluir_animal, name='excluir_animal'),
]
