
from django.test import TestCase

from budget_tracker.models import BudgetTransaction
import budget_tracker.service as budget_tracker_svc

class BudgetTrackerTest(TestCase):

    def test_add_transaction(self):
        self.assertEqual(BudgetTransaction.objects.count(), 0)
        t = budget_tracker_svc.create_transaction("Royalties", "Other", 100.0, 'income')
        self.assertEqual(BudgetTransaction.objects.count(), 1)
        self.assertEqual(t.name, 'Royalties')
        self.assertEqual(t.category, 'Other')
        self.assertEqual(t.amount, 100.0)
        self.assertEqual(t.is_income, True)
        self.assertEqual(t.is_expense, False)

    def test_edit_transaction(self):
        self.assertEqual(BudgetTransaction.objects.count(), 0)
        t = budget_tracker_svc.create_transaction("Royalties", "Other", 100.0, 'income')
        transaction_id = t.id
        budget_tracker_svc.edit_transaction(transaction_id, 'Royalties', 'Other', 200.0)
        t = BudgetTransaction.objects.get(pk=transaction_id)
        self.assertEqual(t.name, 'Royalties')
        self.assertEqual(t.category, 'Other')
        self.assertEqual(t.amount, 200.0)
        self.assertEqual(t.is_income, True)
        self.assertEqual(t.is_expense, False)
        
