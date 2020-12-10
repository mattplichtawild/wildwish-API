from rest_framework import serializers
from .models import Animal

# Works similar to ModelForm
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        # 'images' field just needs to return the url of the image
        fields = ('id', 'zoo', 'name', 'species', 'bio', 'images')