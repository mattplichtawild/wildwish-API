from django.db.models.deletion import CASCADE
from animals.models import Animal, Toy, Wish
from django.db import models

# Image is abstract class (no db table)
# Subclasses inherit from this model and each have their own db table
class Image(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField()
    
    class Meta:
        abstract = True

# Each model can have many Images and Image can have either Toy, Wish, or Animal (or all three)
# Image won't have more than one of each model related to it
class AnimalImage(Image):
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    
    class Meta:
        db_table = 'animal_images'
        
class ToyImage(Image):
    toy = models.ForeignKey(Toy, on_delete=CASCADE)

    class Meta:
        db_table = 'toy_images'
        
class WishImage(Image):
    wish = models.ForeignKey(Wish, on_delete=CASCADE)
    
    class Meta:
        db_table = 'wish_images'