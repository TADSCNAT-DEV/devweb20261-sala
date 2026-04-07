from django.urls import path
from . import views

app_name = 'enquete'

urlpatterns = [
    path('', views.index, name='index'),
    path('votar/', views.votar, name='votar'),
]
