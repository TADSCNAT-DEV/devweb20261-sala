from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('tipos/', views.listar_tipos_animais, name='listar_tipos_animais'),
    path('tipos/<int:tipo_id>/animais/', views.listar_animais_por_tipo, name='listar_animais_por_tipo'),
]