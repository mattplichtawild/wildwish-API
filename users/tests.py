from django.test import TestCase
from users.models import User

# Create your tests here.

class UserTestCase(TestCase):
    
    def create_user(self, **kwargs):
        return User.objects.create(**kwargs)
    
## User can create an account
    def test_user_create(self):
        '''User can create account'''
        user = self.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com')
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.name())
        
    
        
## User can login (obtain tokens)

## User can use those tokens to view resources

## User can create and edit their own resources

## User cannot view resources that don't belong to them

## User cannot edit or delete resources that don't belong to them

## Admins can view all resources
