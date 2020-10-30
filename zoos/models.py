from django.db import models
from multiselectfield import MultiSelectField

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
    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
