from django.http import request
from django.http.response import JsonResponse
from animals.models import Animal, Wish
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You're at the animals index.")

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
    
    # render method uses template in '/animals/templates' to return HTML template
    return render(request, 'animals/detail.html', {'animal': animal})

def donate(request, animal_id):
    print (f'The request was: {request}')
    print (request.POST)
    animal = get_object_or_404(Animal, pk=animal_id)
    try:
        wish = Wish.objects.get(pk=request.POST['wish'])
        print (f'Donate to {wish}')
    except (KeyError, Wish.DoesNotExist):
        return render(request, 'animals/detail.html', {'animal': animal, 'error_message': 'Wish does not exist'})
    else:
        return HttpResponse("This is some example text.")