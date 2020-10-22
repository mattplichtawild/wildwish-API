from django.contrib import admin

from .models import Donation, Toy, User, Animal, Wish

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Toy)
admin.site.register(Wish)
admin.site.register(Donation)