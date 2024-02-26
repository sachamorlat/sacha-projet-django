from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rechercher_voyages/', views.rechercher_voyages, name='rechercher_voyages'),
    path('reserver_voyage/<int:voyage_id>/', views.reserver_voyage, name='reserver_voyage'),
]