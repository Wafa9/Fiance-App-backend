from django.contrib import admin
from .models import Transaction
from .models import FinancialDeateails
# Register your models here.


class TransactionAdmin (admin.ModelAdmin):
    list_display = ['type', 'amount', 'owner', 'category', 'date']


admin.site.register(Transaction,  TransactionAdmin)
admin.site.register(FinancialDeateails)
