from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('painel/', views.PainelView.as_view(), name='painel'),
    
    path('login/', auth_views.LoginView.as_view(template_name='funcionarios/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]