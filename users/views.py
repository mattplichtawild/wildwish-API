from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes
from .models import User
from .serializers import UserSerializer, TokenObtainPairSerializer
from rest_framework import authentication, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework.views import APIView

# Copy/paste example method '/users/create/'
class UserCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.DjangoModelPermissions]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    ## Have POST to '/users/' go to this action
    # @permission_classes([permissions.AllowAny])
    # def create(self, request, format='json'):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             json = serializer.data
    #             return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# For simpleJWT
class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class UserView():
    pass