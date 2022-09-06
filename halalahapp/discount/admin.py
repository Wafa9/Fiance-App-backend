from django.contrib import admin
from .models import Discount

class DiscountAdmin (admin.ModelAdmin):
    list_display= ['key','website','code','icon','precent']
admin.site.register(Discount, DiscountAdmin)
