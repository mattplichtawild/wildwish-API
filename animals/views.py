

from images.models import Image
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from animals.models import Animal, Species, Wish, User, Toy
from zoos.models import Zoo
from users.models import User
from donations.models import Donation
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from mailer import mailer

from .serializers import AnimalSerializer, WishSerializer, ImageSerializer
from rest_framework import generics, viewsets, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework import parsers
import pprint
import pgeocode
import json

class AnimalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    
class WishViewSet(viewsets.ModelViewSet):
    pass

    ## When resources images are updated, email those images to all the donors
    ## Create new Post from images 
    def update(self, request, *args, **kwargs):
        ## Check if the patch request includes images
        ## If it does, use the mailer module to send those images to the donors in 'donation_set'
        ## Then, use those images to create a new Post
        super().update(self, request, *args, **kwargs)
    
# Returns distance between two coordinates in km
import math 
def haversine(lat1, lon1, lat2, lon2): 
    # ensure args are not strings
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    # distance between latitudes 
    # and longitudes 
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
  
    # convert to radians 
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
  
    # apply formulae 
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2)); 
    rad = 6371
    c = 2 * math.asin(math.sqrt(a)) 
    return rad * c 

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # Probably don't have this in production? This is my own IP
    # This makes it so I can still get a location during development
    if ip == '127.0.0.1':
        ip = '73.153.40.163'
    return ip

def get_client_info(request):
    import ipinfo
    # Put this in .env or something so it's not public
    access_token = 'c919021826b373'
    handler = ipinfo.getHandler(access_token)
    ip_address = get_client_ip(request)
    details = handler.getDetails(ip_address)
    
    # lat, lon = details.loc.split(',')
    return details

# {
# "zoo": {
#     "name":"",
#     "website":""
#     },
#  "user": {
#      "first_name":"Paul",
#      "last_name":"Blart",
#      "email":"mallcop@example.com"
#      },
#  "animals":[
#      {
#          "name":"Test",
#          "species":"Lion",
#          "dob":"",
#          "bio":"Test",
#          "images":[{ uuid: 'string' }, { uuid: 'string' }],
#          "toys":[
#              {"url":"https://www.wildlifetoybox.com/p-balls.html"}
#             ]
#     },
#     ]
#  }

# To create objects from static page hosted on Netlify
@csrf_exempt
@api_view(['POST'])
@parser_classes([parsers.JSONParser])
def create_from_landing(request, format=None):
    data = request.data
    
    ## Serializers created with django-rest-framework need csrf and CORS protection
    ## This is quick and dirty till I build authentication
    zooInfo = data['zoo']
    z, created = Zoo.objects.get_or_create(name=zooInfo['name'])
    if created:
        z.website = zooInfo['website']
        # Address lines are needed functions but I don't want to include these fields on the main form
        z.city = 'UPDATE ADDRESS FIELDS'
        z.st = 'CO'
        z.zip = '80205'
        z.country = 'US'
    z.save()
    
    userInfo = data['user']
    u, created = User.objects.get_or_create(
        email=userInfo['email'],
        first_name=userInfo['first_name'],
        last_name=userInfo['last_name']
        )
    u.zoo = z
    u.save()
    
    animals = data['animals']
    for e in animals:
        if e['dob'] == '':
            dob = None
        else:
            dob = e['dob']

        a = Animal(
            zoo=z,
            user=u,
            name=e['name'],
            date_of_birth=dob,
            bio=e['bio'],
        )
        species, created = Species.objects.get_or_create(common_name=e['species'])
        species.save()
        a.species = species
        a.save()
        
        # Create animal-image relationships by looking up the uuid of the image (auto uploaded by same form)
        for i in e['images']:
            # Using get_or_create here allows finding the image to fail gracefully
            # If it was created, then it's obviously not what we're looking for
            img, created = Image.objects.get_or_create(uuid=i['uuid'])
            if not created:
                a.images.add(img)
        
        for t in e['toys']:
            # Create new toy with user submitted URL
            # Set default price as 10 until it is manually set by admins
            if t['url'] != '':
                try:
                    toy = Toy.objects.get(url=t['url'])
                # get_or_create wasn't working correctly since 'name' is required
                except Toy.DoesNotExist:
                    toy = Toy(
                        url=t['url'],
                        name='Default Toy Name',
                        price=10,
                        brand=''
                    )
                    toy.save()
                
                wish = Wish(toy=toy, animal=a, fund_amount=toy.price)
                wish.save()
            
        # Set the first wish as active
        w = a.wish_set.first()
        w.active = True
        w.save()
        a.save()
    
    return JsonResponse( data, safe=False)

# For CRUD actions using rest_framework
class AnimalListCreate(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class WishListFeatured(generics.ListAPIView):
    queryset = Wish.objects.all().filter(active=True)
    serializer_class = WishSerializer
        
class WishListNearby(generics.ListAPIView):
    queryset = Wish.objects.all().filter(active=True)
    serializer_class = WishSerializer
    
    def find_by_dist(self):
        # Dist between locations in km.
        MAX_DIST = 250
        
        # client_details is object like:
        '''
        {
            "ip": "8.8.8.8",
            "city": "Mountain View",
            "region": "California",
            "country": "US",
            "loc": "37.3860,-122.0838",
            "postal": "94035",
            "timezone": "America/Los_Angeles"
        }
        '''
        
        client_details = get_client_info(self.request)
        pprint.pprint(client_details.all)
        dist = pgeocode.GeoDistance(client_details.country)
        nearby_list = []
        
        # pgeocode requires that both zips be in same country
        queryset = self.queryset.filter(animal__zoo__country=client_details.country)
        
        # Add object to nearby_list if it is within max distance
        for w in queryset:
            if dist.query_postal_code(w.animal.zoo.zip, client_details.postal) < MAX_DIST:
                nearby_list.append(w)
        
        return nearby_list
    
    def get_queryset(self):
        return self.find_by_dist()
        
class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    # Below methods covered by RetrieveUpdateDestroyAPIView
    # def get_object(self, pk):
    #     try:
    #         return Animal.objects.get(pk=pk)
    #     except Animal.DoesNotExist:
    #         raise Http404
    
    # def get(self, request, pk, format=None):
    #     animal = self.get_object(pk)
    #     serializer = AnimalSerializer(animal)
    #     return Response(serializer.data)
    
    # def put(self, request, pk, format=None):
    #     animal = self.get_object(pk)
    #     serializer = AnimalSerializer(animal, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
      
    
class WishListCreate(APIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    
class WishDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Wish.objects.get(pk=pk)
        except Wish.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        wish = self.get_object(pk)
        serializer = WishSerializer(wish)
        return Response(serializer.data)

# '/animals/:id
# Create donation with parameters from POST request and add them to the animal's active wish
# Why did I build it using this url and not '/wishes/:id'?
# THIS FUNCTION NOT USED, REFACTORED INTO 'donations.views' AS 'create_donation'
def donate(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    print('before if statement')
    if request.POST:
        print('Hit if statement')
        wish = get_object_or_404(Wish, pk=request.POST['wish_id'])
        try:
            d = Donation(
                    wish_id=request.POST['wish_id'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    amount=request.POST['amount']
                )
            mailer.send_recpt(d)
            d.save()
            if wish.current_funding() >= wish.fund_amount:
                wish.complete_funding()
            # wish.save()
            print (f'{d.user} donated {d.amount} to {d.wish}')
        except (KeyError, Wish.DoesNotExist):
            return render(request, 'animals/detail.html', {'animal': animal, 'error_message': 'Please select a wish'})
        else:
            # reverse() is a utility function provided by Django
            return HttpResponseRedirect(reverse('animals:detail', args=(animal.id,)))
        
    else:
        return HttpResponseRedirect(reverse('animals:detail', args=(animal.id,)))
    
# /animals/:animal_id/wish
# Maybe refactor into separate wish app and use '/wishes/:wish_id
# Method for keepers to update active wish with pictures, not creating new wish 
def update_wish(request, animal_id):
    from images.forms import ImageForm
    # Get active wish from animal's set
    # GET returns form to upload images (no other attribute changes)
    # POST adds images and triggers mailer to send email with images to donor
    
    animal = Animal.objects.get(pk=animal_id)
    wish = animal.get_active_wish()
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
             # img_obj = Image.objects.create(upload=request.POST['upload'])
            img_obj = form.instance
            wish.images.add(img_obj)
            
            # Get list of address and send email to each one
            d_set = wish.donation_set.all()
            for d in d_set:
                mailer.send_wish_imgs(d)
                
            # Get the current instance object to display in the template
            return render(request, 'animals/wish_form.html', {'form': form, 'img_obj': img_obj})
    else:
        return render(request, 'animals/wish_form.html', {'wish': wish, 'form': form})
    
    
    
# Deprecated views, no longer used (keep for reference)
#
# Responds to GET request at '/' using django template
# 'as_view()' method will return the defined query set as context object
# class ActiveWishList(ListView):
#     # Below is same as 'queryset = Wish.objects.all()'
#     # model = Wish
    
#     queryset = Wish.objects.filter(active=True)
#     context_object_name = 'active_wish_list'

def ActiveWishList(request):
    queryset = Wish.objects.filter(active=True)
    return JsonResponse(queryset, safe=False)
    
class IndexView(ListView):
    model = Animal
    template_name = 'animals/index.html'
    context_object_name = 'animals_index'
    
    def get_queryset(self):
        return Animal.objects.all
    
# Index using functional view instead of class based    
def index(request):
    # Use pagination/React components once page gets big enough
    animals_list = Animal.objects.all()
    
    return render(request, 'animals/index.html', {'animals_list': animals_list})

def detail(request, animal_id):
    # animal = Animal.objects.get(pk=animal_id)
    # # return JsonResponse({animal})
    # return HttpResponse(animal)

    # get_object_or_404 does what it says
    animal = get_object_or_404(Animal, pk=animal_id)
    
    # Below method is same as 'get_object_or_404' method above
    # try:
    #     animal = Animal.objects.get(pk=animal_id)
    # except Animal.DoesNotExist:
    #     raise Http404("Animal does not exist")
    # return render(request, 'animals/detail.html', {'animal': animal})

# class AnimalView(DetailView):
#     template_name = '/animals/detail.html'
#     model = Animal
#     context_object_name = 'animal'

#     def get_context_data(self, **kwargs):
#         context = {
#             'component': 'overview.js',
#             'title': 'Hello World',
#             'props': 
#                 {'animal': animal}
#         }

#         return context
    
#     # render method uses template in '/animals/templates' to return HTML template
#     return render(request, 'animals/detail.html', {'animal': animal})