from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the animals index.")

def detail(request, animal_id):
    return HttpResponse("This is the profile page of animal %s" % animal_id)
    