"""
URL configuration for budget_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import budget_tracker.views

urlpatterns = [
    path('', budget_tracker.views.home_page),
    path('add-new-transaction-button/<slug:transaction_type>', budget_tracker.views.add_new_transaction_button, name='add-new-transaction-button'),
    path('transaction', budget_tracker.views.transaction, name='transaction'),
    path('transactions/<slug:transaction_type>', budget_tracker.views.transactions, name='transactions'),
    path('transaction-form/<slug:transaction_type>', budget_tracker.views.transaction_form, name='transaction-form'),
    path('admin/', admin.site.urls),
]
