from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'wish', 'created_at')
    readonly_fields = ['created_at', 'updated_at', 'wish']
    # street = Order.wish.animal.zoo.street
    fieldsets = [
        (None, {'fields': ['status', 'wish', ('created_at', 'updated_at')]}),
        # ('Ship to:', {'fields': ['street']})
    ]
    
admin.site.register(Order, OrderAdmin)
