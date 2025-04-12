
from django.shortcuts import render

from budget_tracker.models import Budget, INCOME_CATEGORIES

# Create your views here.
def home_page(request):
    budgets = Budget.objects.all()
    return render(request, 'index.html', {
        'budgets': budgets
    })

def transaction_form(request, transaction_type):
    categories = INCOME_CATEGORIES
    return render(request, 'htmx/transaction-form.html', {
        'categories': categories,
        'transaction_type': transaction_type
    })