from images.models import Image
from django.contrib import admin

from .models import Donation, Species, Toy, User, Animal, Wish, Vendor


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
    # fieldsets = [
    #     (None, {'fields': ['fund_amount']}),
    #     # ('Current funding', {'fileds': ['']})
    # ]
    # exclude = ('fund_amount',)
    
class WishInLine(admin.StackedInline):
    model = Wish
    # 'fields' and 'exclude' are doing the same thing
    # fields = ('toy', 'animal')
    exclude = ('images','fund_amount')
    # extra = How many fields are available at once
    extra = 1
    
class AnimalImageInLine(admin.TabularInline):
    model = Animal.images.through
    # extra = How many fields are available at once
    extra = 1
    
    verbose_name = 'Image'
    verbose_name_plural = 'Images'
    
class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['zoo', 'name', 'species', 'bio']}),
        # ('Profile Pic', {'fields': ['recent_img']})
    ]
    inlines = [WishInLine, AnimalImageInLine]
    search_fields = ['zoo', 'name', 'species']
    
class ToyImageInline(admin.TabularInline):
    model = Toy.images.through
    extra = 1
    verbose_name = 'Image'
    verbose_name_plural = "Images"
    
class ToyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'price', 'description', 'url']})
    ]
    inlines = [ToyImageInline]
    
    
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species)
admin.site.register(Toy, ToyAdmin)
admin.site.register(Vendor)
# admin.site.register(User, UserAdmin)
# admin.site.register(Wish, WishAdmin)
# admin.site.register(Donation)