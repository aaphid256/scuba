
from django.urls import path

from . import views

urlpatterns = [
    path("dives", views.index, name="index"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('dives/<int:pk>/', views.dive_detail, name='dive_detail'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination_detail'),
    #path('create_dive/', views.create_dive, name='create_dive'),
    #path('create_destination/', views.create_destination, name='create_destination'),
]
