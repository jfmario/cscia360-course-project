from django.db import models

INCOME_CATEGORIES = [
    'Salary/Wages',
    '1099 Income',
    'Investments',
    'Benefits',
    'Other'
]

EXPENSE_CATEGORIES = [
    'Housing',
    'Transportation',
    'Food',
    'Utilities',
    'Healthcare',
    'Liabilities',
    'Entertainment',
    'Shopping',
    'Investments',
    'Other'
]

# deprecated
class Budget(models.Model):
    
    name = models.CharField(max_length=30)

class BudgetTransaction(models.Model):

    is_income = models.BooleanField(default=False)
    is_expense = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    amount = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name