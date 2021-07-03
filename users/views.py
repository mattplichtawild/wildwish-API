from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import authentication, permissions

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
