from django.shortcuts import render


from .models import IncomeExpense
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse

@csrf_exempt
def income_expense_view(request):
	if request.method == "POST":
		title = request.POST.get("title")
		amount = request.POST.get("amount")
		transaction_type = request.POST.get("transaction_type")
		if title and amount and transaction_type:
			IncomeExpense.objects.create(
				title=title,
				amount=amount,
				transaction_type=transaction_type
			)
		return HttpResponseRedirect(reverse("income_expense"))
	records = IncomeExpense.objects.all().order_by('-date')
	total_income = sum(r.amount for r in records if r.transaction_type == "income")
	total_expense = sum(r.amount for r in records if r.transaction_type == "expense")
	return render(request, "income_expense.html", {
		"records": records,
		"total_income": total_income,
		"total_expense": total_expense,
	})
