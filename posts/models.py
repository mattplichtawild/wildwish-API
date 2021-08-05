from images.models import Image
from django.db import models

class Post(models.Model):
    ## upload_id created by Instagram when posted
    upload_id = models.CharField(max_length=900, null=True, blank=True)
    caption = models.CharField(max_length=2200, default='')
    photos = models.ManyToManyField(Image)
    user_tags = models.CharField(max_length=2200, default='')
    hash_tags = models.CharField(max_length=2200, default='')
    
