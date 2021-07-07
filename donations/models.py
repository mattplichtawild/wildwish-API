from django.db import models
from animals.models import User, Wish
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL

class Donation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
            return (f'${self.amount} to {self.wish.animal.name}')
        else:
            return (f'${self.amount} to nobody in particular')
        
    class Meta:
        db_table = 'donations'
