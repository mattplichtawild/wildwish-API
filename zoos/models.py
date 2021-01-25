from django.db import models
from multiselectfield import MultiSelectField
# Set Google API key before using AddressField
# from address.models import AddressField

from .constants import ACCR_CHOICES, ST_CHOICES
# from animals import models
# from django.db.models.deletion import SET_NULL

class Zoo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=72)
    website = models.URLField(max_length=200, null=True)
    accrs = MultiSelectField(choices=ACCR_CHOICES, null=True, blank=True)
    accrs.verbose_name = 'Accreditations'
    
    # Beginner location data, migrate to AddressField in future iteration
    street = models.CharField(max_length=140, null=True, blank=True)
    street.help_text = 'Shipping address. Do not use main zoo address.'
    city = models.CharField(max_length=48)
    st = models.CharField(
        max_length=2,
        choices=ST_CHOICES
        )
    zip = models.CharField(max_length=5)
    st.verbose_name = 'State'
    zip.verbose_name = 'Zip Code'
    
    def __str__(self):
        return self.name

    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
