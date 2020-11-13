from animals.models import Animal
from django.contrib import admin
from .models import Zoo
    
class AnimalInLine(admin.TabularInline):
    model = Animal
    extra = 3

class ZooAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Zoo Info', {'fields': ['city', 'st']}),
        (None, {'fields': ['accrs']}),
    ]
    inlines = [AnimalInLine]
    search_fields = ['name']
admin.site.register(Zoo, ZooAdmin)