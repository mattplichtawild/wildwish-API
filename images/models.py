from django.db import models

class Image(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField()
