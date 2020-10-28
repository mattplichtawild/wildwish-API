from django.contrib import admin

from .models import Donation, Toy, User, Animal, Wish


# User custom class to override fields for User
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'keeper']

admin.site.register(User, UserAdmin)
admin.site.register(Animal)
admin.site.register(Toy)
admin.site.register(Wish)
admin.site.register(Donation)