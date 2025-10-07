from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.usuario_login, name='login'),
    path('cadastro/', views.usuario_cadastro, name='cadastro'),
]
