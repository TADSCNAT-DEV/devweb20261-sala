from django.urls import path
from animais.viewsclass.racasviews import RacaListView, RacaSalvarView, RacaAtualizarView,RacaExcluirView
from animais.viewsclass.animaisviews import AnimalListView, AnimalSalvarView, AnimalAtualizarView, AnimalExcluirView
from animais.viewsclass.tipoanimalviews import (
    TipoAnimalListView,
    TipoAnimalSalvarView,
    TipoAnimalAtualizarView,
    TipoAnimalExcluirView,
)

app_name = 'animais'

urlpatterns = [
    path('tipos/listar/', TipoAnimalListView.as_view(), name='listar_tipos'),
    path('racas/listar/', RacaListView.as_view(), name='listar_racas'),
    path('tipos/atualizar/<int:id>/', TipoAnimalAtualizarView.as_view(), name='atualizar_tipo_animal'),
    path('tipos/excluir/<int:id>/', TipoAnimalExcluirView.as_view(), name='excluir_tipo_animal'),
    path('tipos/cadastrar/', TipoAnimalSalvarView.as_view(), name='cadastrar_tipo_animal'),
    path('racas/cadastrar/', RacaSalvarView.as_view(), name='cadastrar_raca'),
    path('racas/atualizar/<int:id>/', RacaAtualizarView.as_view(), name='atualizar_raca'),
    path('racas/excluir/<int:id>/', RacaExcluirView.as_view(), name='excluir_raca'),
    path('listar/', AnimalListView.as_view(), name='listar_animais'),
    path('cadastrar/', AnimalSalvarView.as_view(), name='cadastrar_animal'),
    path('atualizar/<int:id>/', AnimalAtualizarView.as_view(), name='atualizar_animal'),
    path('excluir/<int:id>/', AnimalExcluirView.as_view(), name='excluir_animal'),
]
