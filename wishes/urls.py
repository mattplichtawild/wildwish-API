from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'wishes'

router = routers.DefaultRouter()
router.register(r'', views.WishViewSet)

urlpatterns = [
    path('', include(router.urls)),
]