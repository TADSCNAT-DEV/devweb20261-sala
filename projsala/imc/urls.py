from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('jose',views.jose,name='jose'),
    path('tabuada/<int:valor>/',views.tabuada,name='tabuada'),
    path('calcular_imc/<int:altura>/<int:peso>/',views.calcular_imc,name='calcular_imc'),
]