from . import views
from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'users'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# First arg is prefix to use. Keep blank so users/ are created directly on top of /
# ex: r'users_api' would set path as /users/users_api/
router.register(r'', views.UserViewSet)

urlpatterns = [
    # path('', views.UserListCreate.as_view()),
    
    # Copy/paste example from blog
    # TODO: Get rid of this url so paths are RESTful eg: POST to '/users/' does this
    path('create/', views.UserCreate.as_view(), name="create_user"),
    
    path('', include(router.urls)),
]