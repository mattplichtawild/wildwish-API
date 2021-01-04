from animals.models import Animal
from django.contrib import admin
from .models import Zoo
    
class AnimalInLine(admin.TabularInline):
    model = Animal
    extra = 3

class ZooAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'st', 'website']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Zoo Info', {'fields': ['website', 'city', 'st', 'zip']}),
        (None, {'fields': ['accrs']}),
    ]
    # inlines = [AnimalInLine]
    search_fields = ['name', 'st']
admin.site.register(Zoo, ZooAdmin)