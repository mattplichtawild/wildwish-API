from django.shortcuts import render
from rest_framework import generics, viewsets, authentication, permissions

class WishViewSet(viewsets.ModelViewSet):
    pass

    ## When resources images are updated, email those images to all the donors
    ## Create new Post from images 
    def update(self, request, *args, **kwargs):
        ## Check if the patch request includes images
        ## If it does, use the mailer module to send those images to the donors in 'donation_set'
        ## Then, use those images to create a new Post
        super().update(self, request, *args, **kwargs)
