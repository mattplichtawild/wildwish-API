from django.db import models
from django.db.models.deletion import PROTECT
from zoos.models import Zoo
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            pass
        # Copy/pasted value error has error with _typeshed
            # raise ValueError(_typeshed('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        ## These copy/pasted value errors have errors with underscore. TODO: Fix it
        if extra_fields.get('is_staff') is not True:
            pass
            # raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            pass
            # raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=72, unique=True)
    keeper = models.BooleanField(default=False)
    zoo = models.ForeignKey(Zoo, blank=True, null=True, on_delete=PROTECT)
    verified = models.BooleanField(default=False)
    
    # Fields below needed to correctly use AbstractUser
    username = None 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def name(self):
        return f'{self.first_name} {self.last_name}'

    # what authorization checks to complete?
    def auth_keeper(self):
        return self.keeper & self.verified
    
    auth_keeper.boolean = True
    auth_keeper.short_description = 'Verified Zookeeper'
    
    def __str__(self):
        return self.name()
    
    class Meta:
        db_table = 'users'
