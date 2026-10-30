from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from restaurant.views import MenuItemViewSet,BookingViewSet
r=DefaultRouter(); r.register("menu-items",MenuItemViewSet); r.register("bookings",BookingViewSet)
urlpatterns=[path("admin/",admin.site.urls),path("api/",include(r.urls)),path("auth/",include("djoser.urls")),path("auth/",include("djoser.urls.authtoken")),path("",include("restaurant.web_urls"))]
