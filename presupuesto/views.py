from collections import OrderedDict
from datetime import datetime

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from presupuesto.budgets.models import Category
from presupuesto.transactions.models import get_future_transaction_amounts_by_month


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
    start_balance = float(open("BALANCE.txt").read())
    
    today = datetime.today()
    current_month = today.month - 1
    
    amount_by_category = _get_amount_by_category()
    transaction_amount_by_month = _reorder_iterable(get_future_transaction_amounts_by_month(), current_month)
    
    amounts_by_month = zip(
        transaction_amount_by_month, *_reorder_columns_in_rows(amount_by_category.values(), current_month))
    
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
    
    months = _reorder_iterable(MONTH_LABELS, current_month)
    
    context = {
        'start_balance': start_balance,
        'months': months,
        'amount_by_category': amount_by_category,
        'transaction_amount_by_month': transaction_amount_by_month,
        'variation_by_month': variation_by_month,
        'balance_by_month': balance_by_month,
        'balance_before_income_by_month': balance_before_income_by_month,
        }
    return render_to_response("report.html", RequestContext(request, context))


def _reorder_iterable(iterable, new_start):
    first_half = iterable[:new_start]
    last_half = iterable[new_start:]
    return last_half + first_half


def _reorder_columns_in_rows(rows, new_start_column):
    reordered_rows = []
    for row in rows:
        reordered_rows.append(_reorder_iterable(row, new_start_column))
    
    return reordered_rows


def _get_amount_by_category():
    amount_by_category = OrderedDict()
    for category in Category.objects.order_by("default_amount"):
        amount_by_category[category] = category.get_amounts_by_month()
    
    return amount_by_category
