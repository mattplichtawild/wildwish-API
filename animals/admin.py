from django.contrib import admin

from .models import Toy, User, Animal, Wish

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Toy)
admin.site.register(Wish)