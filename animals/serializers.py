from users.serializers import UserSerializer
from zoos.models import Zoo
from django.db import models
from rest_framework import serializers
from .models import Animal, Species, Toy, Wish
from images.models import Image

# For related images field
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title','upload']
        
class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id', 'name', 'description', 'price')

class WishSerializer(serializers.ModelSerializer):
    # animal_id = serializers.PrimaryKeyRelatedField(read_only=True)
    images = ImageSerializer(many=True)
    toy = ToySerializer(read_only=True)
    
    class Meta:
        model = Wish
        fields = ['id', 'toy', 'images', 'active', 'current_funding']
        depth = 2
        
class ZooSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Zoo
        fields = ('id', 'name', 'city', 'st', 'zip')
        
class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('common_name', 'genus', 'species', 'sub_species')
        
class AnimalSerializer(serializers.ModelSerializer):
    
    # StringRelatedField returns the __str__ method of the related model
    zoo = ZooSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    # species = SpeciesSerializer()
    wish_set = WishSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    avatar = ImageSerializer(many=False, read_only=True)
    
    class Meta:
        model = Animal
        # 'images' field just needs to return the url of the image
        fields = ('id', 'name', 'species', 'date_of_birth', 'user', 'zoo', 'bio', 'images', 'wish_set', 'avatar')

# class WishSerializer(serializers.ModelSerializer):
    
#     animal = AnimalSerializer(read_only=True)
#     toy = serializers.StringRelatedField()
    
#     class Meta:
#         model = Wish
#         fields = ['id', 'toy', 'animal']