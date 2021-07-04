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
    path('', include(router.urls)),
]