from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('income-expense/', views.income_expense_view, name='income_expense'),
]