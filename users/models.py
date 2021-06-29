from django.db import models
from django.db.models.deletion import PROTECT
from zoos.models import Zoo

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=72)
    keeper = models.BooleanField(default=False)
    zoo = models.ForeignKey(Zoo, null=True, on_delete=PROTECT)
    verified = models.BooleanField(default=False)
    
    def name(self):
        return f'{self.first_name} {self.last_name}'

    # what authorization checks to complete?
    def auth_keeper(self):
        return self.keeper & self.verified
    
    auth_keeper.boolean = True
    auth_keeper.short_description = 'Verified Zookeeper'
    
    def __str__(self):
        return self.name()
    
    class Meta:
        db_table = 'users'
