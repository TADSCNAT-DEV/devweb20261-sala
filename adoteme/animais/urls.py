from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('listar/', views.listar_animais, name='listar_animais'),
    path('tipos/listar/', views.listar_tipos, name='listar_tipos'),
]
