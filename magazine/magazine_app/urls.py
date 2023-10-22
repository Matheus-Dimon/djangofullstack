from django.urls import path
from magazine_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  
    path('produtos/', views.lista_cadastro, name='cadastro'),
    path('cadastro/', views.produtos_cadastrados , name='listagem_produtos'),
    path('trocas/', views.trocas , name='trocas'),
    ]                                                    
