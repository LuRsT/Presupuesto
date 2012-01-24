from django.contrib.admin import ModelAdmin, site, TabularInline

from presupuesto.budgets.models import Category, SpecificMonthAmount


class SpecificMonthAmountInLineAdmin(TabularInline):
    model = SpecificMonthAmount
    
    max_num = 12


class CategoryAdmin(ModelAdmin):
    
    list_display = ('description', 'default_amount')
    
    inlines = [SpecificMonthAmountInLineAdmin]

site.register(Category, CategoryAdmin)
