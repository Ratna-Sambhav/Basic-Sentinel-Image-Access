from django.urls import path
from .views import satellite_image

urlpatterns = [
    path('', satellite_image, name='satellite_image')
] 
