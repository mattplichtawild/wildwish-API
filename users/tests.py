from django.test import ( TestCase, Client )
from users.models import User

# Create your tests here.

class UserTestCase(TestCase):
    
    ## Spin up a test client to test API use
    client = Client()
    
    def create_user(self, **kwargs):
        return User.objects.create(**kwargs)
    
    def test_user_create(self):
        '''User can create account'''
        user = self.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com')
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.name())
        
    ## User can create an account
    def test_create_with_api(self):
        data = {
            'first_name': 'Paul',
            'last_name': 'Blart',
            'email': 'mallcop@gmail.com',
            'password': 'password'
        }
        resp = self.client.post('/users/register/', data)
        self.assertEqual(resp.status_code, 201)
        
    ## Account creation fails without provided email and password
    def test_email_pass_required(self):
        data = {
            'first_name': 'Paul',
            'last_name': 'Blart',
        }
        resp = self.client.post('/users/register/', data)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp.content, {"email": "This field is required.", "password": "This field is required."})
        
        
        
        
## User can login (obtain tokens)

## User can use those tokens to view resources

## User can create and edit their own resources

## User cannot view resources that don't belong to them

## User cannot edit or delete resources that don't belong to them

## Admins can view all resources
