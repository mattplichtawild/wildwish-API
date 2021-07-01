from . import views
from django.urls import path

from . import views

app_name = 'animals'
# 'name' argument is used by django route helpers (in templates and such)
urlpatterns = [
    # Path to index using functional view instead of class based
    path('', views.AnimalListCreate.as_view()),
    
    path('wishes/active', views.WishListCreate.as_view(), name='active_wish_list'),
    
    path('landing', views.create_from_landing),
    # ex: /animals/
    # Index view using django generic view
    # path('', views.IndexView.as_view(), name='animal_index'),

    # ex: /animals/1
    path('<int:pk>', views.AnimalDetail.as_view(), name='detail'),
    path('<int:animal_id>/donate', views.donate, name='donate'),
    # Not very RESTful
    path('<int:animal_id>/wish', views.update_wish, name='update_wish'),
    # path('<int:animal_id>/wishes/<int:wish_id', views.WishDetail.get())
]