from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('tipos/listar/', views.listar_tipos, name='listar_tipos'),
    path('tipos/atualizar/<int:id>/', views.atualizar_tipo_animal, name='atualizar_tipo_animal'),
    path('tipos/excluir/<int:id>/', views.excluir_tipo_animal, name='excluir_tipo_animal'),
    path('tipos/cadastrar/', views.cadastrar_tipo_animal, name='cadastrar_tipo_animal'),
    path('racas/cadastrar/', views.cadastrar_raca, name='cadastrar_raca'),
    path('racas/listar/', views.listar_racas, name='listar_racas'),
    path('racas/atualizar/<int:id>/', views.atualizar_raca, name='atualizar_raca'),
    path('racas/excluir/<int:id>/', views.excluir_raca, name='excluir_raca'),
    path('listar/', views.listar_animais, name='listar_animais'),
    path('cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('atualizar/<int:id>/', views.atualizar_animal, name='atualizar_animal'),
    path('excluir/<int:id>/', views.excluir_animal, name='excluir_animal'),
]
