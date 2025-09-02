from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('', views.menu, name='menu'),  # หน้าแรก
    path('menu/', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
]