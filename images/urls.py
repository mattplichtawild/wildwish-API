from . import views
from django.urls import path


app_name = 'images'
# 'name' argument is used by django route helpers (in templates and such)
urlpatterns = [
    
    # Handles submissions from dropzone on static landing page
    path('landing', views.create_from_landing),
    
]