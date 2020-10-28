from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.utils import timezone
import datetime

class User(models.Model):
    first_name = models.CharField(max_length=24, default='test')
    last_name = models.CharField(max_length=24, default='test')
    email = models.EmailField(max_length=32, default='test')
    keeper = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
class Donation(models.Model):
    # Preserve record of donation even if user deletes their account
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    
    # Preserve record donation even if animal or wish is deleted
    wish = models.ForeignKey(Wish, null=True, on_delete=SET_NULL)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return (f'{self.amount} to {self.wish.animal.name}')