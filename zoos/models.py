from django.db import models
from multiselectfield import MultiSelectField
from address.models import AddressField

# Constants to use for accreditation choices
NONE = ''
AZA = 'AZA'
GFAS = 'GFAS'
EAZA = 'EAZA'

ACCR_CHOICES = (
    (AZA, 'Association of Zoos and Aquariums'),
    (GFAS, 'Global Federation of Animal Sanctuaries'),
    (EAZA, 'European Association of Zoos and Aquariums')
)

class Zoo(models.Model):
    name = models.CharField(max_length=72)
    accrs = MultiSelectField(choices=ACCR_CHOICES, null=True)
    
    # Beginner location data, migrate to AddressField in future iteration
    city = models.CharField(max_length=48)
    st = models.CharField(max_length=2)

    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
