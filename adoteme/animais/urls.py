from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('tipos/', views.listar_tipos_animais, name='listar_tipos'),
]
