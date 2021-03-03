from django.contrib.auth import views
from django.urls import path
from parking import views

urlpatterns = [
    path('park-car', views.ParkCarView.as_view(), name='park_car'),
    path('unpark-car', views.UnParkCarView.as_view(), name='unpark_car'),
    path('information/<str:number_type>/<str:number>', views.Information.as_view(), name='information'),
]