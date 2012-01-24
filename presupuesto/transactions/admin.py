from django.contrib.admin import ModelAdmin, site

from presupuesto.transactions.models import FutureTransaction


class FutureTransactionAdmin(ModelAdmin):

    list_display = ("description", "amount", "priority")
    
    list_filter = ("date", )


site.register(FutureTransaction, FutureTransactionAdmin)
