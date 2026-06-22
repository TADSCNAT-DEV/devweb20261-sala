from django.urls import path
from . import views
from principal.viewsclass.principal import PrincipalView

app_name = 'principal'

urlpatterns = [
    path('', PrincipalView.as_view(), name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adoteme/', views.index_logado, name='index_logado'),
]