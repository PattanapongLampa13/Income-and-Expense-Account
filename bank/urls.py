from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('', views.login_view, name='login'),  # หน้าแรกเป็น login
    path('menu/', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('slip/', views.slip_view, name='slip'),
    path('digitolsum/', views.digitolsum_view, name='digitolsum'),
    path('register/', views.register_view, name='register'),
]