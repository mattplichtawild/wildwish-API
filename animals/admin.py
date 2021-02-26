from images.models import Image
from django.contrib import admin
from .models import Species, SpeciesGroup, Toy, User, Animal, Wish, Vendor

class ZooAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # class Meta:
        # ordering = ['-id']
    
# User custom class to override fields for User
class UserAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'keeper']
    fieldsets = [
        (None, {'fields': ['first_name','last_name', 'email', 'zoo']}),
        ('Authentication Info', {'fields': ['keeper', 'verified']}),
    ]
    autocomplete_fields = ['zoo']
    list_display = ('last_name', 'first_name', 'auth_keeper', 'zoo')
    
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
    autocomplete_fields = ['toy']
    
class AnimalImageInLine(admin.TabularInline):
    model = Animal.images.through
    # extra = How many fields are available at once
    extra = 1
    
    verbose_name = 'Image'
    verbose_name_plural = 'Images'
    
# class SpeciesGroupInline(admin.StackedInline):
#     model = Species.species_group.through
#     extra = 2
#     verbose_name = 'Species Group'
#     verbose_name_plural = 'Species Groups'
    
class SpeciesAdmin(admin.ModelAdmin):
    search_fields = ['common_name', 'species_group__group_name']
    list_display = ['common_name', 'genus', 'species', 'sub_species']
    # inlines = [SpeciesGroupInline]
    
class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['zoo', 'name', 'species', 'bio', 'date_of_birth']}),
        # ('Profile Pic', {'fields': ['recent_img']})
    ]
    list_display = ['name', 'species', 'zoo', 'user']
    inlines = [WishInLine, AnimalImageInLine]
    search_fields = ['name', 'species__common_name', 'zoo__name', 'species__species_group__group_name']
    autocomplete_fields = ['species', 'zoo']
    
class ToyImageInline(admin.TabularInline):
    model = Toy.images.through
    extra = 1
    verbose_name = 'Image'
    verbose_name_plural = "Images"
    
class ToyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'vendor__name', 'suggested_species__group_name']
    list_display = ['name', 'price', 'vendor', 'url']
    fieldsets = [
        (None, {'fields': ['name', 'description', 'brand', 'price', 'ship_cost', 'vendor', 'url', 'suggested_species']})
    ]
    inlines = [ToyImageInline]
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
    

    
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Toy, ToyAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(SpeciesGroup)
admin.site.register(Image)
admin.site.register(User, UserAdmin)
admin.site.register(Wish, WishAdmin)