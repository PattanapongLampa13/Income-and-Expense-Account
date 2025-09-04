from django.db import models
from django.contrib.auth.models import User

class IncomeExpense(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'รายรับ'),
        ('expense', 'รายจ่าย'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', null=True)

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.transaction_type} - {self.amount}"
