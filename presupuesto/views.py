from collections import OrderedDict
from datetime import datetime

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from presupuesto.budgets.models import Category
from presupuesto.transactions.models import get_future_transaction_amounts_by_month,\
    FutureTransaction
from presupuesto.utils import get_balance, reorder_iterable


MONTH_LABELS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    )


def home(request):
    start_balance = get_balance()
    
    current_month = datetime.today().month - 1
    
    amount_by_category = _get_amount_by_category(current_month)
    
    transaction_amount_by_month = get_future_transaction_amounts_by_month(
        current_month)
    
    amounts_by_month = amount_by_category.values() + \
        [transaction_amount_by_month.values()]
    amounts_by_month = zip(*amounts_by_month)
    
    variation_by_month = map(sum, amounts_by_month)
    
    balance_by_month = []
    last_balance = start_balance
    for balance in variation_by_month:
        last_balance += balance
        balance_by_month.append(last_balance)
    
    balance_before_income_by_month = []
    last_month_balance = start_balance
    for month_number, month_balance in enumerate(balance_by_month):
        outcome_amounts = [
            amount for amount in amounts_by_month[month_number] if amount < 0]
        month_outcome = sum(outcome_amounts)
        balance_before_income = last_month_balance + month_outcome
        balance_before_income_by_month.append(balance_before_income)
        
        last_month_balance = month_balance
    
    months = reorder_iterable(MONTH_LABELS, current_month)
    
    unsheduled_transactions = FutureTransaction.objects \
        .filter(date__isnull=True) \
        .order_by("priority", "-amount")
    
    context = {
        'start_balance': start_balance,
        'months': months,
        'amount_by_category': amount_by_category,
        'transaction_amount_by_month': transaction_amount_by_month,
        'variation_by_month': variation_by_month,
        'balance_by_month': balance_by_month,
        'balance_before_income_by_month': balance_before_income_by_month,
        'unsheduled_transactions': unsheduled_transactions,
        }
    return render_to_response("report.html", RequestContext(request, context))


def _get_amount_by_category(initial_month):
    amount_by_category = OrderedDict()
    for category in Category.objects.order_by("default_amount"):
        amount_by_category[category] = reorder_iterable(
            category.get_amounts_by_month(), initial_month)
    
    return amount_by_category
