from django.urls import path

from teste.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carros/', views.carros, name='carros'),
    path('deletecarro/', views.deleteCarro, name='deletecarro'),
    path('fabricantes/', views.fabricantes, name='carros'),
    path('deletefabricante/', views.deleteFabricante, name='deletecarro'),
]