from django.test import ( TestCase, Client )
from rest_framework.test import APIClient
from users.models import User
from django.urls import reverse

# Create your tests here.

class UserTestCase(TestCase):
    
    client = APIClient()
    
    def create_user(self, **kwargs):
        return User.objects.create(**kwargs)
    
    def test_user_create(self):
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
        
    ## User can login by obtaining token
    def test_user_login(self):
        data = {
            'first_name': 'Paul',
            'last_name': 'Blart',
            'email': 'mallcop@gmail.com',
            'password': 'password'
        }
        
        ## Register the user first
        self.client.post(reverse('users:create_user'), data)
        ## Then test that the user can login
        resp = self.client.post(reverse('token_obtain_pair'), { "email": "mallcop@gmail.com", "password": "password"})
        self.assertTrue('access' in resp.json())
        self.assertTrue('refresh' in resp.json())
        
        

    ## User can use those tokens to view account (other resources tested within respective apps)
    def test_token_access(self):
        client = APIClient()
        ## Create a user
        user = self.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com')
        user.set_password('password')
        user.save()
    
        ## Get the access token and set it in the request header
        resp = client.post(reverse('token_obtain_pair'), { "email": "mallcop@gmail.com", "password": "password"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        resp = client.get(f'/users/{user.id}/')
        self.assertEqual(resp.status_code, 200)
     
    ## User cannot view other accounts 
    def test_forbidden_user(self):
        '''User cannot view other accounts'''
        client = APIClient()
        ## Create users
        user1 = User.objects.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com', password='password')
        
        user2 = User.objects.create_user(first_name='Matt', last_name='Plichta', email='testemail@gmail.com', password='betterpassword')
    
        ## Get the access token and set it in the request header
        resp = client.post(reverse('token_obtain_pair'), { "email": user1.email, "password": "password"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        resp = client.get(f'/users/{user2.id}/')
        self.assertEqual(resp.status_code, 403)
        
    ## Admins can view all user accounts
    def test_admin_account_view(self):
        '''Admins can view all user accounts'''
        client = APIClient()
        
        user = User.objects.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com', password='password')
            
        admin = User.objects.create_superuser(first_name='Matt', last_name='Plichta', email='testemail@gmail.com', password='betterpassword')
        
        resp = client.post(reverse('token_obtain_pair'), { "email": admin.email, "password": "betterpassword"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        resp = client.get(f'/users/{user.id}/')
        self.assertEqual(resp.status_code, 200)
        
    ## User can edit their account, cannot edit others
    def test_edit_account(self):
        '''User can edit their account, cannot edit others'''
        client = APIClient()
        
        user1 = User.objects.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com', password='password')
        user2 = User.objects.create_user(first_name='Matt', last_name='Plichta', email='testemail@gmail.com', password='betterpassword')
        newFirstName = "Kevin"
        newLastName = "James"

        resp = client.post(reverse('token_obtain_pair'), { "email": user1.email, "password": "password"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        
        ## Patch request to forbidden account
        resp = client.patch(f'/users/{user2.id}/', { "first_name": newFirstName, "last_name": newLastName })
        self.assertEqual(resp.status_code, 403)

        ## Patch request to correct account
        resp = client.patch(f'/users/{user1.id}/', { "first_name": newFirstName, "last_name": newLastName })
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['first_name'], newFirstName)
        self.assertEqual(resp.json()['last_name'], newLastName)
        

    ## User can delete their account, cannot delete others
    def test_delete_account(self):
        '''User can delete their account, cannot delete others'''
        client = APIClient()
        
        user1 = User.objects.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com', password='password')
        user2 = User.objects.create_user(first_name='Matt', last_name='Plichta', email='testemail@gmail.com', password='betterpassword')
        
        resp = client.post(reverse('token_obtain_pair'), { "email": user1.email, "password": "password"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
       
        preUserCount = User.objects.all().count()
        
        ## Delete request to forbidden account
        resp = client.delete(f'/users/{user2.id}/')
        self.assertEqual(resp.status_code, 403)
        self.assertEqual(User.objects.all().count(), preUserCount)
        
        ## Delete request to correct account
        resp = client.delete(f'/users/{user1.id}/')
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(User.objects.all().count(), (preUserCount - 1) )
        
    ## Only admins can view index of all users
    def test_index_view(self):
        '''Only admins can view index of all users'''
        client = APIClient()
        
        user = User.objects.create_user(first_name='Paul', last_name='Blart', email='mallcop@gmail.com', password='password')
        admin = User.objects.create_superuser(first_name='Matt', last_name='Plichta', email='testemail@gmail.com', password='betterpassword')
        
        # Login admin user and try index
        resp = client.post(reverse('token_obtain_pair'), { "email": admin.email, "password": "betterpassword"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        
        resp = client.get('/users/')
        self.assertEqual(resp.status_code, 200)
        
        # Login regular user and try index
        resp = client.post(reverse('token_obtain_pair'), { "email": user.email, "password": "password"})
        token = resp.json()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token['access'])
        
        resp = client.get('/users/')
        self.assertEqual(resp.status_code, 403)