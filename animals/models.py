from django.db import models
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