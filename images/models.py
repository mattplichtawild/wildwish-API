from django.db import models
import uuid

# Image is abstract class (no db table)
# Subclasses inherit from this model and each have their own db table
class Image(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField()
    title = models.CharField(max_length=90, default='Untitled')
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.upload.name
    
    # class Meta:
    #     abstract = True

# Each model can have many Images and Image can have either Toy, Wish, or Animal (or all three)
# Image won't have more than one of each model related to it
# class AnimalImage(models.Model):
#     image = models.ForeignKey(Image, on_delete=CASCADE)
#     animal = models.ForeignKey(Animal, on_delete=CASCADE)
    
#     class Meta:
#         db_table = 'animal_images'
        
# class ToyImage(models.Model):
#     # image = models.ForeignKey(Image, on_delete=CASCADE)
#     toy = models.ForeignKey(Toy, on_delete=CASCADE)

#     class Meta:
#         db_table = 'toy_images'
        
# class WishImage(models.Model):
#     # image = models.ForeignKey(Image, on_delete=CASCADE)
#     wish = models.ForeignKey(Wish, on_delete=CASCADE)
    
#     class Meta:
#         db_table = 'wish_images'