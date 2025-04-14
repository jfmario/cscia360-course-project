
from django.http import QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from budget_tracker.models import Budget, BudgetTransaction, INCOME_CATEGORIES, EXPENSE_CATEGORIES

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

def delete_transaction_from(request, transaction_id):
    transaction = BudgetTransaction.objects.get(pk=transaction_id)
    return render(request, 'htmx/delete-transaction-form.html', {
        'transaction': transaction
    })

def edit_transaction_from(request, transaction_id):

    transaction = BudgetTransaction.objects.get(pk=transaction_id)

    categories = INCOME_CATEGORIES
    if transaction.is_expense:
        categories = EXPENSE_CATEGORIES

    return render(request, 'htmx/edit-transaction-form.html', {
        'categories': categories,
        'transaction': transaction
    })

@csrf_exempt
def transaction(request, transaction_id):

    if request.method == 'GET':
        transaction = BudgetTransaction.objects.get(pk=transaction_id)
        return render(request, 'htmx/transaction.html', {
            'transaction': transaction
        })

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

    if request.method == 'PUT':

        put = QueryDict(request.body)
        name = put.get('name')
        category = put.get('category')
        amount = put.get('amount')

        transaction = BudgetTransaction.objects.get(pk=transaction_id)
        transaction.name = name
        transaction.category = category
        transaction.amount = amount
        transaction.save()

        return render(request, 'htmx/transaction.html', {
            'transaction': transaction
        })

def transactions(request, transaction_type):
    if transaction_type == 'income':
        transactions = BudgetTransaction.objects.filter(is_income=True)
    else:
        transactions = BudgetTransaction.objects.filter(is_expense=True)
    return render(request, 'htmx/transactions.html', {
        'transactions': transactions
    })

def transaction_form(request, transaction_type):
    categories = INCOME_CATEGORIES
    if transaction_type == 'expense':
        categories = EXPENSE_CATEGORIES
    return render(request, 'htmx/new-transaction-form.html', {
        'categories': categories,
        'transaction_type': transaction_type
    })