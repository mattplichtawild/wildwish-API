from django.urls import include, path
# from rest_framework import routers
from rest_framework_nested import routers
from . import views
from images.views import ImageViewSet

app_name = 'wishes'

router = routers.DefaultRouter()
router.register(r'', views.WishViewSet)

wishes_router = routers.NestedSimpleRouter(router, r'', lookup='wish')
wishes_router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(wishes_router.urls))
]