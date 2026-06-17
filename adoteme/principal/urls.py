from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adoteme/', views.index_logado, name='index_logado'),
]