from orders.models import Order
from rest_framework import viewsets
from .serializers import DonationSerializer
from .models import Donation
from mailer import mailer
from rest_framework import authentication, permissions

class DonationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()
     
    def get_queryset(self):
        if 'user_pk' in self.kwargs: 
            return self.queryset.filter(user=self.kwargs['user_pk'])
        else:
            return self.queryset
        
    # Send email receipt when creating donation   
    # TODO: Create method to check if email already exists in User database
    def perform_create(self, serializer):
        donation = serializer.save()
        wish = donation.wish
        mailer.send_recpt(donation)
        
        # If the created donation fulfills the funding amount, create a new order:
        if wish.current_funding() >= wish.fund_amount:
            wish.complete_funding()
            order = Order(wish=wish)
            order.save()
            
## Functional view written while first going through docs
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from animals.models import Wish
from django.http import HttpResponseRedirect
import json

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
