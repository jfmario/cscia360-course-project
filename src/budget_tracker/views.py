
from django.shortcuts import render

from budget_tracker.models import Budget

# Create your views here.
def home_page(request):
    budgets = Budget.objects.all()
    return render(request, 'index.html', {
        'budgets': budgets
    })
