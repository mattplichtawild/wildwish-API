from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from animals.models import Wish
from django.http import HttpResponseRedirect
from .models import Donation
from django.urls import reverse
from mailer import mailer

def create_donation(request):
    # animal = get_object_or_404(Animal, pk=animal_id)
    
    print(request.POST)
    
     
    print('before if statement')
    if request.POST:
        print('Hit if statement')
        wish = get_object_or_404(Wish, pk=request.POST.get('wish_id'))
        animal = wish.animal
        
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
        
        return JsonResponse(d, safe=False)
        
    #     try:
    #     # create donation with error handling
    #     except (KeyError, Wish.DoesNotExist):
    #         return render(request, 'animals/detail.html', {'animal': animal, 'error_message': 'Please select a wish'})
    #     else:
    #         # reverse() is a utility function provided by Django
    #         return HttpResponseRedirect(reverse('animals:detail', args=(animal.id,)))
        
    else:
        return HttpResponseRedirect('/')
