from django.contrib import admin
from .models import Zoo

class ZooAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Zoo Info', {'fields': ['city', 'st']}),
        (None, {'fields': ['accrs']}),
    ]
    
admin.site.register(Zoo, ZooAdmin)