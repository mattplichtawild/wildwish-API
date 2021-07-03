from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from animals.models import Wish
from django.http import HttpResponseRedirect
from .models import Donation
from django.urls import reverse
from mailer import mailer
import json

from rest_framework import viewsets
from .models import User
from .serializers import DonationSerializer
from rest_framework import authentication, permissions

class DonationViewSet(viewsets.ModelViewSet):
    # Which auth and permission classes to use?
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer




## Functional view written while first going through docs
# Create serializer to handle POST requests to /donations
# DONE # TODO: Use rest-framework and serializers to handle this  
def create_donation(request):
    
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        wish = get_object_or_404(Wish, pk=data.get('wish_id'))
        animal = wish.animal
        
        d = Donation(
                wish_id=data.get('wish_id'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                amount=data.get('amount')
            )
       
        d.save()
        mailer.send_recpt(d)
        if wish.current_funding() >= wish.fund_amount:
            wish.complete_funding()
            
        print (f'{d.first_name} donated ${d.amount} to Wish {d.wish}')
        
        return JsonResponse(data, safe=False)
        
    #     try:
    #     # create donation with error handling
    #     except (KeyError, Wish.DoesNotExist):
    #         return render(request, 'animals/detail.html', {'animal': animal, 'error_message': 'Please select a wish'})
    #     else:
    #         # reverse() is a utility function provided by Django
    #         return HttpResponseRedirect(reverse('animals:detail', args=(animal.id,)))
        
    else:
        return HttpResponseRedirect('/')
