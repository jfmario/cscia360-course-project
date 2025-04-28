
from budget_tracker.models import BudgetTransaction

def create_transaction(name, category, amount, transaction_type):

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

    return entry

def edit_transaction(transaction_id, name, category, amount):
    transaction = BudgetTransaction.objects.get(pk=transaction_id)
    transaction.name = name
    transaction.category = category
    transaction.amount = amount
    transaction.save()
    return transaction

def delete_transaction(transaction_id):
    transaction = BudgetTransaction.objects.get(pk=transaction_id)
    transaction.delete()

def calculate_balance():

    transactions = BudgetTransaction.objects.all()

    balance = 0

    for transaction in transactions:
        if transaction.is_income:
            balance += transaction.amount
        if transaction.is_expense:
            balance -= transaction.amount
    
    return balance