from django.contrib import admin
from .models import IncomeExpense

@admin.register(IncomeExpense)
class IncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "transaction_type", "date")
