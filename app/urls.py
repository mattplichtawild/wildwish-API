"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from animals.views import ActiveWishList
from django.contrib import admin
# from django.views.generic import TemplateView
from django.urls import include, path, re_path
from animals import views

urlpatterns = [
    ## This was to solve client sending requests to routes that were supposed to be handled by react-router-dom
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view()),
    # path('/', TemplateView.as_view(template_name="app.html"), 
    # login_url='l/'),
    # re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="app.html"), 
    # login_url='/'),
    
    # For basic html template
    # path('', ActiveWishList.as_view()),
    
    # For React frontend
    path('', include('frontend.urls')),
    path('animals/', include('animals.urls')),
    path('donations/', include('donations.urls')),
    # path('zoos/', include('zoos.urls')),
    path('images/', include('images.urls')),
    path('admin/', admin.site.urls),
    
    # Should probably separate these into their own app
    path('wishes/<int:pk>', views.WishDetail.as_view()),
    path('wishes/featured', views.WishListFeatured.as_view() ),
    path('wishes/nearby', views.WishListNearby.as_view() )
]