from rest_framework import serializers
from .models import Animal

# Works similar to ModelForm
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'zoo', 'name', 'species', 'bio', 'images')