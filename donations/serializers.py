from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Donation
        fields = ['user', 'first_name', 'last_name', 'email', 'wish', 'amount']