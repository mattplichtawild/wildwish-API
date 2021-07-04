from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'keeper']
    fieldsets = [
        (None, {'fields': ['first_name','last_name', 'email', 'zoo']}),
        ('Authentication Info', {'fields': ['keeper', 'verified']}),
    ]
    autocomplete_fields = ['zoo']
    list_display = ('email', 'last_name', 'first_name', 'auth_keeper', 'zoo')

admin.site.register(User, UserAdmin)