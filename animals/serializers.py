from django.db import models
from rest_framework import serializers
from .models import Animal, Wish
from images.models import Image

# For related images field
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['upload']
        
class WishSerializer(serializers.ModelSerializer):
    # toy_id = serializers.StringRelatedField()
    # animal_id = serializers.StringRelatedField()
    
    class Meta:
        model = Wish
        fields = ['id', 'active']
        
class AnimalSerializer(serializers.ModelSerializer):
    
    # StringRelatedField returns the __str__ method of the related model
    zoo = serializers.StringRelatedField()
    species = serializers.StringRelatedField()
    wish_set = WishSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    avatar = ImageSerializer(many=False, read_only=True)
    
    class Meta:
        model = Animal
        # 'images' field just needs to return the url of the image
        fields = ('id', 'name', 'species', 'zoo', 'bio', 'images', 'wish_set', 'avatar')

# class WishSerializer(serializers.ModelSerializer):
    
#     animal = AnimalSerializer(read_only=True)
#     toy = serializers.StringRelatedField()
    
#     class Meta:
#         model = Wish
#         fields = ['id', 'toy', 'animal']