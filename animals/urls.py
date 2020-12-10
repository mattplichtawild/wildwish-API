from . import views
from django.urls import path

from . import views

app_name = 'animals'
# 'name' argument is used by django route helpers (in templates and such)
urlpatterns = [
    # Path to index using functional view instead of class based
    path('', views.index, name='animals_index'),
    
    # ex: /animals/
    # Index view using django generic view
    # path('', views.IndexView.as_view(), name='animal_index'),
    path('api', views.AnimalListCreate.as_view() ),
    
    # ex: /animals/1
    path('<int:animal_id>', views.detail, name='detail'),
    path('<int:animal_id>/donate', views.donate, name='donate'),
    # Not very RESTful
    path('<int:animal_id>/wish', views.update_wish, name='update_wish')
]