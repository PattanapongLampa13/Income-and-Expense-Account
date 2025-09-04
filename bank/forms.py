from django import forms
from .models import IncomeExpense

class IncomeExpenseForm(forms.ModelForm):
    class Meta:
        model = IncomeExpense
        fields = ['title', 'amount', 'transaction_type']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount', 'class': 'form-input'}),
            'transaction_type': forms.Select(attrs={'class': 'form-input'}),
        }
