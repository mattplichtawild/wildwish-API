from django.http.response import JsonResponse
from animals.models import Animal
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
    
    # render method uses template in '/animals/templates' to return HTML template
    return render(request, 'animals/detail.html', {'animal': animal})

    # Below method is same as 'get_object_or_404' method above
    # try:
    #     animal = Animal.objects.get(pk=animal_id)
    # except Animal.DoesNotExist:
    #     raise Http404("Animal does not exist")
    # return render(request, 'animals/detail.html', {'animal': animal})