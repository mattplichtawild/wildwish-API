from django.db import models
from multiselectfield import MultiSelectField
# Set Google API key before using AddressField
# from address.models import AddressField

from .constants import ACCR_CHOICES, ST_CHOICES
# from animals import models
# from django.db.models.deletion import SET_NULL

class Zoo(models.Model):
    # superuser running into issues with circular imports
    # Has superuser to manage all animals and wishes in collection?
    # superuser = models.ForeignKey('animals.User', null=True, on_delete=SET_NULL)
    name = models.CharField(max_length=72)
    website = models.URLField(max_length=200, null=True)
    accrs = MultiSelectField(choices=ACCR_CHOICES, null=True, blank=True)
    accrs.verbose_name = 'Accreditations'
    
    # Beginner location data, migrate to AddressField in future iteration
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
