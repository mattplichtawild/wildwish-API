from django.urls import path

from . import views

urlpatterns = [
    # ex: /animals/
    path('', views.index, name='animals_index'),
    
    # ex: /animals/1
    path('<int:animal_id>/', views.detail, name='detail')
]