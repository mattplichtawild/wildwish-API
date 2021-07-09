from orders.models import Order
from images.models import Image
from zoos.models import Zoo
from users.models import User
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.utils import timezone
import datetime

        
class SpeciesGroup(models.Model):
    group_name = models.CharField(max_length=72)
    
    def __str__(self):
        return self.group_name
    
    class Meta:
        verbose_name = 'Species Group'
    
class Species(models.Model):
    common_name = models.CharField(max_length=72)
    genus = models.CharField(max_length=72, null=True, blank=True)
    species = models.CharField(max_length=72, null=True, blank=True)
    sub_species = models.CharField(max_length=72, null=True, blank=True)
    species_group = models.ManyToManyField(SpeciesGroup, blank=True)
    common_name.verbose_name = 'Common Name'
    sub_species.verbose_name = 'Subspecies'
    species_group.verbose_name = 'Species Groups'
    
    def __str__(self):
        return self.common_name
    
    class Meta:
        verbose_name_plural = 'Species'

class Animal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # (default=self.user.zoo_id)?
    zoo = models.ForeignKey(Zoo, on_delete=PROTECT)
    # for user: on_delete=models.SET(set_user_from_zoo)
    user = models.ForeignKey(User, on_delete=PROTECT, null=True, blank=True)
    name = models.CharField(max_length=24)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=PROTECT, null=True)
    bio = models.TextField(null=True, blank=True)
    images = models.ManyToManyField(Image)
    avatar = models.ForeignKey(Image, on_delete=PROTECT, null=True, related_name='avatar_img')
    
    date_of_birth.help_text = 'YYYY-MM-DD'

    # This is being handled on the frontend
    # def get_recent_img(self):
    #     if self.images.count() > 0:
    #         return self.images.last()
        
    # def set_default_avatar(self):
    #     self.avatar = self.get_recent_img()
    
    def get_active_wish(self):
        return self.wish_set.filter(active=True).first()
    
    # Returns <Animal: 'name'> instead of <Animal: Animal object (n)> when calling object
    def __str__(self):
        return f'{self.name} - {self.species}'
    
    class Meta:
        db_table = 'animals'
            
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class Vendor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=72)
    website = models.CharField(max_length=72)
    
    def __str__(self):
        return self.name
    
class Toy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=32)
    description = models.TextField(null=True)
    images = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ship_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=180, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, null=True, blank=True)
    url = models.URLField(max_length=1200, null=True)
    
    suggested_species = models.ManyToManyField(SpeciesGroup, blank=True)
    suggested_species.verbose_name = 'Suggested Species'
    ship_cost.help_text = 'Leave blank if unknown.'
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'toys'
    
class Wish(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # If the animal is deleted, wishes also get deleted
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    images = models.ManyToManyField(Image, blank=True)
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
    
    def save(self, *args, **kwargs):
        # Set fund amount before saving
        # This value will use toy.price, plus shipping costs and other criteria
        if self.fund_amount is None:
            self.fund_amount = self.toy.price
        super(Wish, self).save()
            
        super().clean(*args, **kwargs)
        
    def complete_funding(self):
        self.active = False
        order = Order(wish=self)
        order.save()
        self.save()
            
    def __str__(self):
        return (f'ID #{self.id} | {self.toy.name} for {self.animal.name} at {self.animal.zoo.name}')
    
    class Meta:
        verbose_name_plural = 'Wishes'
        db_table = 'wishes'
    