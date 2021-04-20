from django.http.response import HttpResponse, JsonResponse
# from rest_framework import generics, viewsets
from .models import Image
# from animals.serializers import ImageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
# from rest_framework.parsers import MultiPartParser
    
@csrf_exempt
def create_from_landing(request):
    uuid = request.POST['uuid']
    if request.method == 'POST':
        # There will only be one file in list due to each file auto uploading from form
        file = request.FILES['file']
        
        img = Image(upload=file, uuid=uuid)

        img.save()
        
        # Using django's form api
        # Doesn't play well with the way RDU is sending request
        # from .forms import ImageForm
        # form = ImageForm(request.POST, request.FILES)
        # print(request.POST, request.FILES, form.is_valid(), form)
        # if form.is_valid():
        #     form.save()
        #      # img_obj = Image.objects.create(upload=request.POST['upload'])
        # img = form.instance
        
        return HttpResponse(img)
    
    
## First attempt using 'django-rest-framework'
## Maybe refactor this later for other use?
# @api_view(['POST'])
# class ImageDetail(viewsets.ModelViewSet):
#     parser_classes = [MultiPartParser]
    
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
    
#     @csrf_exempt
#     def create(self, validated_data):
#         pass