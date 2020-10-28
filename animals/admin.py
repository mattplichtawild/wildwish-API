from django.contrib import admin

from .models import Donation, Toy, User, Animal, Wish


# User custom class to override fields for User
class UserAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'keeper']
    fieldsets = [
        (None, {'fields': ['first_name','last_name']}),
        ('Authentication Info', {'fields': ['keeper', 'verified']}),
    ]
    
class WishInLine(admin.StackedInline):
    model = Wish
    # extra = How many fields are available at once
    extra = 3
    

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'species', 'bio']})
    ]
    inlines = [WishInLine]
    
admin.site.register(User, UserAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Toy)
admin.site.register(Wish)
admin.site.register(Donation)