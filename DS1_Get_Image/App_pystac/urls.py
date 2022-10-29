from django.urls import path
from .views import main, dataDetail, list

urlpatterns = [
    path('', main.as_view(), name='main'),
    path('redirected_detail/<int:pk>/', dataDetail.as_view(), name='listDetail'),
    path('allEntries', list.as_view(), name='allEntries'),
] 
