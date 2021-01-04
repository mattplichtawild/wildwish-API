from images.models import Image
from zoos.models import Zoo
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.utils import timezone
import datetime

class User(models.Model):
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
        
class Species(models.Model):
    common_name = models.CharField(max_length=72)
    genus = models.CharField(max_length=72, null=True)
    species = models.CharField(max_length=72, null=True)
    sub_species = models.CharField(max_length=72, null=True)
    
    common_name.verbose_name = 'Common Name'
    sub_species.verbose_name = 'Subspecies'
    
    def __str__(self):
        return self.common_name
    
    class Meta:
        verbose_name_plural = 'Species'

class Animal(models.Model):

    # (default=self.user.zoo_id)?
    zoo = models.ForeignKey(Zoo, on_delete=PROTECT)
    # for user: on_delete=models.SET(set_user_from_zoo)
    user = models.ForeignKey(User, on_delete=PROTECT, null=True)
    name = models.CharField(max_length=24)
    species = models.ForeignKey(Species, on_delete=PROTECT, null=True)
    bio = models.TextField(null=True)
    images = models.ManyToManyField(Image)
    recent_img = models.ForeignKey(Image, on_delete=PROTECT, null=True, related_name='recent_img')

    def get_recent_img(self):
        if self.images.count() > 0:
            return self.images.last()
    
    def get_active_wish(self):
        return self.wish_set.filter(active=True).first()
    
    # Returns <Animal: 'name'> instead of <Animal: Animal object (n)> when calling object
    def __str__(self):
        return f'{self.name} - {self.species}'
    
    class Meta:
        db_table = 'animals'
            
    def save(self, *args, **kwargs):
        self.recent_img = self.get_recent_img()
        super().save(*args, **kwargs)
    
class Vendor(models.Model):
    name = models.CharField(max_length=72)
    website = models.CharField(max_length=72)
    
    def __str__(self):
        return self.name
    
class Toy(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True)
    images = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, null=True)
    url = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'toys'
    
class Wish(models.Model):
    # If the animal is deleted, wishes also get deleted
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    images = models.ManyToManyField(Image)
    # Don't allow deletion of the toy if being referenced by wishes
    toy = models.ForeignKey(Toy, on_delete=PROTECT)
    # Only active wishes are available to donate to
    active = models.BooleanField(default=False)
    fund_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    
    def current_funding(self):
        agg_fnd = 0
        for d in self.donation_set.all():
            agg_fnd += d.amount
            
        return agg_fnd
    
    # To set fund amount
    def set_fund(self, *args, **kwargs):
        return self.toy.price
    
    def clean(self, *args, **kwargs):
        if self.fund_amount is None:
            self.fund_amount = self.toy.price
            
        super().clean(*args, **kwargs)
        
    def complete_funding(self):
        self.active = False
        self.save()
            
    def __str__(self):
        return (f'ID #{self.id} | {self.toy.name} for {self.animal.name}')
    
    class Meta:
        verbose_name_plural = 'Wishes'
        db_table = 'wishes'
    
class Donation(models.Model):
    # Preserve record of donation even if user deletes their account
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL, blank=True)
    
    # donor first and last name to preserve if User is ever deleted
    # Allows donation to be created without needing to create User
    first_name = models.CharField(max_length=72)
    last_name = models.CharField(max_length=72)
    email = models.EmailField(max_length=72)
    
    # Preserve record of donation even if animal or wish is deleted
    wish = models.ForeignKey(Wish, null=True, on_delete=SET_NULL)
    
    # Need to enforce rule that amount is greater than 0
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    # This method probably shouldn't be used at all
    # Set donor name and email variables for preservation in table
    # def set_donor_info(self):
    #     if self.user:
    #         self.donor_first_name = self.user.first_name
    #         self.donor_last_name = self.user.last_name
    #         self.donor_email = self.user.email
            
    # Extend the save method
    # def save(self, *args, **kwargs):
    #     self.set_donor_info(self)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        if self.wish:
            return (f'{self.amount} to {self.wish.animal.name}')
        else:
            return (f'{self.amount} to nobody in particular')
        
    class Meta:
        db_table = 'donations'
        
