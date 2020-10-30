from django.db import models
from multiselectfield import MultiSelectField
# Set Google API key before using AddressField
# from address.models import AddressField

from .constants import ACCR_CHOICES, ST_CHOICES

class Zoo(models.Model):
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
