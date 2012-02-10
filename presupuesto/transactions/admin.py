from django.contrib.admin import ModelAdmin, site

from presupuesto.transactions.models import FutureTransaction


class FutureTransactionAdmin(ModelAdmin):

    list_display = ("description", "date", "amount", "priority")
    
    list_filter = ("date", )
    
    ordering = ("date", "priority", "amount")


site.register(FutureTransaction, FutureTransactionAdmin)
