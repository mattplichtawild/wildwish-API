from . import views
# from rest_framework import routers
from rest_framework_nested import routers
from django.urls import path, include
from . import views
from animals.views import AnimalViewSet

app_name = 'users'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# First arg is prefix to use. Keep blank so users/ are created directly on top of /
# ex: r'users_api' would set path as /users/users_api/
router.register(r'', views.UserViewSet)

users_router = routers.NestedSimpleRouter(router, r'', lookup='user')
users_router.register(r'animals', AnimalViewSet)

urlpatterns = [
    # path('', views.UserListCreate.as_view()),
    
    path('register/', views.UserCreate.as_view(), name="create_user"),
    
    path('', include(router.urls)),
    path('', include(users_router.urls))
]