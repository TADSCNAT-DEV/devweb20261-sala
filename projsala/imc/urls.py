from django.urls import path
from . import views

app_name = 'imc'

urlpatterns=[
    path('',views.index,name='index'),
    path('jose',views.jose,name='jose'),
    path('tabuada/<int:valor>/',views.tabuada,name='tabuada'),
    path('calcular_imc/<int:altura>/<int:peso>/',views.calcular_imc,name='calcular_imc'),
    path('calcular_novo/',views.calcular,name='calcular'),
    path('mensagem/',views.mensagem,name='mensagem'),
    path('tabela_imc/',views.tabela_imc,name='tabela_imc'),
]