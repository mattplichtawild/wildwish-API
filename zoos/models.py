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
    accrs = MultiSelectField(choices=ACCR_CHOICES, null=True)
    accrs.verbose_name = 'Accreditations'
    
    # Beginner location data, migrate to AddressField in future iteration
    city = models.CharField(max_length=48)
    st = models.CharField(
        max_length=2,
        choices=ST_CHOICES
        )
    st.verbose_name = 'State'

    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
