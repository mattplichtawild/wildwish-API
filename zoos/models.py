from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
from multiselectfield import MultiSelectField
# Set Google API key before using AddressField
# from address.models import AddressField
from django_countries.fields import CountryField

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
    street = models.CharField(max_length=140, default='', blank=True)
    street.help_text = 'Shipping address. Do not use main zoo address.'
    city = models.CharField(max_length=48)
    st = models.CharField(
        max_length=2,
        choices=ST_CHOICES
        )
    zip = models.CharField(max_length=5)
    country = CountryField()
    # location = models.PointField(null=False, blank=False, default=Point(0.0, 0.0), srid=4326, verbose_name='Location')
    # lat = models.FloatField(default=0.0, verbose_name="Latitude")
    # lon = models.FloatField(default=0.0, verbose_name="Longitude")
    st.verbose_name = 'State'
    zip.verbose_name = 'Zip Code'
    
    # def set_coords(self):
    #     if self.lat is None or self.lon is None:
            
        
    def __str__(self):
        return self.name

    # Use 'django_address' dependency for addresses?
    # address1 = AddressField()
    # address2 = AddressField(related_name='+', blank=True, null=True)
