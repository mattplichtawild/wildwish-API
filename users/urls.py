from . import views
from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'users'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.UserListCreate.as_view()),
    path('', include(router.urls)),
]