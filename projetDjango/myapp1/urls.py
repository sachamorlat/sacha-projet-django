from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inscription

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inscription/', inscription, name='inscription'),
    path('rechercher_voyages/', views.rechercher_voyages, name='rechercher_voyages'),
    path('reserver_voyage/<int:voyage_id>/', views.reserver_voyage, name='reserver_voyage'),
]