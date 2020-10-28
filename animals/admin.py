from django.contrib import admin

from .models import Donation, Toy, User, Animal, Wish


# User custom class to override fields for User
class UserAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'keeper']
    fieldsets = [
        (None, {'fields': ['first_name','last_name']}),
        ('Authentication Info', {'fields': ['keeper', 'verified']}),
    ]
    list_display = ('last_name', 'first_name', 'auth_keeper')
    
class WishAdmin(admin.ModelAdmin):
    # each entry is a callable attribute on 'Wish'
    list_display = ('id', 'animal', 'toy')
    
class WishInLine(admin.TabularInline):
    model = Wish
    # extra = How many fields are available at once
    extra = 1
    

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'species', 'bio']})
    ]
    inlines = [WishInLine]
    search_fields = ['name', 'species']
    
admin.site.register(User, UserAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Toy)
admin.site.register(Wish, WishAdmin)
admin.site.register(Donation)