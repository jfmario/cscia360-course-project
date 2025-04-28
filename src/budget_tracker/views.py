
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from budget_tracker.models import Budget, BudgetTransaction, INCOME_CATEGORIES, EXPENSE_CATEGORIES
import budget_tracker.service as budget_tracker_svc

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

def balance(request):

    balance = budget_tracker_svc.calculate_balance()

    return render(request, 'htmx/balance.html', {
        'balance': balance
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
def transaction(request, transaction_id=None):

    if request.method == 'GET':
        transaction = BudgetTransaction.objects.get(pk=transaction_id)
        return render(request, 'htmx/transaction.html', {
            'transaction': transaction
        })

    if request.method == 'DELETE':
        budget_tracker_svc.delete_transaction(transaction_id)
        return HttpResponse('')

    if request.method == 'POST':

        transaction_type = request.POST.get('transaction_type')
        name = request.POST.get('name')
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        transaction = budget_tracker_svc.create_transaction(name, category, amount, transaction_type)

        return redirect(reverse('add-new-transaction-button', kwargs={ 'transaction_type': transaction_type }))

    if request.method == 'PUT':

        put = QueryDict(request.body)
        name = put.get('name')
        category = put.get('category')
        amount = put.get('amount')

        transaction = budget_tracker_svc.edit_transaction(transaction_id, name, category, amount)

        return render(request, 'htmx/transaction.html', {
            'transaction': transaction
        })

@csrf_exempt
def transactions(request, transaction_type, amount_sort=None):

    category = 'ALL'

    if request.method == 'POST':
        category = request.POST.get('category')

    if transaction_type == 'income':
        transactions = BudgetTransaction.objects.filter(is_income=True)
        categories = INCOME_CATEGORIES
    else:
        transactions = BudgetTransaction.objects.filter(is_expense=True)
        categories = EXPENSE_CATEGORIES
    if category != 'ALL':
        transactions = transactions.filter(category=category)

    if amount_sort == 'asc':
        transactions = transactions.order_by('amount')
    if amount_sort == 'desc':
        transactions = transactions.order_by('-amount')

    total = sum([e.amount for e in transactions.all()])

    return render(request, 'htmx/transactions.html', {
        'filter_category': category,
        'categories': categories,
        'transaction_type': transaction_type,
        'transactions': transactions,
        'total': total
    })

def transaction_form(request, transaction_type):
    categories = INCOME_CATEGORIES
    if transaction_type == 'expense':
        categories = EXPENSE_CATEGORIES
    return render(request, 'htmx/new-transaction-form.html', {
        'categories': categories,
        'transaction_type': transaction_type
    })