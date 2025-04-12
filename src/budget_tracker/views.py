
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from budget_tracker.models import Budget, BudgetTransaction, INCOME_CATEGORIES

# Create your views here.
def home_page(request):
    budgets = Budget.objects.all()
    return render(request, 'index.html', {
        'budgets': budgets
    })

def add_new_transaction_button(request, transaction_type):
    return render(request, 'htmx/add-new-transaction-button.html', {
        'transaction_type': transaction_type
    })

@csrf_exempt
def transaction(request):

    if request.method == 'POST':

        transaction_type = request.POST.get('transaction_type')
        name = request.POST.get('name')
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        is_income = False
        is_expense = False

        if transaction_type == 'income':
            is_income = True
        if transaction_type == 'expense':
            is_expense = True

        entry = BudgetTransaction(
            is_income=is_income,
            is_expense=is_expense,
            name=name,
            category=category,
            amount=amount
        )

        entry.save()

    return redirect(reverse('add-new-transaction-button', kwargs={ 'transaction_type': transaction_type }))

def transaction_form(request, transaction_type):
    categories = INCOME_CATEGORIES
    return render(request, 'htmx/transaction-form.html', {
        'categories': categories,
        'transaction_type': transaction_type
    })