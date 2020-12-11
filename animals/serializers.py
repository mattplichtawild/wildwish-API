from django.db import models
from rest_framework import serializers
from .models import Animal
from images.models import Image

# For related images field
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['upload']
        
        
# Works similar to ModelForm
class AnimalSerializer(serializers.ModelSerializer):
    
    # StringRelatedField returns the __str__ method of the related model
    zoo = serializers.StringRelatedField()
    
    images = ImageSerializer(many=True, read_only=True)
    recent_img = ImageSerializer(many=False, read_only=True)
    
    
    # Use slug related field to get attribute from Image model
    # images = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='url'
    #  )
    
    class Meta:
        model = Animal
        # 'images' field just needs to return the url of the image
        fields = ('id', 'zoo', 'name', 'species', 'bio', 'images', 'recent_img')