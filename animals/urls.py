from . import views
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'animals'
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# First arg is prefix to use. Keep blank so users/ are created directly on top of /
# ex: r'users_api' would set path as /users/users_api/
router.register(r'', views.AnimalViewSet)

# 'name' argument is used by django route helpers (in templates and such)
urlpatterns = [
    path('', include(router.urls)),
    
    # Path to index using functional view instead of class based
    path('', views.AnimalListCreate.as_view()),
    
    path('wishes/active', views.WishListCreate.as_view(), name='active_wish_list'),
    
    path('landing', views.create_from_landing),
    # ex: /animals/
    # Index view using django generic view
    # path('', views.IndexView.as_view(), name='animal_index'),

    # ex: /animals/1
    # path('<int:pk>', views.AnimalDetail.as_view(), name='detail'),
    path('<int:animal_id>/donate', views.donate, name='donate'),
    # Not very RESTful
    path('<int:animal_id>/wish', views.update_wish, name='update_wish'),
    # path('<int:animal_id>/wishes/<int:wish_id', views.WishDetail.get())
]