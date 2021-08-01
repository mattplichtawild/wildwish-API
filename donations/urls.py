from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'donations'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# First arg is prefix to use. Keep blank so users/ are created directly on top of /
# ex: r'users_api' would set path as /users/users_api/
router.register(r'', views.DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Path to index using functional view instead of class based
    # path('', views.create_donation, name='donate'),
]