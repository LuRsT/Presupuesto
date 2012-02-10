from collections import OrderedDict

from django.db import models

from presupuesto.utils import reorder_iterable


class FutureTransaction(models.Model):
    
    description = models.CharField(max_length=100)
    
    date = models.DateField(null=True, blank=True)
    
    amount = models.FloatField()
    
    priority = models.PositiveIntegerField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        default=1,
        )
    
    def __str__(self):
        return self.description


def get_future_transaction_amounts_by_month(initial_month):
    amounts_by_month = OrderedDict()
    ordered_months = reorder_iterable(range(1, 13), initial_month)
    for month_number in ordered_months:
        transactions = FutureTransaction.objects.filter(date__month=month_number)
        transaction_amounts = [transaction.amount for transaction in transactions]
        month_total = sum(transaction_amounts)
        
        amounts_by_month[month_number] = month_total
    
    return amounts_by_month
