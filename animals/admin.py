from django.contrib import admin

from .models import User, Animal

admin.site.register(User)
admin.site.register(Animal)