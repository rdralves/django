from django.urls import path


from app_usuarios import views

urlpatterns = [
    path('cadastro/',  views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('sair/', views.sair, name="sair"),
    path('home', views.home, name='home'),
    
    ]