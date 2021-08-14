from images.models import Image
from django.db import models
from instabot import Bot
from decouple import config

from boto3 import boto3


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
    
    def post_to_insta(self, image):
        ## Creating bot instance and logging in should be done outside of this method, where to instantiate?
        bot = Bot()
        bot.login(username = config('INSTA_USERNAME'), password = config('INSTA_PASSWORD'))
        img_url = self.photos.first().upload.url
        
        ## instabot cannot use s3 bucket as source, will first need to download pic to temp location and use that file path
        ## Or possibly use image parameter, method can be called when user is uploading so the file can be grabbed before being uploaded to s3?
        bot.upload_photo(img_url)
        
    def download_source(self):
        s3_client = boto3.client('s3', 
                                 aws_access_key_id='<Access Key ID>', 
                                 aws_secret_access_key='<Secret Access Key>', 
                                 region_name='ap-south-1'
                                 )

        ## download_file 2nd param: Name to give object that is downloaded
        ## download_file 3rd param: full path of s3 file to download
        s3_client.download_file('BUCKET_NAME', 'TEMP_OBJ', 'FILE_NAME')
        
        print('Downloaded source photo')
