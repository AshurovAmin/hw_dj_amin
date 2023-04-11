from django.contrib import admin

from .models import Item, Purchase

admin.site.register(Item)
admin.site.register(Purchase)

# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'age', 'item', 'data_purchase']
#
# admin.site.register(Purchase, PurchaseAdmin)
