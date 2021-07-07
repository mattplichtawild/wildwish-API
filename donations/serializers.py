from animals.serializers import WishSerializer
from users.serializers import UserSerializer
from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    # user = UserSerializer
    # wish = WishSerializer(read_only=True)
    
    class Meta:
        model = Donation
        fields = ['id', 'user', 'first_name', 'last_name', 'email', 'wish', 'amount']