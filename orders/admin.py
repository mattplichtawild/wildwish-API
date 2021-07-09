from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'wish', 'created_at')
    readonly_fields = ['created_at', 'updated_at', 'wish']
    fieldsets = [
        (None, {'fields': ['status', 'wish', 'created_at', 'updated_at']}),
        ('Ship to:', {'fields': ['']})
    ]
    
admin.site.register(Order, OrderAdmin)
