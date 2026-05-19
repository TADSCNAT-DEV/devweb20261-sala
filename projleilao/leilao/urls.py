from django.urls import path
from . import views

app_name = 'leilao'

urlpatterns = [
   path('', views.index, name='index'),
   path('leilao/<int:leilao_id>/itens/', views.listar_itens_leilao, name='listar_itens_leilao'),
]