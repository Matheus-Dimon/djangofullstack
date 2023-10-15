from django.urls import path
from magazine_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  
    path('produtos/', views.lista_cadastro, name='cadastro'),
    path('cadastro/', views.newcad , name='listagem_produtos')]                                                    
