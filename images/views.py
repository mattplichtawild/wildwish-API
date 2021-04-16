from django.http.response import HttpResponse, JsonResponse
# from rest_framework import generics, viewsets
from .models import Image
# from animals.serializers import ImageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# from rest_framework.parsers import MultiPartParser
    
@csrf_exempt
def create_from_landing(request):
    # from .forms import ImageForm
   
    if request.method == 'POST':
        # form = ImageForm(request.POST, request.FILES)
        # print(request.POST, request.FILES, form.is_valid(), form)
        # if form.is_valid():
        #     form.save()
        #      # img_obj = Image.objects.create(upload=request.POST['upload'])
        # img = form.instance
        
        file = request.FILES['file']
        img = Image(upload=file)
        img.save()
        
        print(img)
        return HttpResponse(img)
    
    
## First attempt using 'django-rest-framework'
## Maybe refactor this later for other use?
# @csrf_exempt
# @api_view(['POST'])
# class ImageDetail(viewsets.ModelViewSet):
#     parser_classes = [MultiPartParser]
    
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
    
#     @csrf_exempt
#     def create(self, validated_data):
#         pass