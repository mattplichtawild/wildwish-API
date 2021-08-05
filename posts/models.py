from images.models import Image
from django.db import models

class Post(models.Model):
    ## upload_id created by Instagram when posted
    upload_id = models.CharField(max_length=900, null=True, blank=True)
    caption = models.CharField(max_length=2200, default='')
    photos = models.ManyToManyField(Image)
    ## user_tags will be used as parameter when creating post with instabot
    ## hash_tags contains list of hash tags that are created and concatenated to caption
    user_tags = models.CharField(max_length=2200, default='')
    hash_tags = models.JSONField(null=True, blank=True)
    
    ## Get user tags from each donor of the wish, zookeeper users of that animal and the zoo that the animal resides in
    def get_user_tags():
        pass
    
    ## Set by using species groups derived from the animal in the images
    def get_hash_tags():
        pass
    
    ## Tag by going through list in hash_tags and concatenating each one to caption
    def concat_hash_tags():
        pass
    
    def post_to_insta(self):
        pass
        
