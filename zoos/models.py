from django.db import models

class Zoo(models.Model):
    name = models.CharField(max_length=72, default='test')
    