from animals.views import donate
from django.urls import path

from . import views

app_name = 'animals'
# 'name' argument is used by django route helpers (in templates and such)
urlpatterns = [
    # Path to index using functional view instead of class based
    # path('', views.index, name='animals_index'),
    
    # ex: /animals/
    path('', views.IndexView.as_view(), name='index'),
    
    # ex: /animals/1
    path('<int:animal_id>/', views.detail, name='detail'),
    
    path('<int:animal_id>/donate', views.donate, name='donate')
]