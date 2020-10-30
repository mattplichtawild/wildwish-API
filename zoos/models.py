from django.db import models

class Zoo(models.Model):
    name = models.CharField(max_length=72, default='test')
    
    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
