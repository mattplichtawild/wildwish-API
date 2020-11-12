from zoos.models import Zoo
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.utils import timezone
import datetime

class User(models.Model):
    first_name = models.CharField(max_length=24, default='test')
    last_name = models.CharField(max_length=24, default='test')
    email = models.EmailField(max_length=32, default='test')
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
        return f'{self.first_name} {self.last_name}'

# If an animals user is deleted, assign the zoo's superuser to the new user if it exists
# Method needs to be rewritten. 'Zoo' doesn't have a 'superuser' attr
def set_user_from_zoo(animal):
    if animal.zoo.superuser:
        return animal.zoo.superuser
    return None

class Animal(models.Model):
    # Is this fk needed since a fk already exists with 'user' which has a zoo fk?
    # (default=self.user.zoo_id)?
    # zoo = models.ForeignKey(Zoo, null=True, on_delete=PROTECT)
    # for user: on_delete=models.SET(set_user_from_zoo)
    user = models.ForeignKey(User, on_delete=PROTECT, null=True)
    name = models.CharField(max_length=24, default='test')
    species = models.CharField(max_length=72, default='test')
    bio = models.CharField(max_length=180, default='test')
    
    # Returns <Animal: 'name'> instead of <Animal: Animal object (n)> when calling object
    def __str__(self):
        return self.name
    
    # Example method from docs
    def was_created_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Toy(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField
    
    def __str__(self):
        return self.name
    
class Wish(models.Model):
    # If the animal is deleted, wishes also get deleted
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    
    # Don't allow deletion of the toy if being referenced by wishes
    toy = models.ForeignKey(Toy, on_delete=PROTECT)
    
    def __str__(self):
        return (f'Wish ID #{self.id}: {self.toy.name} for {self.animal.name}')
    
    class Meta:
        verbose_name_plural = 'Wishes'
    
class Donation(models.Model):
    # Preserve record of donation even if user deletes their account
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    donor_name = models.CharField(max_length=72)
    # Preserve record of donation even if animal or wish is deleted
    wish = models.ForeignKey(Wish, null=True, on_delete=SET_NULL)
    
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Set donor name attribute
    def __init__(self):
        if self.user:
            self.donor_name = (f'{self.user.first_name} {self.user.last_name}')
    
    # def __str__(self):
    #     return (f'{self.amount} to {self.wish.animal.name}')