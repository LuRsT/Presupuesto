from django.db import models


class FutureTransaction(models.Model):
    
    description = models.CharField(max_length=100)
    
    date = models.DateField(null=True)
    
    amount = models.FloatField()
    
    priority = models.PositiveIntegerField()
    
    def __str__(self):
        return self.description


def get_future_transaction_amounts_by_month():
    amounts_by_month = []
    for month_number in range(1, 13):
        transactions = FutureTransaction.objects.filter(date__month=month_number)
        transaction_amounts = [transaction.amount for transaction in transactions]
        month_total = sum(transaction_amounts)
        amounts_by_month.append(month_total)
    
    return amounts_by_month
