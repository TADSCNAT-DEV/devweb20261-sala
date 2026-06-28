from django.urls import path
from . import views
from principal.viewsclass.principal import PrincipalView,PrincipalLogadoView,ContatoView

app_name = 'principal'

urlpatterns = [
    path('', PrincipalView.as_view(), name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adoteme/', PrincipalLogadoView.as_view(), name='index_logado'),
    path('contato/', ContatoView.as_view(), name='contato'),
]